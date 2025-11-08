#Function
print("Hello world")

def PrintMe(myName):
    queenName = myName + " the queen"
    return queenName

finalName = PrintMe(input("whats your name:"))
print(finalName)