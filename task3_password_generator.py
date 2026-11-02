import secrets
import string


def generate_password(length, use_digits=True, use_symbols=True):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Ensure the selected character groups are represented when enabled.
    required_groups = [string.ascii_lowercase, string.ascii_uppercase]
    if use_digits:
        required_groups.append(string.digits)
    if use_symbols:
        required_groups.append(string.punctuation)

    if length < len(required_groups):
        raise ValueError(
            f"Choose a length of at least {len(required_groups)} "
            "for the selected options."
        )

    password_chars = [
        secrets.choice(group) for group in required_groups
    ]
    password_chars.extend(
        secrets.choice(characters)
        for _ in range(length - len(password_chars))
    )

    # Securely shuffle the characters so required groups are not predictable.
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def ask_yes_no(prompt, default=True):
    answer = input(prompt).strip().lower()
    if answer == "":
        return default
    return answer in ("y", "yes")


def main():
    print("========== PASSWORD GENERATOR ==========")

    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Please choose a length of at least 4.")
            return
    except ValueError:
        print("Please enter a whole number for the length.")
        return

    use_digits = ask_yes_no("Include numbers? (Y/n): ")
    use_symbols = ask_yes_no("Include symbols? (Y/n): ")

    try:
        password = generate_password(length, use_digits, use_symbols)
        print("\nGenerated password:")
        print(password)
        print("\nKeep your password private and store it securely.")
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
