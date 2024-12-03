import sys
import base64
from nacl.public import PublicKey, SealedBox

def encrypt_message(public_key_base64, text_string):
    public_key_bytes = base64.b64decode(public_key_base64)

    if len(public_key_bytes) != PublicKey.SIZE:
        print("Invalid public key length. Expected 32 bytes.")
        sys.exit(1)

    public_key = PublicKey(public_key_bytes)
    box = SealedBox(public_key)
    encrypted_message = box.encrypt(text_string.encode('utf-8'))
    encrypted_message_base64 = base64.b64encode(encrypted_message).decode('utf-8')
    print(encrypted_message_base64)

def main():
    # Ensure the script gets two arguments (public_key and text_string)
    if len(sys.argv) != 3:
        print("Usage: python3 encrypt_message.py <public_key_base64> <text_string>")
        sys.exit(1)

    public_key_base64 = sys.argv[1]  # First argument: public key in base64
    text_string = sys.argv[2]         # Second argument: text string to encrypt

    encrypt_message(public_key_base64, text_string)

if __name__ == "__main__":
    main()
