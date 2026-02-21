secret_word = ("penguin")
guess = ""
guess_count = 0
guess_limit = 4
out_of_guess = False
while guess != secret_word and guess_count < guess_limit:
    guess = input("enter the word:").strip()
    guess_count += 1
if guess == secret_word:
    print("you won")
else:
    print(f"Wrong! {guess_limit - guess_count} guesses left.")

if guess != secret_word:
    out_of_guess = True
    print("Out of guesses! Game over.")


    
