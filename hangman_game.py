import random
import hangman_stages

with open("English_wordsfile.txt", "r") as file:
    word_list = file.read().splitlines()

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

print(" ".join(display))

while not end_of_game:
    guess = input("Guess a letter: ").lower()

   
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!!")


    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_stages.stages[lives])