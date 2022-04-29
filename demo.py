def countWordsFromFile():
    file_name = input("Enter File Name: ")
    numberOfWords = 0
    file = open(file_name, "r")
    for i in file:
        words = i.split()
        numberOfWords = numberOfWords + len(words)
    print(numberOfWords)

    
countWordsFromFile()