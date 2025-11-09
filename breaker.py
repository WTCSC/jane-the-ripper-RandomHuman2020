
from functs import crack_passwords

print("Welcome to Jane the Ripper!")
   

def main():
    wordlist_path = input("Please input the path to your wordlist.\n> ")
    hashlist_path = input("Please input the path to the list of hashes you would like to crack.\n> ")
    crack_passwords(wordlist_path, hashlist_path)


main()