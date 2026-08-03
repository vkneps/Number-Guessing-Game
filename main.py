from random import randint

def is_valid(n, limit):
    return n.isdigit() and 1 <= int(n) <= limit

def play_single_game():
    lim = int(input('Введите границу угадывания: '))
    num = randint(1, lim)
    repeats = 0

    while True:
        guess = input(f'Введите число от 1 до {lim}: ')

        if is_valid(guess, lim):
            guess = int(guess)
            repeats += 1
        else:
            print(f'А может быть все-таки введем целое число от 1 до {lim}?')
            continue

        if guess == num:
            print('Вы угадали, поздравляем!')
            print(f'На это вам потребовалось {repeats} попыток')
            break
        elif guess > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')

def main():
    print('Добро пожаловать в числовую угадайку')

    while True:
        play_single_game()

        new_game = input('Хотите еще сыграть? Ответьте да/нет: ')
        if new_game != 'да':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

main()