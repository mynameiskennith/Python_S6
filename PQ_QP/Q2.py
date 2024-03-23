nums = list(map(int,input('Enter the numbers : ').split()))

e_count=sum(1 for i in nums if i%2==0)
o_count=sum(1 for i in nums if i%2!=0)

print(f'The number of Odd Numbers are {o_count}')
print(f'The number of even numbers are {e_count}')

# nums = list(map(int,input('Enter the numbers : ').split()))
# print(nums)
# e_count = 0
# o_count = 0
# for i in nums:
#     if i%2==0:
#         e_count+=1
#     elif i%2!=0:
#         o_count+=1
#     else:
#         pass
# print(f'The number of even numbers are {e_count}')
# print(f'The number of odd numbers are {o_count}')

