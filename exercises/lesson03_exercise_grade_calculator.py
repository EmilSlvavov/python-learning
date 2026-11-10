text = input("Give a score from 0 - 100: ").strip()
if not text:
    print("No score entered.")
else:
    score = int(text)
    if score < 0 or score > 100:
        print("Invalid score.")
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        result = "Passed" if score >= 60 else "Failed"
        print(f"Grade: {grade}")
        print(result)
        if score == 100:
            print("Perfect score!")
