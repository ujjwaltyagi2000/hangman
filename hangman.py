word_list = {
    "Electronics": ["microwave oven", "washing Machine", "television", "refrigerator", "toaster"],
    "Astronomy": ["constellation", "dark matter", "hubble telescope", "meteor shower", "milky way", "solar system"],
    "Countries": ["soviet union", "argentina", "united kingdom", "brazil", "germany", "france",
    "india", "portugal", "spain", "mexico", "ukraine", "sweden"],
    "Chemical Elements": ["aluminum", "antimony", "beryllium", "bismuth", "chlorine", "chromium", "fluorine", "gallium", "germanium", "hydrogen"],
    "Geography": ["altitude", "antarctic circle", "equator", "longitude", "prime meridian"],
    "Monsters": ["boogeyman", "centaur", "cyclops", "godzilla", "golem", "werewolf", "yeti"],
    }

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''']


def gen_blanks(word):
    # num_blanks=len(word)
    blanks = ""
    for char in word:
        if char == " ":
            blanks += " "
        else:
            blanks += "_ "
    print(blanks)
    return blanks


def print_format_list(display):
    format_list = ""
    for n in display:
        if n == "_":
            format_list += "_ "
        elif n == " ":
            format_list += " "
        else:
            format_list += n+" "
    print(format_list)


# def letter_guess(random_word, display, lives):
#     guess = input("\nGuess a letter: ").lower()
#     position = 0
#     print(lives)
#     for letter in random_word:
#         if letter == guess:
#             display[position] = letter
#             position+=1    
#         if guess not in random_word:
#             lives-=1
#             print(stages[lives])
#             print("\nYou lost a life, be careful")
            
#     print_format_list(display)  
#     return lives