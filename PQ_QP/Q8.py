import math
x1,y1=map(int,input('Enter the 1st Coordinates : ').split())
x2,y2=map(int,input('Enter the 2nd Coordinates : ').split())

print(f'Distance = {math.sqrt((x2-x1)**2+(y2-y1)**2)}')