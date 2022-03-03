"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_optimal_predict(number: int = 1) -> int:
    """Сначала устанавливаем любое random число от 1 до 100, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min_num = 1
    count = 0
    max_num = 101
    predict = np.random.randint(1, 101) # предполагаемое число
    
    while number != predict:  
        count += 1
        predict = np.random.randint(min_num, max_num) # уменьшаем множество чисел для ускорения поиска
        
        if number < predict:
            max_num = predict
                       
        elif number > predict:
            min_num = predict 
               
    return count

def score_game(game_optimal_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывается наш алгоритм

    Args:
        game_optimal_predict ([type]): функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls=[] # список для сохраниения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array=np.random.randint(1,101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(game_optimal_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return(score)


# RUN
if __name__ == '__main__':
    score_game(game_optimal_predict)
