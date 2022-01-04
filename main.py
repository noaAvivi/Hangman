def main():
    MAX_TRIES = 7
    level = 0
    old_letters_guessed = []
    flag = "YOU LOSE"
    HANGMAN_PHOTOS = {"0": "x-------x",
                      "1": """
    x-------x
    |
    |
    |
    |
    | 
        """,
                      "2": """
    x-------x
    |       |
    |       0
    |
    |
    |
             """,

                      "3": """
    x-------x
    |       |
    |       0
    |       |
    |
    |
             """,
                      "4": """
    x-------x
    |       |
    |       0
    |      /|
    |
    |

    """,
                    "5": """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |

    """,
                      "6": """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |

    """,
                      "7": """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """}
    HANGMAN_ASCII_ART = """Welcome to the game Hangman 


     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/



    """
    words =["shir","king","pineapple","u","noa","teacher","class","disney"]
    print(HANGMAN_ASCII_ART)
    index = int(input("choose a number: "))
    secret_word = choose_word(words, index)
    print(show_hidden_word(secret_word, old_letters_guessed))

    while (level < MAX_TRIES):

        letter_guessed = input("guess a letter :")
        letter_guessed = letter_guessed.lower()
        if (not (letter_guessed in secret_word) and (check_valid_input(letter_guessed, old_letters_guessed)) and not (
                letter_guessed in old_letters_guessed)):
            level += 1
            if level == 1:
                print("you have " + str(level) + " mistake. remember! you have only 7 tries.")
            else:
                print("you already had " + str(level) + " mistakes. remember! you have only 7 tries.")


        if check_valid_input(letter_guessed, old_letters_guessed):
            try_update_letter_guessed(letter_guessed, old_letters_guessed)
            print(print_hangman(level, HANGMAN_PHOTOS))
            print(show_hidden_word(secret_word, old_letters_guessed))

            if check_win(secret_word, old_letters_guessed):
                flag = "YOU WIN!! :)"
                break

        else:
            print("Please enter a valid input")
            print(print_hangman(level, HANGMAN_PHOTOS))
            print(show_hidden_word(secret_word, old_letters_guessed))

        print("\n")

    print(flag)
    ask = input("please enter T/t if you want another game (any other letter get you out of this game): ")
    if ((ask == "T") or (ask == "t")):
        main()
    else:
        print("Bye")


def choose_word(words, index):
    """this function takes the secret word from a array of words
        :words: array, the words the player choose from to guess
        :index: int, a number to choose the word from the file(location)
        :treturn: string
    """
    num_of_words = len(words)
    index = (index % num_of_words)
    the_choosen_word = words[index]
    return (the_choosen_word)


def print_hangman(level, HANGMAN_PHOTOS):
    """this function shows the user his progress with photos      
        :level: int, the level the user is in
        :HANGMAN_PHOTOS: dict, a list of all the stages
        :treturn: string
    """
    return HANGMAN_PHOTOS[str(level)]

def show_hidden_word(secret_word, old_letters_guessed):
    """this function shows the blanks and the letters in the secret word      
        :secret_word: string, the word the user needs to guess
        :old_letters_guessed: list, a list of all old letters the used guessed
        :treturn: string
    """
    blanks = ""
    for letter in secret_word:
        if letter == " ":
            blanks += "  "
        elif letter in old_letters_guessed:
            blanks += letter + " "
        else:
            blanks += "_ "
    return blanks


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """this function checks if the word that the user guessed is already guessed before      
        :letter_guessed: string, the letter the user guessed
        :old_letters_guessed: list, a list of all old letters the used guessed
        :treturn: void
    """

    if (old_letters_guessed.count(letter_guessed) == 0):
        old_letters_guessed.append(letter_guessed)

    else:
        print("Don't you remember the letters you already guessed ?")
        print("the letters you already guessed are :")
        print(*old_letters_guessed, sep='->')


def check_valid_input(letter_guessed, old_letters_guessed):
    """this function checks if the input is valid

        :letter_guessed: string, the letter the user guessed
        :old_letters_guessed: list, a list of all old letters the used guessed
        :treturn: boolean
    """
    if (((len(letter_guessed) != 1)) and (letter_guessed.isalpha())):
        return False

    elif (((letter_guessed >= 'a') and (letter_guessed <= 'z')) == False):
        return False

    elif ((((letter_guessed >= 'a') and (letter_guessed <= 'z'))) and (not (letter_guessed.isalpha()))):
        return False

    else:
        return True


def check_win(secret_word, old_letters_guessed):
    """this function checks if the user wins or not
        :secret_word: string, the word that the user needs to guess
        :old_letters_guessed: list, a list of all old letters the used guessed
        :treturn: boolean
    """
    secret_word_len = len(secret_word)
    temp = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            temp += 1

    if (temp == secret_word_len):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
