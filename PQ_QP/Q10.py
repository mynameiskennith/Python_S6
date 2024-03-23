dict = {'ram': '20th March','g' : '15th May','a' : '14th March'}

name=input()
if name in dict:
    print(f'Birthday of {name} is on {dict[name]}')
else:
    print('Your name is not in Dictionary')