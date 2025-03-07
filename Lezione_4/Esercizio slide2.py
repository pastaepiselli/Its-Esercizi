def check_length(a: str) -> None:
    if len(a) == 10:
        print(f"{a} The string has 10 characters")
    elif len(a) > 10:
        print(f"{a} The string is longer than 10 characters")
    else:
        print(f"{a} The string is shoter than 10 characters")


check_length("Oggi pier damien e molto felice")
check_length("Popa e triste")