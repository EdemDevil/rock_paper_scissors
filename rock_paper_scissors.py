"""Импортируем необходимые модули"""
import random as r
import sys

"""Обявляем переменные, в них помещаем эмоджи"""
scissors = "✌"
paper = "✋"
rock = "✊"

"""Формируем список, для облегчения доступа к переменным"""
hand_gesture = [scissors, paper, rock]

"""Формируем список с численными значениями переменных, для возможности далльнейшего сравнения"""
number_hand_gesture = [ord(scissors), ord(paper), ord(rock)]

"""Находим длину списка"""
length = len(hand_gesture) - 1

"""Принимаем информацию о выборе от пользователя"""
human_choiсe = input("Choose your gesture(1-scissors, 2-paper, 3-rock)):  ")

"""Формируем случайный выбор жеста компьютером, диапозон от нуля до последнего элемента списка"""
computer_choise = hand_gesture[r.randint(0, length)]

"""Условие для выбора пользователя"""
if human_choiсe == "1":
    """Выводим информацию о выборе пользователя и компьютера"""
    print(f"{hand_gesture[0]}\nComputer choise:\n{computer_choise}")
    """Сравнение выбора для определения статуса игры"""
    if ord(computer_choise) == number_hand_gesture[0]:
        print("DRAW")
    elif number_hand_gesture[2] < ord(computer_choise) < number_hand_gesture[0]:
        print("YOU WIN")
    else:
        print("YOU LOSE")

if human_choiсe == "2":
    print(f"{hand_gesture[1]}\nComputer choise:\n{computer_choise}")
    if ord(computer_choise) == number_hand_gesture[1]:
        print("DRAW")
    elif ord(computer_choise) > number_hand_gesture[1]:
        print("YOU LOSE")
    else:
        print("YOU WIN")

if human_choiсe == "3":
    print(f"{hand_gesture[2]}\nComputer choise:\n{computer_choise}")
    if ord(computer_choise) == number_hand_gesture[2]:
        print("DRAW")
    elif number_hand_gesture[0] > ord(computer_choise) > number_hand_gesture[2]:
        print("YOU LOSE")
    else:
        print("YOUWIN")