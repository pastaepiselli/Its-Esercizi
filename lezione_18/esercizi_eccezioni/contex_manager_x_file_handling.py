
try:
    with open('safe_square_root.py') as file:
        content = file.read()
        print("File content:")
        print(content)
except IOError as e:
    print(f"Si è verificato un errore durante la lettura del file: {e}")