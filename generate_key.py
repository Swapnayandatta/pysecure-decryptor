from cryptography.fernet import Fernet

# Generate a key and save it into a file
key = Fernet.generate_key()
with open("thekey.key", "wb") as key_file:
    key_file.write(key)

print("✅ Key generated and saved as 'thekey.key'")

