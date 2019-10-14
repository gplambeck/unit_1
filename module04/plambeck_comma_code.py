# A function that takes a list value as an argument and returns a string with
# all the items separated by a comma and a space, with 'and' inserted before
# the last item.

def commaCode(listValue):
    for i in range(len(listValue) - 1):
        print(listValue[i], end=', ') # 'end' disables new line after print()
    print('and ' + listValue[-1])
