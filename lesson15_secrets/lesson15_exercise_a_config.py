import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ENV_FILE = Path(__file__).parent.parent / ".env"

TRUE_VALUES = {"true", "1", "yes", "on"}
FALSE_VALUES = {"false", "0", "no", "off"}


@dataclass
class Config:
    app_name: str
    debug: bool
    max_retries: int
    weather_city: str
    api_key: str


def parse_bool(value: str) -> bool:
    formated = value.strip().lower()
    if formated in TRUE_VALUES:
        return True
    elif formated in FALSE_VALUES:
        return False
    else:
        raise ValueError(f"Not a boolean: {value}")


def require(name: str) -> str:
    value = os.getenv(name)
    if value is None or not value.strip():
        raise RuntimeError(f"Missing required setting: {name}")
    return value


def mask(secret: str) -> str:
    if len(secret) < 8:
        return "****"
    return f"{secret[:4]}...{secret[-4:]}"


def load_config(env_file: Path) -> Config:
    load_dotenv(env_file)
    return Config(
        app_name=require("APP_NAME"),
        debug=parse_bool(require("DEBUG")),
        max_retries=int(require("MAX_RETRIES")),
        weather_city=os.getenv("WEATHER_CITY", "Sofia"),
        api_key=require("DEMO_API_KEY")
    )


def main() -> None:
    print("=== Config ===")
    try:
        config = load_config(ENV_FILE)
        print(f"App: {config.app_name}")
        print(f"Debug: {config.debug}")
        print(f"Max retries: {config.max_retries}")
        print(f"Weather city: {config.weather_city}")
        print(f"API key: {mask(config.api_key)}")
    except (RuntimeError, ValueError) as e:
        print(f"Config error: {e}")


if __name__ == "__main__":
    main()