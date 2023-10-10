import tkinter
from tkinter import *
from tkinter import ttk

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

# Kolory
COLOUR_PALETTE = ["#112D4E", "#3F72AF", "#DBE2EF", "#F9F7F7"]

text = ""

# ---------------------------- Exit window ------------------------------- #
def exit_fullscreen(event):
    window.attributes("-fullscreen", False)


# ---------------------------- Writing text ------------------------------- #
def write(event):
    global text
    # Pobierz znak wpisany na klawiaturze
    pressed_key = event.char
    # Wyświetlenie tekstu
    text = text + pressed_key
    text_label.config(text=text)


# ---------------- Label width depending on window width ------------------ #
def update_label_width(event):
    text_label.config(width=window.winfo_width())


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Disappearing Text Writing App")
window.config(padx=100, pady=50, bg=COLOUR_PALETTE[0])

# Środkowanie zawartości
# window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Ustawienie okna na pełny ekran
window.attributes("-fullscreen", True)

# Przypisanie klawisza Esc do funkcji wyjścia z pełnego ekranu
window.bind("<Escape>", exit_fullscreen)

# Tytuł
title = Label(text="Disappearing Text Writing App", font=(FONT_NAME, 35), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
title.grid(column=0, row=0, pady=25)

# Komunikat
text_label = Label(text="Type the text below:", font=(FONT_NAME, 18), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3])
text_label.grid(column=0, row=1, pady=50)

# Napisany tekst przez użytkownika
written_text_label = Label(text="1", font=(FONT_NAME, 15), bg=COLOUR_PALETTE[0], fg=COLOUR_PALETTE[3], width=window.winfo_width())
written_text_label.grid(column=0, row=2, pady=25)

# Utworzenie styli dla tesktu napisanego przez użytkownika
style_2 = ttk.Style()
style_1 = ttk.Style()
style_0 = ttk.Style()
style_2.configure("Font_2.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[2])
style_1.configure("Font_1.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[1])
style_0.configure("Font_0.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[0])

# Przypisz funkcję on_key_press do zdarzenia KeyPress na oknie głównym
window.bind("<KeyPress>", write)

# Przypisz funkcję update_label_width do zdarzenia zmiany rozmiaru okna
window.bind("<Configure>", update_label_width)

window.mainloop()
