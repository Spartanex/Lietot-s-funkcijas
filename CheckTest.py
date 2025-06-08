import tkinter as tk
from tkinter import messagebox
import random

# Обновлённые вопросы
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

random.shuffle(questions)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Skaitlisko Funkciju Tests")

        self.q_index = 0
        self.correct = 0
        self.incorrect_questions = []

        self.question_var = tk.StringVar()
        self.options_vars = []

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()

        self.label = tk.Label(self.frame, textvariable=self.question_var, wraplength=400, justify="left")
        self.label.pack(anchor="w")

        for _ in range(4):
            var = tk.IntVar()
            cb = tk.Checkbutton(self.frame, variable=var)
            cb.pack(anchor="w")
            self.options_vars.append((var, cb))

        self.next_btn = tk.Button(self.frame, text="Tālāk", command=self.next_question)
        self.next_btn.pack(pady=10)

        self.display_question()

    def display_question(self):
        q = questions[self.q_index]
        self.question_var.set(f"{self.q_index + 1}. {q['question']}")
        for i, option in enumerate(q['options']):
            self.options_vars[i][0].set(0)
            self.options_vars[i][1].config(text=option)

    def next_question(self):
        selected = [i for i, (var, _) in enumerate(self.options_vars) if var.get()]
        correct_answers = questions[self.q_index]["answers"]
        if set(selected) == set(correct_answers):
            self.correct += 1
        else:
            self.incorrect_questions.append(questions[self.q_index]["question"])

        self.q_index += 1
        if self.q_index >= len(questions):
            self.show_result()
        else:
            self.display_question()

    def show_result(self):
        self.frame.destroy()
        result_text = f"Pareizi atbildēts: {self.correct} no {len(questions)} jautājumiem."
        result_label = tk.Label(self.root, text=result_text, font=("Arial", 14))
        result_label.pack(pady=10)

        if self.incorrect_questions:
            tk.Label(self.root, text="Nepareizi atbildētie jautājumi:", font=("Arial", 12)).pack()
            for q in self.incorrect_questions:
                tk.Label(self.root, text="• " + q, wraplength=500, justify="left").pack(anchor="w")

root = tk.Tk()
app = QuizApp(root)
root.mainloop()