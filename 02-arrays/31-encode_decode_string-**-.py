import base64

text = "Hello world."
print(f'Text : {text}')
encoded_text = base64.b64encode(text.encode('utf-8'))       # encode is inside bcz base64 needs to be in byte formate to convert
print(f'Encoded text : {encoded_text}')

decoded_text = base64.b64decode(encoded_text).decode('utf-8')
print(f'Decoded text : {decoded_text}')

