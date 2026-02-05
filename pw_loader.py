import os


def load_passwords():
    pw_storage = 'passwords'
    files = os.listdir(pw_storage)

    passwords = []
    for file in files:
        # Read using latin-1 to preserve raw bytes as-is (safe for password lists)
        with open(f'{pw_storage}/{file}', 'r', encoding='latin-1') as f:
            text = f.read()

        lines = text.split()
        passwords += lines

    return set(passwords)


if __name__ == '__main__':
    passwords = load_passwords()
    print(len(passwords))
