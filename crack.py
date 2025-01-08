import hashlib
import itertools
import sys
import time

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

def rainbow_table_attack(hash, rainbow_table):
    with open(rainbow_table, 'r') as file:
        for line in file:
            if line.startswith(hash):
                return line.split(':')[1].strip()
    return None

def main():
    if len(sys.argv) < 5:
        print("Usage: python crack.py --hash <hash> --method <method> [--wordlist <wordlist>] [--rainbow <rainbow_table>]")
        sys.exit(1)

    hash = sys.argv[2]
    method = sys.argv[4]
    wordlist = sys.argv[6] if '--wordlist' in sys.argv else None
    rainbow_table = sys.argv[6] if '--rainbow' in sys.argv else None

    print(f"Hash: {hash}")
    print(f"Identified algorithm: {identify_hash(hash)}")

    start_time = time.time()
    result = None

    if method == 'dictionary':
        if not wordlist:
            print("Wordlist is required for dictionary attack")
            sys.exit(1)
        print("Starting dictionary attack...")
        result = dictionary_attack(hash, wordlist)
    elif method == 'brute-force':
        print("Starting brute-force attack...")
        result = brute_force_attack(hash, 'abcdefghijklmnopqrstuvwxyz', 8)
    elif method == 'rainbow':
        if not rainbow_table:
            print("Rainbow table is required for rainbow table attack")
            sys.exit(1)
        print("Starting rainbow table attack...")
        result = rainbow_table_attack(hash, rainbow_table)
    else:
        print("Unknown method")
        sys.exit(1)

    end_time = time.time()

    if result:
        print(f"Cracked password: {result}")
    else:
        print("Password not found")

    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
