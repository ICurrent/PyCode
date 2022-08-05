text = "Welcome"
new_text = []
key = 13
for i in text:
    encode = ord(i) + key
    new_text.append(chr(encode))

new_text = ''.join(new_text)

print(f"Word: {text}")
print(f"Encryption: {new_text}")
print(f"Decryption: ")