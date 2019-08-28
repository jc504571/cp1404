"""CP1404/CP5632 - Practical
program using a function"""


def main():
    """get a numeric value and display its score"""
    score = float(input("Enter score: "))
    value = determine_grade(score)
    print(value)


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
