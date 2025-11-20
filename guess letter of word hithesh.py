def hangman():
    
    hangmans = [
        """
        ------
        |    |
        |
        |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        --------
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        --------
        """
    ]


    name = input("What is your name? ")
    print("Good Luck!", name)
    import random


    words = ['Amrita', 'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'reverse', 'water', 'board', 'geeks']
    word = random.choice(words)


    b = len(word)
    print(f"The word has {b} characters.")
    l = ['_'] * b 
    l2 = list(word)  
    maxg = len(hangmans) - 1  
    wrong = 0
    curstage = 0


    while wrong != maxg:
        print(hangmans[curstage])  
        print("Guess the character:", ' '.join(l)) 
        charguess = input("Enter a character: ").lower()

        if charguess in word:
            print("Correct guess!\n")
            for i in range(len(word)):
                if word[i] == charguess:
                    l[i] = charguess
        else:
            print("Wrong guess!\n")
            curstage += 1
            wrong += 1
            print(f"You have {maxg - wrong} attempts left.")
        
        if "_" not in l:
            print("Congrats! You guessed the word:", word)
            break

    if wrong == maxg:
        print(hangmans[curstage])
        print("You have run out of guesses.")
        print(f"The word was: {word}")
hangman()

    