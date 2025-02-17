import random
# random is a built in libaray in python that gives us access to a lot 
# of random oprtations

words = ['apple', 'python', 'java', 'ruby', 'swift']
# choice is to pick a random choice form a list
chosen_word = random.choice(words)
word_display = ['-' for _ in chosen_word] # this creats a - for every character in the word
print(word_display)
attempts = 8

print("Welcome to Hangman Game")

while attempts > 0 and '-' in word_display:
    print("\n" + ''.join(word_display))
    userInput = input("Enter a letter to guess the word!:").lower()
    if userInput in chosen_word:
        for index, letter in enumerate(chosen_word):
             if letter == userInput:
                 word_display[index] = userInput
    else:
        attempts -= 1
        #same as
        # for i in range(len(chosen_word)):
          #  if chosen_word[i] == userInput:
          #      word_display[i] = userInput
         #   else:
          #      attempts -= 1
        
if '-' not in word_display:
    print(f"Congrate! You guessed the word {chosen_word} and won the game!")
else:
    print(f"You lost the game! The work was: {chosen_word}")