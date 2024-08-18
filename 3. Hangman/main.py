import random
words = [
    'python', 'javascript', 'kotlin', 'ruby', 'swift', 'algorithm', 'compiler', 'database', 'encryption',
    'firewall', 'hardware', 'internet', 'java', 'kernel', 'malware', 'network', 'object', 'protocaol',
    'query', 'router', 'security', 'token', 'url', 'virtual', 'wireless', 'xml', 'yaml', 'zip', 'abstract',
    'binary', 'cache', 'developer', 'ethernet', 'framework', 'gateway', 'hexadecimal', 'iteration', 'juxtapose',
    'keystroke', 'lambda', 'metadata', 'node']

hangman_stages = ["""
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""", '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
       |
       |
       |
      ===''',]

# Choose a Random word from the list
chosen_word = random.choice(words)
print(chosen_word)

word_display = ['_' for _ in chosen_word]

# Maximum number of guesses allowed
attempts = 6

print("Welcome to Hangman!")

# Display the current state of the word and the hangman
def display_state():
    print(f"attempts = {attempts}")
    print(hangman_stages[attempts])
    print(' '.join(word_display))

def display_word():
    print(' '.join(word_display))

while attempts > 0 and '_' in word_display:
    display_state()
    guess = input('Guess a letter: ').lower()

    # Check if the guessed letter is in word
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                if word_display[index] == '_':
                    word_display[index] = guess
    else:
        print("Incorrect! Try again.")
        attempts -= 1
    
    #check Win condition
    if '_' not in word_display:
        display_state()
        print("Congratulation! You Won!")
        break

if attempts == 0:
    display_state()
    print("Sorry! You lost. The word was: ", chosen_word)

display_word()