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

checklist=[]
for letter in random_word:
    if letter==" ":
        checklist+=" "
    else:
        checklist+=letter

victory=False

while victory!=True:
    hangman.letter_guess(random_word,display)
    if display==checklist:
        print("You win")
        break






# right_guess=0
# wrong_guess=0


