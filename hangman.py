import random

words = ["Python", "Java", "C++", "Ruby", "Perl", "PHP", "JavaScript", "HTML", "CSS", "SQL", "Swift", "Objective-C", "C", "C#", "R"]
print("Welcome to Hangman!")

def mode():
    tries = 6
    word = random.choice(words).lower()
    word_length = len(word)
    display = ["_"] * word_length

    while tries != 0:
        print(" ".join(display))
        guess = input("\nEnter your guess: ").lower()

        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
        else:
            tries -= 1
            print(f"Incorrect guess. You have {tries} tries left.")

        if "_" not in display:
            print("Congratulations! You've guessed the word:", word)
            break
    else:
        print("Sorry, you've run out of tries. The word was:", word)

if __name__ == "__main__":
    mode()