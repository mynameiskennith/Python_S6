# An exception is an event which occurs during the excution of a program 's instruction.
# When a Python script encounters a situation that it cannot cope with, it raises an exception.
# When a python script raises an exception immedeately otherwise it terminates and quits.

def divide(x,y):
    try:
        result = x//y
        print('No probs ..')
    except ZeroDivisionError:
        print('Sorry ! You are dividing by zero')
    else:
        print('This is else block')
    # print('this is sommething')
    finally:
        print('This is finally block')

divide(2,0)