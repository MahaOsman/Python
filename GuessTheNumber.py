from operator import truediv


print("Hello to the Guess the Number Game , Please choose a number between 0 - 100 ")
low = 0
high = 100
medium = (low+high)//2
guess = True
while guess == True:
    ans = input(
        f"Is your number : {medium} if Yes: enter y , if too high enter : h ,if too low enter l")
    if(ans == 'y'):
        print(f"Your number is : {medium}")
        guess == False
        break
    elif(ans == 'h'):
        high = medium
        medium = (low+high)//2
    elif(ans == 'l'):
        low = medium
        medium = (low+high)//2
    else:
        print("Sorry I couldn't guess the Number")
        break
