a = list(input('Enter a string: '))
vowel = 0
const = 0

for i in a:
    if i in ['a', 'e', 'i', 'o', 'u']:  # Corrected condition
        vowel += 1
    elif i.isalpha():
        const += 1

print('Vowels:', vowel, '\nConsonants:', const)
