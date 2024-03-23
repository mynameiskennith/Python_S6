num = input('ENter a number : ')
arm = 0
for i in num:
    arm += int(i)**3

print(f'{num} is {'Armstrong' if arm==num else 'Not Armstrong' if arm!=0 else ''}')