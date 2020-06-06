from random_word import pick_random_word


def print_current_state(current_word, attempts_remaining):
    print("Current word state : ", end=" ")
    for i in current_word:
        print(i, end=" ")

    print("\t Attempts Remaining:", attempts_remaining)


def change_current_word(selected_word, current_word, input_char):
    modified_word = ""
    for i in range(len(selected_word)):
        if current_word[i] == "_" and selected_word[i] == input_char:
            modified_word += selected_word[i]
        else:
            modified_word += current_word[i]
    return modified_word


def check_in_word(selected_word, current_word, attempts_remaining, input_char):
    if input_char in selected_word:
        current_word = change_current_word(selected_word, current_word, input_char)
    else:
        attempts_remaining -= 1
    return current_word, attempts_remaining


def check_the_game(selected_word, current_word, attempts_remaining):
    if attempts_remaining <= 0:
        print("Sorry, you lost the game!!!!!!")
        print("The Word was :", selected_word)
        return False
    elif current_word == selected_word:
        print("Hurray!!!! WINNER WINNER CHICKEN DINNER!!!")
        return False
    return True


def run_game(attempts=5):
    selected_word = pick_random_word()
    current_word = ""
    for i in selected_word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            current_word += i
        else:
            current_word += "_"
    attempts_remaining = attempts
    print_current_state(current_word, attempts_remaining)
    while True:
        input_char = input("Guess a character: ")
        current_word, attempts_remaining = check_in_word(selected_word, current_word, attempts_remaining, input_char)
        print_current_state(current_word, attempts_remaining)
        check = check_the_game(selected_word, current_word, attempts_remaining)
        if not check:
            break

run_game()
