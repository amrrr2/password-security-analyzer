import csv
from colorama import Fore, Style, init

init(autoreset=True)


def check_strength(password):

    SpecialChars = ["$", "@", "*", "&", "!", "#", "%"]

    score = 0

    if any(c in password for c in SpecialChars):
        score += 1

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(not c.isalnum() for c in password):
        score += 1

    return score


def password_tips(score):

    if score <= 2:
        return "Weak Password -> Add uppercase letters, numbers and symbols."

    elif score <= 4:
        return "Medium Password -> Make it longer and add more symbols."

    else:
        return "Strong Password -> Good job."


def filereader(filePath):

    with open(filePath, "r", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            name = row["name"]
            password = row["password"]

            score = check_strength(password)

            tip = password_tips(score)

            print(
                Fore.LIGHTBLACK_EX + "Website Name: "
                + Style.RESET_ALL
                + f"{name} "
                + Fore.LIGHTBLACK_EX + "|||| Password: "
                + Style.RESET_ALL
                + f"{password} "
                + Fore.LIGHTBLACK_EX + "|||| Score: "
                + Style.RESET_ALL
                + f"{score}"
            )

            print(
                Fore.YELLOW + "Tip: "
                + Style.RESET_ALL
                + tip
            )

            print("-" * 70)


if __name__ == "__main__":

    targetfile=input("Enter your file path: ").strip('"')
    filereader(targetfile)