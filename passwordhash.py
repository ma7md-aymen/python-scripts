#this code shoude take input from a file and hash it into md5 hash then add a prefix then encoded into base64
#and it work form the first time 🥹
import hashlib , base64

with open('password.txt') as password :
    for word in password:
        md5_of_encoded = hashlib.md5(word.encode()).hexdigest()
        prefix = 'carlos:' + md5_of_encoded
        encoded = base64.b64encode(prefix.encode()).decode()
        print(encoded)
