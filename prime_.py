num = int(input('ENter a number'))

print(f'{num} is {"prime" if all(num % i != 0 for i in range(2, int(num**0.5) + 1)) else 'not prime'}')