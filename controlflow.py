# ---------------------------------------------------------------------
# 控制流程

import random
import tkinter
import tkinter.messagebox as messagebox

m = random.randint(0, 1000)

def check_guess():
    hit = False
    try:
        n = float(guess_input.get())
    except ValueError:
        messagebox.showinfo('Wrong input!', 'Please input a number!')
        return hit
    if n == m:
        messagebox.showinfo('Great!', 'You get it! My number is {}'.format(m))
        hit = True
    elif n < m:
        messagebox.showerror('Too small!', 'Try something bigger!')
    else:
        messagebox.showerror('Too big!', 'Try something small!')
    return hit


window = tkinter.Tk()
window.title('Guess Game!')

tkinter.Label(window, text="Input your guess between 0 and 1000:").grid(row=0)
guess_input = tkinter.Entry(window)
guess_input.grid(row=0, column=1)
tkinter.Button(window, text="Guess!", command=check_guess).grid(row=1, columnspan=2)


window.mainloop()