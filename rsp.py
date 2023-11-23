import random


def get_user_choice():
    user_choice = input("Выберите камень (k), ножницы (н) или бумагу (б): ")
    while user_choice not in ['к', 'н', 'б']:
        user_choice = input("Введите к, н или б: ")
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(['к', 'н', 'б'])
    return computer_choice

def get_winner(user_choice, computer_choice):

    if user_choice == computer_choice:
        return "Ничья"
    elif user_choice == 'к' and computer_choice == 'н':
        return "Вы выиграли раунд!"
    elif user_choice == 'н' and computer_choice == 'б':
        return "Вы выиграли раунд!"
    elif user_choice == 'б' and computer_choice == 'к':
        return "Вы выиграли раунд!"
    else:
        return "Компьютер выиграл раунд"
        

def play_game():
    print("Добро пожаловать в игру 'камень, ножницы, бумага'!")
    score = 0
    cscore = 0
    rounds_played = 0
    while score != 3 or cscore != 3:
        rounds_played += 1
        print(f"Раунд {rounds_played}:")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Ваш выбор: {user_choice}")
        print(f"Выбор компьютера: {computer_choice}")
        print(get_winner(user_choice, computer_choice))

        if get_winner(user_choice, computer_choice) == "Вы выиграли раунд!":
            score +=1
        if get_winner(user_choice, computer_choice) == "Компьютер выиграл раунд":
            cscore +=1
        print(f'Счёт {score}:{cscore}')
        if score == 3:
            print("Вы выиграли серию игр!")
            score = 0
            cscore = 0
            rounds_played = 0
            play_again = input("Хотите сыграть еще раз? (да/нет) ").lower()
            if play_again != 'да':
                print("Спасибо за игру! До свидания.")
                break
        if cscore == 3:
            print("Компьютер выиграл серию игр!")
            score = 0
            cscore = 0
            rounds_played = 0
            play_again = input("Хотите сыграть еще раз? (да/нет) ").lower()
            if play_again != 'да':
                print("Спасибо за игру! До свидания.")
                break
play_game()