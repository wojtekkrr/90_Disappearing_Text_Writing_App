import tkinter
from tkinter import *
from tkinter import ttk
import time

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

# Kolory
COLOUR_PALETTE = ["#112D4E", "#3F72AF", "#DBE2EF", "#F9F7F7"]

text = ""

rows = 10

row_width = 10

count_time = 5

timer_r = None

last_key_press_time = None

# ---------------------------- Exit window ------------------------------- #
def exit_fullscreen(event):
    window.attributes("-fullscreen", False)


# ---------------------------- Writing text ------------------------------- #
def write(event):
    global text
    global rows
    global last_key_press_time
    # Pobierz znak wpisany na klawiaturze
    pressed_key = event.char

    last_key_press_time = time.time()
    text_disappear()
    # Wyświetlenie tekstu
    text = text + pressed_key

    chunk_size = row_width
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    for i in range(1, rows + 1):
        if len(chunks) <= rows:
            if i <= len(chunks):
                exec(f'written_text_label_{i}.config(text="{chunks[i - 1]}")')
        else:
            exec(f'written_text_label_{i}.config(text="{chunks[len(chunks) - rows + i - 1]}")')


# --------------------- DISAPPEARING MECHANISM ------------------------ #
def text_disappear():
    global timer_r
    global last_key_press_time

    for i in range(3, 5):
        if time.time() - last_key_press_time >= i:
            for j in range(1, rows + 1):
                exec(f'written_text_label_{j}.configure(style="Font_{i}.TLabel")')
    if count_time <= 0:
        return

    timer_r = window.after(1000, text_disappear)


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

# Utworzenie styli dla tekstu napisanego przez użytkownika
style_3 = ttk.Style()
style_2 = ttk.Style()
style_1 = ttk.Style()
style_0 = ttk.Style()
style_3.configure("Font_3.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[3])
style_2.configure("Font_2.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[2])
style_1.configure("Font_1.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[1])
style_0.configure("Font_0.TLabel", background=COLOUR_PALETTE[0], foreground=COLOUR_PALETTE[0])

# Napisany tekst przez użytkownika
for i in range(1, rows + 1):
    label = f"written_text_label_{i}"
    argument_1 = f'ttk.Label(text="", font=(FONT_NAME, 15), width={row_width})'
    argument_2 = f".grid(column=0, row={i + 1})"
    argument_3 = f'.configure(style="Font_3.TLabel")'
    exec(f"{label} = {argument_1}")
    exec(f"{label}{argument_2}")
    exec(f'{label}{argument_3}')

# Przypisz funkcję on_key_press do zdarzenia KeyPress na oknie głównym
window.bind("<KeyPress>", write)

window.mainloop()
