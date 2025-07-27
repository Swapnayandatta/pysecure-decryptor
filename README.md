Developed a secure file encryption and decryption tool in Python using the cryptography library's Fernet symmetric encryption. The tool encrypts all files in a specified directory (excluding script and key files) and allows them to be safely decrypted using the same key.

Key Features:

Implemented Fernet symmetric encryption, which ensures confidentiality, integrity, and authenticity of file contents.

Created three modular scripts:

Key Generator (generate_key.py): Generates a secure Fernet key and stores it in thekey.key.

File Encryptor (encrypt.py): Encrypts all eligible files in the current directory using the saved key.

File Decryptor (decrypt.py): Decrypts the previously encrypted files using the same key.

Ensured that sensitive scripts and key files are excluded from encryption to avoid accidental data loss.

Performed secure file read/write operations in binary mode to maintain file integrity.

Tools & Technologies:

Python 3.x

cryptography library (Fernet)

File handling with os and open()

Symmetric key encryption (AES under the hood via Fernet)
