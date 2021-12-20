import random
import hangman

print("\nHello and Welcome to the Hangman Game!")
category=random.choice(list(hangman.word_list))
print(f"\nThe word below belongs to \"{category}\" category:\n")
random_word=random.choice(hangman.word_list[category])

hangman.gen_blanks(random_word)

word_lenth=len(random_word)

display=[]
for letter in random_word:
    if letter==" ":
        display+=" "
    else:
        display+="_"

game_over=False
lives=7

while game_over!=True:
#     # lives=hangman.letter_guess(random_word,display,max_life)
    guess = input("\nGuess a letter: ").lower()
    position = 0
    for letter in random_word:
        if letter == guess:
            display[position] = letter
        position+=1    
    if guess not in random_word:
        lives-=1
        print(hangman.stages[lives])
        print("\nYou lost a life, be careful")
            
    hangman.print_format_list(display)

    if "_" not in display:
        print("You Won!")
        game_over=True
    if lives==0:
        print(f"\nYou Lost :( \nThe word was \"{random_word}\"")
        game_over=True
