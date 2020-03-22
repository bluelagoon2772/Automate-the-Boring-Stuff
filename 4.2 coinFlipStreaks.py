import random

numberofStreaks=0
#Create list of heads and tails
for experimentNumber in range(10000):
    list=[]
    for i in range(0,100):
        list.append(random.randint(0,1))
        if list[i]==0:
            list[i]='h'
        else:
            list[i]='t'

    #Check for 6 heads or tails in a row
    x=0
    while x<int(len(list)-5):
        if list[(x)]==list[(x+1)]==list[x+2]==list[x+3]==list[x+4]==list[x+5]:
            numberofStreaks=numberofStreaks+1
            x=x+6
        else:
            x=x+1


print('Chance of streak: %s%%' % (numberofStreaks / 10000))
 
