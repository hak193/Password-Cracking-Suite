import hashlib
import itertools
import sys

def identify_hash(hash):
    hash_algorithms = {
        32: 'MD5',
        40: 'SHA1',
        64: 'SHA256'
    }
    return hash_algorithms.get(len(hash), 'Unknown')

def dictionary_attack(hash, wordlist):
    with open(wordlist, 'r') as file:
        for word in file:
            word = word.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash:
                return word
    return None

def brute_force_attack(hash, charset, max_length):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess = ''.join(guess)
            if hashlib.md5(guess.encode()).hexdigest() == hash:
                return guess
    return None

def main():
    if len(sys.argv) != 5:
        print("Usage: python crack.py --hash <hash> --method <method> --wordlist <wordlist>")
        sys.exit(1)

    hash = sys.argv[2]
    method = sys.argv[4]
    wordlist = sys.argv[6]

    print(f"Hash: {hash}")
    print(f"Identified algorithm: {identify_hash(hash)}")

    if method == 'dictionary':
        print("Starting dictionary attack...")
        result = dictionary_attack(hash, wordlist)
    elif method == 'brute-force':
        print("Starting brute-force attack...")
        result = brute_force_attack(hash, 'abcdefghijklmnopqrstuvwxyz', 8)
    else:
        print("Unknown method")
        sys.exit(1)

    if result:
        print(f"Cracked password: {result}")
    else:
        print("Password not found")

if __name__ == "__main__":
    main()
