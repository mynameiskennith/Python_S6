str = input()
key = int(input('ENter the key : '))
cipher = ''
for i in str:
    pos=ord(i)
    ci = pos+key
    cipher+=chr(ci)
print(f'{str} => {cipher}')

# print(ord('z'))
# print(ord('a'))
# print(ord('z')+1)
# print(ord('A'))
# print(chr(97))