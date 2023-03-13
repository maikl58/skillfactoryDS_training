"""Игра угадай число.
Компьютер сам загадывает и угадывает число
"""

import numpy as np


def game_core(number: int = 1) -> int:
    """Угадываем чмсло
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # начальное число попыток       
    range_f = (1, 101) # диапазон возможных загаданных чисел из условия задачи
    predict_number = int(sum(range_f)/2) # первое возможное загаданное число
    
    def range_search(range_ff, number, predict_number_f):
        """определяем диапазон поиска учитывая информацию о том, 
           больше ли случайное число или меньше нужного нам.
        Args:
            range_ff (tuple): диапазон возможных загаданных чисел
            number (int): Загаданное число
            predict_number_f (int): возможное загаданное число

        Returns:
            tuple : уменьшенный диапазон
        """
                
        if range_ff[0] <= number < predict_number_f:
            range_ff = (range_ff[0], predict_number_f) #заг. число входит в 1-ую половину диапазона
        else:
            range_ff = (predict_number_f, range_ff[1]) #заг. число входит в 2-ую половину диапазона
        return range_ff
    
    while True: # поиск загаданного числа
        count += 1
        if predict_number == number:
            break # выход если угадали
        else:
            range_f = range_search(range_f, number, predict_number)
            predict_number = int(sum(range_f)/2) # следующее загаданное число
        
    return count




def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))# находим среднее количество попыток
    return score

if __name__ == '__main__':
    score = score_game(game_core)
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
 
    
    