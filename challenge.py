import hashlib
import random
import string

def sha256(x): 
    return hashlib.sha256(x.encode()).hexdigest()

def load_cheeses(filename="cheese.txt"):
    with open(filename, "r") as f:
        cheeses = [line.strip() for line in f if line.strip()]
    return cheeses

def generate_playfair_key_matrix(key):
    key = key.upper().replace("J", "I")  
    matrix = []
    used = set()
    for char in key:
        if char not in used and char in string.ascii_uppercase:
            matrix.append(char)
            used.add(char)
    for char in string.ascii_uppercase:
        if char == "J":  # skip J
            continue
        if char not in used:
            matrix.append(char)
            used.add(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val == char:
                return r, c
    return None

def playfair_encrypt(text, matrix):
    text = text.upper().replace("J", "I")
    prepared = []
    i = 0
    while i < len(text):
        a = text[i]
        b = ""
        if i+1 < len(text):
            b = text[i+1]
        if a == b:
            b = "X"
            i += 1
        else:
            i += 2
        if b == "":
            b = "X"
        prepared.append((a, b))
    cipher = ""
    for a, b in prepared:
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)
        if r1 == r2:  
            cipher += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:
            cipher += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:  
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

def cipher_to_lr(cipher_text):
    sequence = ""
    for ch in cipher_text:
        if not ch.isalpha():
            continue
        idx = ord(ch) - ord('A') + 1
        if idx % 2 == 0:
            sequence += "L"
        else:
            sequence += "R"
    return sequence

def main():
    print("🐭 Welcome to the Mouse & Cheese Playfair Challenge! ")

    cheeses = load_cheeses("cheese.txt")
    cheese = random.choice(cheeses)
    target_hash = sha256(cheese)

    print("\nThe mouse whispers: 'Here’s the hash of my cheese...'")
    print("Hash:", target_hash)

    user_cheese = input("\n🔍 Enter the cracked cheese word: ").strip()
    if user_cheese.lower() != cheese.lower():
        print("Wrong cheese! The mouse stays trapped...")
        return

    print("Correct cheese! Now, encrypt it with a cipher, Wheatstone's friend loved to play so much...")

    matrix = generate_playfair_key_matrix("mousecheese")
    cipher_text = playfair_encrypt(user_cheese.upper(), matrix)

    user_cipher = input("\nEnter the Playfair ciphertext: ").strip().upper()

    if user_cipher != cipher_text:
        print("\n[!] Wrong ciphertext! The mouse shakes its head...")
        return

    print("\n[+] Correct ciphertext! The mouse is impressed.")
    print("\n Clue for the final path:")
    print("   Oh, maybe the 'odd' ones are always 'left (L)' out in the list.")
    print("   And the rest all are 'right' to be split 'even'! ")
    print("   Work it out, smartie! ")

    correct_lr = cipher_to_lr(cipher_text)
    print(correct_lr)
    user_lr = input("\nEnter the full sequence: ").strip().upper()

    if user_lr == correct_lr:
        print("\n CYBER{m0u$etr@p}")
    else:
        print("\n [!] Wrong sequence using L/R! The mouse laughs at your attempt...")

if _name_ == "_main_":
    main()
