import hashlib

def crack_passwords(wordlist_file_path, hash_file_path):
    hashedlist = []
    print("Prepping...")
    try:
        with open(hash_file_path, 'r') as f:
            hashlist = [line.strip() for line in f]
            for line in hashlist:
                hash_clean = line.strip()
                hashedlist.append(hash_clean)
    except:
        print("Error: Your list of hashes does not exist.")
        quit(1)
    print("Ready!")
    crackedhashes = []
    finallist = []
    print("Begin cracking...")
    try:
        with open(wordlist_file_path, 'r') as f:
            wordlist = [line.strip() for line in f]
            if not wordlist:
                print("Your wordlist is empty. Kinda hard to crack hashes without anything to refernce.")
            for line in wordlist:
                word_clean = line.strip()
                word_encoded = hashlib.md5(word_clean.encode())
                word_hex = word_encoded.hexdigest()
                if word_hex in hashlist:
                    print(f"Password cracked! Hash {word_hex} is equivalent to the password {word_clean}.")
                    crackedhashes.append(word_hex)
                elif not hashlist:
                    print("Your list of hashes is empty. Can't exactly crack nothing.")
            for item in hashlist:
                if item not in crackedhashes:
                    print(f"Failed to crack hash {item}.")
                    finallist.append(f"{item}, uncracked")
                elif item in crackedhashes:
                    finallist.append(f"{item}, cracked")
                    
            print("Done!")
            return finallist
    except FileNotFoundError:
        print("Error: Your wordlist does not exist.")
        quit(1)
