#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}
from recettes import add_recipes, print_recipe
from os import path
import pickle

# TODO: Importez vos modules ici
def exercice1(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1,  open(file_path2, encoding="utf-8") as f2:
        for line1 in f1:
            line2 = f2.readline()
            if line1 != line2:
                print(line1 + "is not equal to " + line2)
                break
        print("The two files are the same")

def exercice2(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as f1, open(file_path2, encoding="utf-8") as f2:
        file_path2.write(file_path1.read.read().replace(" ", "   "))


def exercice3(file_path1, file_path2):
    with open(file_path1, encoding="utf-8") as file, open(file_path2, encoding="utf-8") as f:
        note_percent = file_path1.read()
    for note in note_percent:
        for key, value in PERCENTAGE_TO_LETTER.items():
            if value[0] <= int(note) < value[1]:
                f.write(note.strp() + "" + key + "\n")

def exercice5(file_path1):
    with open(file_path1, "r") as f:
        word = f.read().strip().split()
        for w in word:
            if w.isnumeric():


# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice1("./exemple.txt", "./exemple2.txt")
    exercice5("./exemple.txt")
    pass
