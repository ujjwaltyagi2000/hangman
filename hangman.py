word_list={
    "Electronics":["microwave oven", "washing Machine","television", "refrigerator", "toaster"],
    "Astronomy":["constellation", "dark matter", "hubble telescope", "meteor shower", "milky way","solar system"],
    "Countries":["soviet union", "argentina", "bosnia and herzegovina", "costa rica", "czech republic","dominican republic",
    "ecuador", "finland"],
    "Chemical Elements": ["aluminum", "antimony", "beryllium", "bismuth", "chlorine", "chromium", "fluorine", "gallium", "germanium", "hydrogen"],
    "Geography": ["altitude", "antarctic circle", "equator", "longitude", "prime meridian"],
    "Monsters": ["boogeyman", "centaur", "cyclops", "godzilla", "golem", "werewolf", "yeti"],
    }
def gen_blanks(word):
    # num_blanks=len(word)
    blanks=""
    for char in word:
        if char==" ":
            blanks+=" "
        else:
            blanks+="_ "
    print(blanks)
    return blanks

def print_format_list(display):
    format_list=""
    for n in display:
        if n=="_":
            format_list+="_ "
        elif n==" ":
            format_list+=" "
        else:
            format_list+=n+" "
    print(format_list)        

def letter_guess(random_word, display):
    guess=input("\nGuess a letter: ").lower()
    
    position=0
    for letter in random_word:
        if letter==guess:    
            display[position]=letter
        # elif letter!=guess:
        #     print("Oh No! You lost a life")
        position+=1    
    print_format_list(display)