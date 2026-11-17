# Lesson 14: Web APIs with requests
# Every code snippet from the lesson, in order.
# Lines that would crash on purpose are commented out with ❌ so the file runs top to bottom.
# Needs an internet connection and the requests package (installed in Lesson 12).
# APIs used (free, no key): jsonplaceholder.typicode.com (fake test data), httpbin.org (echoes your request),
# open-meteo.com (real weather).

from dataclasses import dataclass

import requests


# ============================================================
# 1. Your first GET request
# ============================================================

response = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=10)

print(response.status_code)                  # 200
print(response.ok)                           # True  (any status below 400)
print(response.headers["Content-Type"])      # application/json; charset=utf-8
print(response.text[:40])                    # the raw JSON text: {\n  "id": 1,\n  "name": "Leanne Graham", ...

user = response.json()                       # parse the JSON body -> dict (json.loads for you)
print(user["name"])                          # Leanne Graham
print(user["address"]["city"])               # Gwenborough


# ============================================================
# 2. Query parameters: let requests build the URL
# ============================================================

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos",
    params={"userId": 1, "completed": "true"},
    timeout=10,
)
print(response.url)          # https://jsonplaceholder.typicode.com/todos?userId=1&completed=true
todos = response.json()      # a LIST of dicts this time
print(len(todos))            # 11
print(todos[0]["title"])     # et porro tempora

# params also escapes special characters for you:
response = requests.get("https://httpbin.org/get", params={"q": "café & tea"}, timeout=10)
print(response.url)          # https://httpbin.org/get?q=caf%C3%A9+%26+tea
print(response.json()["args"])   # {'q': 'café & tea'}


# ============================================================
# 3. Status codes
# ============================================================

# 200 OK            201 Created
# 400 Bad Request   401 Unauthorized (bad/missing API key)   403 Forbidden
# 404 Not Found     429 Too Many Requests (rate limit)
# 500 / 502 / 503   the server's fault

response = requests.get("https://jsonplaceholder.typicode.com/users/999", timeout=10)
print(response.status_code)      # 404
print(response.ok)               # False
print(response.json())           # {}   <- requests does NOT raise on 404 by itself!

if response.status_code == 404:
    print("No such user")


# ============================================================
# 4. raise_for_status(): turn bad status codes into exceptions
# ============================================================

response = requests.get("https://httpbin.org/status/404", timeout=10)
try:
    response.raise_for_status()          # does nothing for 2xx, raises HTTPError for 4xx/5xx
except requests.HTTPError as e:
    print(f"HTTP error: {e}")            # HTTP error: 404 Client Error: Not Found for url: ...

# The usual pattern inside a function:
def get_user(user_id: int) -> dict:
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}", timeout=10)
    response.raise_for_status()          # stop here if it failed
    return response.json()               # only reached on success


print(get_user(2)["name"])               # Ervin Howell
# get_user(999)                          # ❌ requests.HTTPError: 404 Client Error


# ============================================================
# 5. Network errors and timeouts
# ============================================================

# ALWAYS pass timeout=...  Without it, a hanging server can freeze your program forever.

try:
    requests.get("https://httpbin.org/delay/5", timeout=1)     # server waits 5s, we wait 1s
except requests.Timeout:
    print("The server took too long.")

try:
    requests.get("https://this-domain-does-not-exist-12345.com", timeout=5)
except requests.ConnectionError:
    print("Could not connect.")          # no internet, wrong address, DNS failure...

# Exception family (like a Java exception hierarchy):
# requests.RequestException          <- catch this to handle EVERYTHING below
#     ├── requests.ConnectionError
#     ├── requests.Timeout
#     └── requests.HTTPError         (from raise_for_status)

try:
    get_user(999)
except requests.Timeout:                 # specific first...
    print("Too slow.")
except requests.RequestException as e:   # ...general last (same rule as Lesson 9)
    print(f"Request failed: {e}")


# ============================================================
# 6. POST: sending data
# ============================================================

new_post = {"userId": 1, "title": "Hello", "body": "Sent from Python"}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=new_post, timeout=10)
# json=...  turns the dict into JSON AND sets the header Content-Type: application/json

print(response.status_code)      # 201  (Created)
print(response.json())           # {'userId': 1, 'title': 'Hello', 'body': 'Sent from Python', 'id': 101}
# (jsonplaceholder is fake: it answers like a real API but doesn't really save anything)


# ============================================================
# 7. Headers: how API keys are sent
# ============================================================

headers = {
    "Authorization": "Bearer fake-key-123",      # the standard way to send an API key
    "User-Agent": "python-learning/1.0",
}
response = requests.post("https://httpbin.org/post", json={"name": "Ana"}, headers=headers, timeout=10)
echo = response.json()                            # httpbin sends back what it received
print(echo["json"])                               # {'name': 'Ana'}
print(echo["headers"]["Authorization"])           # Bearer fake-key-123


# ============================================================
# 8. A real API: current weather (Open-Meteo, no key needed)
# ============================================================

geo = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": "Sofia", "count": 1},
    timeout=10,
).json()
city = geo["results"][0]
print(city["name"], city["country"], city["latitude"], city["longitude"])
# Sofia Bulgaria 42.69751 23.32415

weather = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "current": "temperature_2m,wind_speed_10m",
    },
    timeout=10,
).json()
print(weather["current"])            # {'time': '...', 'interval': 900, 'temperature_2m': 14.7, 'wind_speed_10m': 5.6}

# A search with no matches has NO "results" key at all:
nothing = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name": "Xyzzyqq", "count": 1},
    timeout=10,
).json()
print(nothing)                       # {'generationtime_ms': 0.06...}
# nothing["results"]                 # ❌ KeyError: 'results'
print(nothing.get("results"))        # None   <- check with .get() first


# ============================================================
# 9. Wrapping an API in functions and dataclasses
# ============================================================

BASE_URL = "https://jsonplaceholder.typicode.com"


@dataclass
class Post:
    id: int
    title: str

    @classmethod
    def from_dict(cls, data: dict) -> "Post":
        return cls(data["id"], data["title"])


def get_posts(user_id: int) -> list[Post]:
    response = requests.get(f"{BASE_URL}/posts", params={"userId": user_id}, timeout=10)
    response.raise_for_status()
    return [Post.from_dict(item) for item in response.json()]


posts = get_posts(1)
print(len(posts))            # 10
print(posts[0])              # Post(id=1, title='sunt aut facere repellat provident ...')

# The rest of the program only sees Post objects: it doesn't care about URLs or JSON.


# ============================================================
# 10. Session: reuse one connection for many requests
# ============================================================

with requests.Session() as session:
    session.headers.update({"User-Agent": "python-learning/1.0"})   # sent with EVERY request
    for user_id in (1, 2, 3):
        r = session.get(f"{BASE_URL}/users/{user_id}", timeout=10)
        print(r.json()["name"])
# Leanne Graham
# Ervin Howell
# Clementine Bauch


# ============================================================
# 11. Preview: the OpenAI API is just another POST
# ============================================================

# Don't run this yet: you need an API key (Lessons 15 and 16).
#
# response = requests.post(
#     "https://api.openai.com/v1/responses",
#     headers={"Authorization": f"Bearer {api_key}"},
#     json={"model": "gpt-5-mini", "input": "Say hello"},
#     timeout=30,
# )
# response.raise_for_status()
# data = response.json()
# print(data["output"][0]["content"][0]["text"])
#
# In Lesson 17 the openai library will do exactly this for you.
