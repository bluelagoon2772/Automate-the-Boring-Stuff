# Write your code here :-)
list=[]
def comma():
    for index, item in enumerate(list):
        if index<int(len(list))-2:
            print(item+', ',end='')
        elif index<int(len(list))-1:
            print(item+' ',end='')
        else:
            print('and '+item+'!')
input_string=input("Please list your favorite fruits. Simply separate each fruilt by a comma:")
list=input_string.split(',')
comma()
