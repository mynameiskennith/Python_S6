# fact = 1
# for i in range(1,int(input('Enter the number : '))+1):
#     fact*=i
# print(f'Factorial = {fact}')

def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

print(f'Factorial = {factorial(int(input('Enter the number : ')))}')