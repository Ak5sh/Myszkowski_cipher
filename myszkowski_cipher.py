# Myszkowski Cipher Implementation (Menu Driven)

def validate_key(key):
    if not key.isalpha():
        print("Key must contain only alphabets.")
        return False
    return True


# USER-DEFINED HASH FUNCTION (Modify this if needed)
def custom_hash_function(key):
    """
    This function assigns ranks to characters in the key.
    Same letters get same rank (Myszkowski rule).
    """
    key = key.lower()
    rank = [0] * len(key)
    current_rank = 1

    for i in range(len(key)):
        if rank[i] == 0:
            rank[i] = current_rank
            for j in range(i + 1, len(key)):
                if key[i] == key[j]:
                    rank[j] = current_rank
            current_rank += 1

    return rank


def create_matrix(text, cols):
    rows = len(text) // cols
    matrix = []
    k = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(text[k])
            k += 1
        matrix.append(row)
    return matrix


def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").lower()

    if not validate_key(key):
        return

    cols = len(key)

    # Padding
    while len(plaintext) % cols != 0:
        plaintext += 'x'

    matrix = create_matrix(plaintext, cols)
    rank = custom_hash_function(key)

    ciphertext = ""

    for r in sorted(set(rank)):
        indices = [i for i in range(len(rank)) if rank[i] == r]

        if len(indices) == 1:
            col = indices[0]
            for row in matrix:
                ciphertext += row[col]
        else:
            for row in matrix:
                for col in indices:
                    ciphertext += row[col]

    return ciphertext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.replace(" ", "").lower()

    if not validate_key(key):
        return

    cols = len(key)
    rows = len(ciphertext) // cols

    rank = custom_hash_function(key)

    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    k = 0

    for r in sorted(set(rank)):
        indices = [i for i in range(len(rank)) if rank[i] == r]

        if len(indices) == 1:
            col = indices[0]
            for i in range(rows):
                matrix[i][col] = ciphertext[k]
                k += 1
        else:
            for i in range(rows):
                for col in indices:
                    matrix[i][col] = ciphertext[k]
                    k += 1

    plaintext = ""
    for row in matrix:
        plaintext += ''.join(row)

    return plaintext


def main():
    while True:
        print("\n=== Myszkowski Cipher Menu ===")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            text = input("Enter plaintext: ")
            key = input("Enter key: ")

            result = encrypt(text, key)
            if result:
                print("Encrypted Text:", result)

        elif choice == '2':
            text = input("Enter ciphertext: ")
            key = input("Enter key: ")

            result = decrypt(text, key)
            if result:
                print("Decrypted Text:", result)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()