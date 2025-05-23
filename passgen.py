#this script make two lists
#one for the users
#one for the password
#it should print carlos in user list and carlos password then print wiener then wiener password form file
print('################The user list###################')
for i in range(150):
    if i % 3 :
        print('carlos')
    else:
        print('wiener')



print('################The password list###################')
with open('password.txt', 'r') as f:
    line = f.readline()
    i = 0
    for l in f:
        if i % 3:
            print(l.strip())
            i = i + 1
        else:
            print('peter')
            i = i + 1
