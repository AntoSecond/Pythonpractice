import random

def CreateBull():
    print("Creating new Bullrun")
    return random.randint(1000,9999)

def CompareBulls(input, bulls):
    bulls = str(bulls)
    input = str(input)
    Bullcount = 0
    Cowcount = 0
    x= 0
    while x < len(bulls):
        if bulls[x] == input[x]:
            Bullcount += 1
        else:
            Cowcount += 1
        x += 1
    return ("{0} bulls, {1} cows".format(Bullcount, Cowcount))

if __name__ == "__main__":
    bulls = CreateBull()
    guess= 0
    Guesses =0
    while guess != bulls:
        guess =int(input("Guess the Bullrun number"))
        print(CompareBulls(guess, bulls))
        print(bulls)
        print(guess)
        Guesses+=1
    print("game over, you spent {0} guesses".format (Guesses))