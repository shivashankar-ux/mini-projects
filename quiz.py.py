print("Welcome to the quiz")

player = input("Do you like to play? ")

if player.lower() != "yes":
    quit()
    
score = 0

answer = input("who is the president of india? ")
if answer.lower() == "droupadi murmu":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("who is the prime minister of india? ")
if answer.lower() == "narendra modi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("who is the cheif minister of Telangana? ")
if answer.lower() == "kcr":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("who is the IT minister of Telangana? ")
if answer.lower() == "ktr":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("who is the Home minister of Telangana? ")
if answer.lower() == "mahmood ali":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("Your score is :" + str(score))

    

