#Joey Rudolph
#10/4/2021
#This program prompts the user to enter a text file
#After the user enters the text file, the program gives the user options for what operations they want to perform on their text file.
#Option A calculates the average word length of the text.
#Option B takes in user input input which prompts the user to enter a letter. The program will then calculate how many words in the file start with that letter.
#Option C calculates the average number of punctuation marks per line in the file
#A text file you can enter is United States Constitution.txt
#Another text file you can enter is United States Declaration of Independence.txt


def project():

    #print program introduction
    
    #get name of file

    #the lines below until line 34 explain the program to the user
    print("This program prompts the user to enter a text file and gives users 3 different options for info they would like to find out about the text.") 
    print()
    print("The user will be able to:")
    print()
    print("1. calculate the average word length of the text,")
    print()
    print("2. input a letter of his choice and determine the number of words starting with that letter,")
    print()
    print("3. calculate the number of punctution marks per line in the text.")
    print()
    print("After the user enters the file, the program lists and describes the different options for the user to choose regarding what they want to find out about the text")
    print()
    print()
    print("If you wish, you can test a file of your own choosing and then make sure it is in the file name.txt format and that it is in the Programming Assignment 2 folder. ") 
    print("If not, 2 text files have been added for your convenience: (United States Constitution.txt or United States Declaration of Independence.txt)")
    print()

    
    user_input = input("Enter your file name with .txt and press return: ") #Prompts the user to enter a text file
    file = open(user_input) 
    readfile = file.read() 
    print()
    #The 3 lines below explain the options to the user
    print("For option a: The program will calculate the average word length of the text")
    print("For option b: The program will take in user input which prompts the user to enter a letter. The program will then calculate how many words in the file start with the letter the user inputted")
    print("For option c: The program will calculates the number of punctution marks per line in the text")
    print()
    user_choice = input("Enter a letter either a, b, or c (corresponsing to the options): ") #Takes in user input
    print()
    print()
    
    if user_choice == 'a': #Condition 1
        letter_count = 0 #Initiates accumulator variable
        words_in_text = readfile.split() #Splits the contents of the file into words
        word_count = len(words_in_text) #Defines word_count as the length of each word in the file

        for word in words_in_text: #Loops over each word in the text
            for letter in word: #Loops over each letter in a word
                letter_count += len(letter) #Updates accumulator variable letter_count by counting letters in a word
        average_word_length = letter_count/word_count #Calculates the average word length of words in the file
        print("The average word length of the file is", round(average_word_length, 5), "letters") #rounding word length to 5 decimal places       
                 

         
    elif user_choice == 'b': #Condition 2
        count = 0 #Initiates accumulator variable 
        user_input_letter = input("Please enter a letter : ") #Takes in user input
        word_in_text = readfile.split() #Splits the contents of the file into words

        for letter in word_in_text: #Loops over each word in the text
            if letter[0].lower() == user_input_letter or letter[0].upper() == user_input_letter.upper(): #This condition makes it not case sensitive while finding words
                count = count + 1 #Updates accumulator variable count to count number of words that start with the letter the user inputted 
        print(count, "words in the text start(s) with the letter", user_input_letter)
        



    elif user_choice == 'c': #Condition 3
        line_count = 0 #Initiates accumulator variable
        punctuation_count = 0 #Initiates accumulator variable
        lines_in_text = readfile.split("\n") #Splits the string into lines
        list_of_punctuation = [".", ",", "!", "?", "-", ":", ";", "/", " ' "] #A list of punctuation marks

        for line in lines_in_text: #Loops over each line in the text
            line_count = line_count + 1 #Updates accumulator variable line_count to count the total number of lines in the text
            for character in line: #Loops over each character in the line
                if character in list_of_punctuation: #Checks to see if there are punctuation marks in each line
                    punctuation_count = punctuation_count + 1 #Updates accumulator variable to count number of punctuation marks
                    
        #The line below calculates the average number of punctuation marks per line by dividing the number of punctuations marks by the total number of lines in the text
        average_number_of_punctuation_marks_per_line = punctuation_count / line_count   
        print("The average number of punctuation marks per line is", round(average_number_of_punctuation_marks_per_line, 5), "marks") #rounding number of punctuation marks to 5 decimal places   

        

    else: #Condition for incorrect input from user
        print("You incorrectly entered a letter other than a, b, or c")
        print("Please re enter your file name with .txt (ie United States Constitution.txt or United States Declaration of Independence.txt) at the next user input")
        print()
        project() #Calls the function again if user enters incorrect input
        
        

    file.close() #Closes the file


        
            
project() #Calls the function
