import tkinter as tk
from tkinter import messagebox
import random

# Jautājumu saraksts
questions = [
    {
        "question": "Kuri no šiem ir skaitliskie tipi Python valodā?",
        "options": ["int", "float", "str", "complex"],
        "answers": [0, 1, 3]
    },
    {
        "question": "Kurš no šiem funkcijām var atgriezt kvadrātsakni?",
        "options": ["math.sqrt", "math.pow", "pow", "sqrt"],
        "answers": [0, 1, 2]
    },
    {
        "question": "Kuras no šīm funkcijām ir daļa no math moduļa?",
        "options": ["sin", "exp", "append", "log10"],
        "answers": [0, 1, 3]
    },
    {
        "question": "Kuri no šiem datu tipiem ļauj izvairīties no precizitātes kļūdām?",
        "options": ["Decimal", "float", "Fraction", "int"],
        "answers": [0, 2]
    },
    {
        "question": "Ko atgriež funkcija divmod(10, 3)?",
        "options": ["(3, 1)", "Tuple", "List", "Rests un dalījums"],
        "answers": [0, 1, 3]
    },
    {
        "question": "Kādas darbības veic round funkcija Python valodā?",
        "options": ["Noapaļo", "Samazina precizitāti", "Izdzēš decimāldaļas", "Apgriež uz augšu"],
        "answers": [0, 1]
    },
    {
        "question": "Kurus datu tipus atbalsta fractions modulis?",
        "options": ["int", "Fraction", "float", "str"],
        "answers": [0, 1, 2]
    },
    {
        "question": "Kādi būs rezultāti no funkcijas pow()?",
        "options": ["pow(2, 3) = 8", "pow(4, 0.5) = 2.0", "pow(2, -2) = 0.25", "pow(3, 1) = 1"],
        "answers": [0, 1, 2]
    },
    {
        "question": "Kurām funkcijām ir nepieciešami importēt math moduli?",
        "options": ["log", "sin", "print", "sqrt"],
        "answers": [0, 1, 3]
    },
    {
        "question": "Kādas vērtības var būt bool tipam?",
        "options": ["True", "False", "0", "1"],
        "answers": [0, 1]
    }
]