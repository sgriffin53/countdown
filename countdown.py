import random
import sys

def isMatch(tomatch,word):
    matched = ""
    for letter in word:
        pos = tomatch.lower().find(letter.lower())
        if (pos != -1):
            tomatch = tomatch[:pos] + tomatch[(pos+1):]
            matched += letter.lower()
    if matched.lower() == word.lower(): return True
    return False

def findAIword(letters,minlen,maxlen):
    file = "words.txt"
    F = open(file,"r")
    readlines = F.readlines()
    for word in readlines:
        word = word.splitlines()[0]
        if isMatch(letters,word):
            if len(word) >= minlen and len(word) <= maxlen:
                return word
    return None

def trimDict():
    file = "dict.txt"
    newfile = "words.txt"
    F = open(file,"r")
    F2 = open(newfile,"w")
    words = F.readlines()
    newwords = []
    for word in words:
        newword = word[0:(len(word) - 1)]
        if isallowed(newword):
            newwords += newword
            F2.write(newword + "\n")
    F.close()
    F2.close()
    #print(words[3])

def isallowed(word):
    for letter in word:
        if (letter != None) and (ord(letter) < 97 or ord(letter) > 122):
            return False
    return True

def mainMenu():
    print("Countdown")
    print("---")
    print("1. New game.")
    print("2. How to play.")
    print("3. Exit.")
    choice = input("Enter choice:")
    if choice == "1":
        newGame()
    if choice == "2":
        print("---")
        print("Countdown is a game where players try to get the highest scoring word out of a selection of 9 letters.")
        print("Play against the AI and try to score the most points.")
        print("---")
        input("Press any key to return to the menu.")
        mainMenu()
    if choice == "3":
        print("Thanks for playing.")
        sys.exit()

def newGame():
    round = 0
    difficulty = None
    playerscore = 0
    AIscore = 0
    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "master":
        difficulty = input("Select difficulty (Easy, Medium, Hard, Master):").lower()
    numrounds = int(input("Select number of rounds (recommended: 5):"))
    while (round<numrounds):
        round+=1
        result = startround(round, difficulty)
        wordlen = result[1]
        winner = result[0]
        if winner == "Tie":
            playerscore += wordlen
            AIscore += wordlen
        if winner == "AI":
            AIscore += wordlen
        if winner == "Player":
            playerscore += wordlen
        print("---")
        print("Current Score")
        print("---")
        print("Player:",playerscore)
        print("AI:",AIscore)
        if round != numrounds: input("Press any key for next round")
        print("")
    if AIscore > playerscore: print("AI wins with", AIscore,"points.")
    if AIscore == playerscore: print("It's a tie with both players scoring,",AIscore,"points.")
    if AIscore < playerscore: print("Player wins with",playerscore,"points.")
    print("")
    print("Thanks for playing!")

def startround(round, difficulty):
    print("Starting round", round)
    letters = randletters()
    print("Letters:", letters)
    print("AI is thinking")
    AIword = getAIword(difficulty, letters)
    print("AI has chosen a word.")
    playerWord = input("Choose your word: ")
    allowed = False
    F = open("words.txt","r")
    readlines = F.readlines()
    for word in readlines:
        word = word.splitlines()[0]
        if word == playerWord:
            allowed = True
            break
    if isMatch(letters, playerWord) == False:
        print("Your word uses letters that are not available.")
        allowed = False
    if not allowed: print("Your word is not allowed. You score 0 points.")
    if allowed: print("Your word is valid.")
    print("AI chose the word",AIword)
    if not allowed:
        print ("AI scores", len(AIword),"points.")
        return("AI",len(AIword))
    if allowed:
        if len(AIword) == len(playerWord):
            print("You both score", len(AIword),"points.")
            return("Tie",len(AIword))
        elif len(AIword) > len(playerWord):
            print("AI scores", len(AIword),"points.")
            return("AI",len(AIword))
        elif len(playerWord) > len(AIword):
            print("Player scores", len(playerWord),"points.")
            return("Player",len(playerWord))






def randletters():
    letterbin = ['A','A','A','A','A','A','A','A','A',
                 'B','B',
                 'C','C',
                 'D','D',
                 'E','E','E','E','E','E','E','E','E','E','E','E',
                 'F','F',
                 'G','G','G',
                 'H','H',
                 'I','I','I','I','I','I','I','I','I',
                 'J',
                 'K',
                 'L','L','L','L',
                 'M','M',
                 'N','N','N','N','N','N',
                 'O','O','O','O','O','O','O','O',
                 'P','P',
                 'Q',
                 'R','R','R','R','R','R',
                 'S','S','S','S',
                 'T','T','T','T','T','T',
                 'U','U','U','U',
                 'V','V',
                 'W','W',
                 'X',
                 'Y','Y',
                 'Z']
    letters = ""
    while len(letters) < 9:
        randnum = random.randint(0,len(letterbin) - 1)
        letter = letterbin[randnum]
        letters += letter.upper()
    return letters





def getAIword(difficulty,letters):
    if difficulty.lower() == "easy":
        AIminlen = 3
        AImaxlen = 6
    if difficulty.lower() == "medium":
        AIminlen = 5
        AImaxlen = 8
    if difficulty.lower() == "hard":
        AIminlen = 7
        AImaxlen = 9
    if difficulty.lower() == "master":
        AIminlen = 9
        AImaxlen = 9
    foundword = False
    wordlen = random.randint(AIminlen,AImaxlen)
    word = None
    while word == None and wordlen > 0:
        word = findAIword(letters,wordlen,wordlen)
        wordlen = wordlen - 1
    return word

mainMenu()
