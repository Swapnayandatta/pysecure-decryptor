import os
from cryptography.fernet import Fernet

# Collect all files except the scripts and key file
files = []
for file in os.listdir():
    if file in ["encrypt.py", "decrypt.py", "generate_key.py", "thekey.key"]:
        continue
    if os.path.isfile(file):
        files.append(file)

# Read the encryption key
with open("thekey.key", "rb") as key_file:
    secret_key = key_file.read()

# Encrypt each file
for file in files:
    with open(file, "rb") as original_file:
        content = original_file.read()
    encrypted_content = Fernet(secret_key).encrypt(content)
    with open(file, "wb") as encrypted_file:
        encrypted_file.write(encrypted_content)

print("🔐 All files encrypted successfully.")

