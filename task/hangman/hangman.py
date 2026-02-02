import random

WORDS = ["python", "java", "swift", "javascript"]

def menu():

    wins = 0
    losses = 0

    print("H A N G M A N")

    while True:

        action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')

        if action == "play":
            result = play_game()

            if result == "win":
                wins += 1

            else:
                losses += 1

        elif action == "results":
            score(wins, losses)

        elif action == "exit":
            break

        else:
            continue

def score(win_counter, lose_counter):
    print(f"You won: {win_counter} times")
    print(f"You lost: {lose_counter} times")


def play_game():

    word_pairs = []

    for word in WORDS:
        length = len(word)
        hint_word = length * "-"
        word_pairs.append((word, hint_word))

    chosen_word, chosen_hint = random.choice(word_pairs)
    chosen_hint_list = list(chosen_hint)

    letters = set(chosen_word)

    correctly_chosen = []
    chosen = []

    attempts = 8

    while attempts > 0:
        print(chosen_hint)
        answer = input("Input a letter: ")

        if not len(answer) == 1:
            print("Please, input a single letter.")

        elif not (answer.isalpha() and answer.islower()):
            print("Please, enter a lowercase letter from the English alphabet.")

        elif answer in chosen:
            print("You've already guessed this letter.")

        else:

            chosen.append(answer)

            if answer in letters:

                if answer not in correctly_chosen:

                    correctly_chosen.append(answer)

                else:

                    attempts -= 1

                    print("No improvements.")

                    if attempts == 0:
                        print("\nYou lost!")

                        return "lose"

                positions = []

                start = 0

                while start < len(chosen_word):
                    position = chosen_word.find(answer, start)

                    if position == -1:
                        break

                    else:
                        positions.append(position)
                        start = position + 1

                for element in positions:

                    chosen_hint_list[element] = answer
                    chosen_hint = "".join(chosen_hint_list)

                if chosen_hint == chosen_word:

                    print(f"You guessed the word {chosen_word}!")
                    print("You survived!")

                    return "win"

            else:
                attempts -= 1

                print("That letter doesn't appear in the word!")

                if attempts == 0:
                    print("You lost!")

                    return "lose"

if __name__ == "__main__":
    menu()











