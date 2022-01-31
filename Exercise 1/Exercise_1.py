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
        emptynum.sort()#Sort them for task 3
        print("Arranged list: ", *emptynum, sep=",")#After ten items prints list of inputs. 
    emptynum=[(random.randrange(0,999))for item in emptynum] #Replaces every element in list with random one between 0 and 999
    emptynum.sort()
    print(*emptynum, sep=",") #Sort the list for task 3

def strlist(): #Start of function
    emptystr=[] #Empty list
    while len(emptystr)<10:#Min 10 items
        emptystr.append(str(input()))
    else:
        emptystr.sort()
        print("Strings: ", *emptystr,sep=",")#After ten items prints list of inputs



#Task 4, 5 and 6
def readint(): #Start of function
    negint=0 #To hold negative integers
    evenint=0 #To hold even integers
    listsum=[] #To hold numbers and use it for sum.
    while True:
        try:
            number=int(input("Please give an integer: "))
        except ValueError:
            print ("Has to be a number")
            continue
        if number == 0:
            print("Number of negative integers is: ", negint)
            print("Number of even integers is: ", evenint)
            Sum=sum(listsum)
            print("Sum of positive integers divisible by three is: ", Sum)
            break
        if number < 0:
            negint+=1
            if number % 2==0:
                evenint+=1
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
    termsList=[]
    sumofterms=[]
    sqrofterms=[]
    x=0
    try:
        x=int(input("Give maximum value: ")) #Needs user input(int)
        numbers=range(3, x, 3) 
        for i in numbers:
            terms+=1 #Adds 1 for everytime it checks term
            termsList.append(i) #Adds the term
            sumofterms.append(i) #Adds the term to list so it can be summed
            sqrofterms.append((i*i)) #Same as previous bu squared
        print("Procession is: ",*termsList)
        print ("Number of terms is: ", terms)
        print("Sumf of terms is: ",sum(sumofterms)) 
        print("Sum of squared terms is: ", sum(sqrofterms))
    except ValueError:
        print("Input needs to be number")
    





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


#Task 9

def ranint():
    return random.randrange(1,7)

print ("Random number is: ", ranint())