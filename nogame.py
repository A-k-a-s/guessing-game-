import random
print("welcome to guessing game\n")
count=1
num=random.randint(1,100)
while count<=7:
    guess = int(input("guess the no\n"))
    if guess<num:
        print("you have guessed a lower number!!please choose a bigger number\n")
        print("you have left",{7-count},"choices to guess\n")
    if guess>num:
        print("you have guessed a higher number!!please choose a smaller number\n")
        print("you have left",{7-count},"choices to guess\n")
    if guess==num:
        print("horray!!!!",num,"\n")
        print("you took",{count},"chances to guess the correct number\n")
        break
    count=count+1
else:
    print("oops you run out of chances!!")
    print("the chosen number was",num)
