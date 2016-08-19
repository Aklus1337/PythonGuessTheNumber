import random


def GetRange():
    MinRange=input("What is the miniumum range? ")
    MaxRange=input("What is the maximum range? ")
    while(int(MinRange) >= int(MaxRange)):
        print("You provided the wrong numbers")
        MinRange=input("What is the minimum range? ")
        MaxRange=input("What is the maximum range? ")
    GenerateTheNumber(int(MinRange),int(MaxRange))

def GenerateTheNumber(Min,Max):
    number=random.randrange(Min,Max)
    StartGuessing(number)

def StartGuessing(number):
    NumberOfTries = 0
    answer = 0
    while(number!=answer):
        answer = input("What is your answer? ")
        answer = int(answer)
        NumberOfTries = NumberOfTries +1
        if(answer<number):
            print("Answer is too low!")
        elif(answer>number): #else is doubling the tip
            print("Answer is too high!")
    print("You did it! You needed "+str(NumberOfTries)+" tries. The number was " +str(number))

GetRange()