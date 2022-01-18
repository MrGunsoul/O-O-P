#Exercise 1
#Nico Kranni

import random,math
#Task 1
print ("Hello")

#Task 2
def numlist(): #Start of function
    emptynum=[] #Empty list
    while len(emptynum)<10:#Min 10 items
        emptynum.append(int(input()))
    else:
        print(emptynum.sort)#After then items prints list of inputs. And we also sort them for task 3
    emptynum=[(random.randrange(0,999))for item in emptynum] #Replaces every element in list with random one between 0 and 999
    print(emptynum.sort) #Sort the list for task 3

def strlist(): #Start of function
    emptystr=[] #Empty list
    while len(emptystr)<10:#Min 10 items
        emptystr.append(str(input()))
    else:
        print(emptystr)#After then items prints list of inputs


#numlist()
#strlist()

#Task 4, 5 and 6
def readint(): #Start of function
    negint=0
    evenint=0
    listsum=[]
    while True:
        try:
            number=int(input("Give a number: "))
        except ValueError:
            print ("Has to be a number")
            continue
        if number == 0:
            print(negint)
            print(evenint)
            Sum=sum(listsum)
            print(Sum)
            break
        if number < 0:
            negint+=1
            continue
        if number % 2==0:
            evenint+=1
            if number > 0 and number % 3 == 0:
                listsum.append(number)
            continue
        if number > 0 and number % 3 == 0:
            listsum.append(number)
            continue

#Task 7
def ariprog():
    terms=0
    termsl=[]
    sumofterms=[]
    sqrofterms=[]
    x=int(input("Give a number: "))
    numbers=range(3, x, 3)
    for i in numbers:
        terms+=1
        termsl.append(i)
        sumofterms.append(i)
        sqrofterms.append((i*i))
    print(termsl)
    print (terms)
    print(sum(sumofterms))
    print(sum(sqrofterms))

#Task 8
def rps():
    items=["Rock", "Paper", "Scissors"] #List where from computer chooses
    cw=0 #Computer wins
    uw=0 #User wins
    while cw<3 and uw<3:
        try:
            user=str(input("Give your choice (Rock, Paper, Scissors): ")) #What does user choose
            computer=random.choice(items) #Computer chooses from list what it plays
            print("Computer's choice is", computer)

        except ValueError:#If not str gives this
            print ("Has to be Rock, Paper or Scissors")
            continue

        if user == computer:
            print(f"It's a tie!")
            print ("Computer", cw, "You", uw, "\n" )

        elif user == "Rock":
            if computer == "Scissors":
                uw+=1
                print("Rock smashes Scissors!") 
                print ("Computer", cw, "You", uw,"\n")

            else:
                cw+=1
                print("Paper covers Rock!")
                print ("Computer", cw, "You", uw,"\n")
                
        elif user == "Paper":
            if computer == "Rock":
                uw+=1
                print("Paper covers Rock!")
                print ("Computer", cw, "You", uw,"\n")

            else:
                cw+=1
                print("Scissors cuts Paper!")
                print ("Computer", cw, "You", uw,"\n")

        elif user == "Scissors":
            if computer == "Paper":
                uw+=1
                print("Scissors cuts Paper!")
                print ("Computer", cw, "You", uw,"\n")

            else:
                cw+=1
                print("Rock smashes Scissors!")
                print ("Computer", cw, "You", uw,"\n")

        else:
            print ("Input has to be Rock, Paper or Scissors") #If input is wrong

    if cw>uw:
        print ("You lost!")
    else:
        print("You won!")