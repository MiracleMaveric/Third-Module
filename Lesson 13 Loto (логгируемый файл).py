import random
import logging
import os
import datetime

logging.basicConfig(level=logging.DEBUG)

def log(log_name="logs", log_level=logging.DEBUG):

    logger = logging.getLogger(log_name)

    c_handler = logging.FileHandler(f'{log_name}.txt', 'a', 'UTF-8')
    c_handler.setLevel(log_level)

    c_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
    c_handler.setFormatter(c_format)

    logger.addHandler(c_handler)

    def decorator(func):

        def wrapper(*args, **kwargs):
            logger.info("{}: функция {} вызвана из функции play_loto".format(datetime.datetime.now(), func.__name__))
            result = None
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.exception(f'{func.__name__} - ошибка {e}')
            finally:
                return result
        return wrapper
    return decorator

file_name = os.path.splitext(os.path.basename(__file__))[0]

@log(file_name)
def get_card():
    card = [[],[],[]]
    G = False
    while not G:
        for i in range(5):
            i = random.randint(1, 91)
            card[0].append(i)
            if card[0].count(i) >= 2:
                None
            else:
                G = True
    B = False
    while not B:
        for i in range(5):
            i = random.randint(1, 91)
            card[1].append(i)
            if card[1].count(i) >= 2:
                None
            else:
                B = True
    T = False
    while not T:
        for i in range(5):
            i = random.randint(1, 91)
            card[2].append(i)
            if card[2].count(i) >= 2:
                None
            else:
                T = True
    card[0].sort()
    card[1].sort()
    card[2].sort()
    for b in range(4):
        card[0].insert(random.randint(0, 6), "-")
        card[1].insert(random.randint(0, 6), "-")
        card[2].insert(random.randint(0, 6), "-")
    return card

@log(file_name)
def check_victory(x):
    for i in x[0].copy():
        if i == '-':
            x[0].remove(i)
    if len(x[0]) == 0:
        for i in x[1].copy():
            if i == '-':
                x[1].remove(i)
        if len(x[1]) == 0:
            for i in x[2].copy():
                if i == '-':
                    x[2].remove(i)
            if len(x[2]) == 0:
                return True
            else: 
                return False
        else:
            return False
    else: 
        return False

@log(file_name)
def play_loto():
    player = get_card()
    computer = get_card()
    def c1():
        print("Ваша карточка: {}".format(player))
    def c2():
        print("Карточка противника: {}".format(computer))
    c1()
    c2()
    used_bbl = []

    def reroll_bag():
        rule = False
        while not rule:
            bbl = random.randint(1, 90)
            if bbl in used_bbl:
                None
            else:
                print("Номер боченка: {}".format(bbl))
                used_bbl.append(bbl)
                return bbl
                rule = True
    
    game = False
    while not game:
        L = reroll_bag()
        c1()
        turn = float(input("Ваш ход: '1' - зачеркнуть, '2' - продолжить "))
        if turn == 1:
            if L in player[0].copy():
                player[0].remove(L)
            else:
                if L in player[1].copy():
                    player[1].remove(L)
                else:
                    if L in player[2].copy():
                        player[2].remove(L)
                    else:
                        print("Game Over")
                        game = True
        elif turn == 2:
            if L in player[0].copy():
                print("Game Over")
                game = True
            else:
                if L in player[1].copy():
                    print("Game Over")
                    game = True
                else:
                    if L in player[2].copy():
                        print("Game Over")
                        game = True
                    else:
                        None
        if game == False:
            c1()
            print("Ход противника...")
            for i in computer[0].copy():
                if L in computer[0].copy():
                    computer[0].remove(L)
            for i in computer[1].copy():
                if L in computer[1].copy():
                    computer[1].remove(L)
            for i in computer[2].copy():
                if L in computer[2].copy():
                    computer[2].remove(L)
            c2()
            w1 = check_victory(player)
            if w1 == True:
                print("Ты выиграл!")
                game = True
            w2 = check_victory(computer)
            if w2 == True:
                print("ИИ одержал победу")
                game = True

play_loto()