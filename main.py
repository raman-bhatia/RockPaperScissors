import tkinter as tk
import random

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

#Game Logic
user_score = 0
comp_score = 0
user_choice = ""
comp_choice = ""

def random_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def result(user,comp):
    global user_score
    global comp_score
    if(user==comp):
        print("Tie")
    elif(user=="rock"):
        if(comp=="scissors"):
            print("You Win")
            user_score = user_score + 1
        else: 
            print("Comp Wins")
            comp_score = comp_score + 1
    elif(user=="paper"):
        if(comp=="rock"):
            print("You Win")
            user_score = user_score + 1
        else: 
            print("Comp Wins")
            comp_score = comp_score + 1

    elif(user=="scissors"):
        if(comp=="paper"):
            print("You Win")
            user_score = user_score + 1
        else: 
            print("Comp Wins")
            comp_score = comp_score + 1
    
    text_area = tk.Text(master=frame1, height = 12, width = 30, padx = 10, pady = 10, bg = "#CAD5E2")
    text_area.grid(column=0, row=0)
    answer = "\n\nYour Choice : {uc} \nComputer's Choice : {cc} \n\nYour Score : {u} \nComputer Score : {c}".format(uc=user_choice, cc=comp_choice, u=user_score, c=comp_score)
    text_area.insert(tk.END, answer)

def rock():
    global user_choice
    global comp_choice
    user_choice = 'rock'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def paper():
    global user_choice
    global comp_choice
    user_choice = 'paper'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def scissors():
    global user_choice
    global comp_choice
    user_choice = 'scissors'
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)


#Game GUI
frame1 = tk.Frame(window)
frame1.grid(column=0, row=0)

text_area = tk.Text(master=frame1, height=12,width=30, padx=10, pady=10, bg="#CAD5E2")
text_area.grid(column=0, row=0)
text_area.insert(tk.END,"\n\nYour Score : 0 \nComputer Score : 0 \n \nClick on any button to start.")

frame2 = tk.Frame(window)
frame2.grid(column=1, row=0)

button1 = tk.Button(frame2, text = "    Rock    ",bg="#50DBB4",padx=25,pady=25,command = rock)
button1.grid(column=0, row=0)
button2 = tk.Button(frame2, text = "    Paper    ",bg="#50DBB4",padx=25,pady=25, command=paper)
button2.grid(column=0, row=1)
button3 = tk.Button(frame2, text = "    Scissors    ",bg="#50DBB4",padx=20,pady=25, command=scissors)
button3.grid(column=0, row=2)

window.mainloop()