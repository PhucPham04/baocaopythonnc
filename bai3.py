import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import Tk,Button

win = Tk()
win.title('OX Game')


clicked = True
count = 0

def disableButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)
    button10.config(state=DISABLED)
    button11.config(state=DISABLED)
    button12.config(state=DISABLED)
    button13.config(state=DISABLED)
    button14.config(state=DISABLED)
    button15.config(state=DISABLED)
    button16.config(state=DISABLED)
    button17.config(state=DISABLED)
    button18.config(state=DISABLED)
    button19.config(state=DISABLED)
    button20.config(state=DISABLED)
    button21.config(state=DISABLED)
    button22.config(state=DISABLED)
    button23.config(state=DISABLED)
    button24.config(state=DISABLED)
    button25.config(state=DISABLED)
    button26.config(state=DISABLED)
    button27.config(state=DISABLED)
    button28.config(state=DISABLED)
    button29.config(state=DISABLED)
    button30.config(state=DISABLED)
    button31.config(state=DISABLED)
    button32.config(state=DISABLED)
    button33.config(state=DISABLED)
    button34.config(state=DISABLED)
    button35.config(state=DISABLED)
    button36.config(state=DISABLED)
    
    
    
def checkwinner():
    global win
    win = False
    
   
    # Kiểm tra hàng dọc phía phải
    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X") or \
   (button2["text"] == "X" and button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X") or \
   (button3["text"] == "X" and button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" and button7["text"] == "X") or \
   (button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X") or \
   (button5["text"] == "X" and button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X") or \
   (button6["text"] == "X" and button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" and button10["text"] == "X") or \
   (button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" and button10["text"] == "X" and button11["text"] == "X") or \
   (button8["text"] == "X" and button9["text"] == "X" and button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X") or \
   (button9["text"] == "X" and button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X") or \
   (button10["text"] == "X" and button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X" and button14["text"] == "X") or \
   (button11["text"] == "X" and button12["text"] == "X" and button13["text"] == "X" and button14["text"] == "X" and button15["text"] == "X") or \
   (button12["text"] == "X" and button13["text"] == "X" and button14["text"] == "X" and button15["text"] == "X" and button16["text"] == "X") or \
   (button17["text"] == "X" and button18["text"] == "X" and button19["text"] == "X" and button20["text"] == "X" and button21["text"] == "X") or \
   (button18["text"] == "X" and button19["text"] == "X" and button20["text"] == "X" and button21["text"] == "X" and button22["text"] == "X") or \
   (button19["text"] == "X" and button20["text"] == "X" and button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X") or \
   (button20["text"] == "X" and button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X" and button24["text"] == "X") or \
   (button21["text"] == "X" and button22["text"] == "X" and button23["text"] == "X" and button24["text"] == "X" and button25["text"] == "X") or \
   (button22["text"] == "X" and button23["text"] == "X" and button24["text"] == "X" and button25["text"] == "X" and button26["text"] == "X") or \
   (button23["text"] == "X" and button24["text"] == "X" and button25["text"] == "X" and button26["text"] == "X" and button27["text"] == "X") or \
   (button24["text"] == "X" and button25["text"] == "X" and button26["text"] == "X" and button27["text"] == "X" and button28["text"] == "X") or \
   (button25["text"] == "X" and button26["text"] == "X" and button27["text"] == "X" and button28["text"] == "X" and button29["text"] == "X") or \
   (button26["text"] == "X" and button27["text"] == "X" and button28["text"] == "X" and button29["text"] == "X" and button30["text"] == "X") or \
   (button27["text"] == "X" and button28["text"] == "X" and button29["text"] == "X" and button30["text"] == "X" and button31["text"] == "X") or \
   (button28["text"] == "X" and button29["text"] == "X" and button30["text"] == "X" and button31["text"] == "X" and button32["text"] == "X") or \
   (button29["text"] == "X" and button30["text"] == "X" and button31["text"] == "X" and button32["text"] == "X" and button33["text"] == "X") or \
   (button30["text"] == "X" and button31["text"] == "X" and button32["text"] == "X" and button33["text"] == "X" and button34["text"] == "X") or \
   (button31["text"] == "X" and button32["text"] == "X" and button33["text"] == "X" and button34["text"] == "X" and button35["text"] == "X") or \
   (button32["text"] == "X" and button33["text"] == "X" and button34["text"] == "X" and button35["text"] == "X" and button36["text"] == "X") or \
   (button1["text"] == "X" and button7["text"] == "X" and button13["text"] == "X" and button19["text"] == "X" and button25["text"] == "X") or \
   (button2["text"] == "X" and button8["text"] == "X" and button14["text"] == "X" and button20["text"] == "X" and button26["text"] == "X") or \
   (button3["text"] == "X" and button9["text"] == "X" and button15["text"] == "X" and button21["text"] == "X" and button27["text"] == "X") or \
   (button4["text"] == "X" and button10["text"] == "X" and button16["text"] == "X" and button22["text"] == "X" and button28["text"] == "X") or \
   (button5["text"] == "X" and button11["text"] == "X" and button17["text"] == "X" and button23["text"] == "X" and button29["text"] == "X") or \
   (button6["text"] == "X" and button12["text"] == "X" and button18["text"] == "X" and button24["text"] == "X" and button30["text"] == "X") or \
   (button7["text"] == "X" and button13["text"] == "X" and button19["text"] == "X" and button25["text"] == "X" and button31["text"] == "X") or \
   (button8["text"] == "X" and button14["text"] == "X" and button20["text"] == "X" and button26["text"] == "X" and button32["text"] == "X") or \
   (button9["text"] == "X" and button15["text"] == "X" and button21["text"] == "X" and button27["text"] == "X" and button33["text"] == "X") or \
   (button10["text"] == "X" and button16["text"] == "X" and button22["text"] == "X" and button28["text"] == "X" and button34["text"] == "X") or \
   (button11["text"] == "X" and button17["text"] == "X" and button23["text"] == "X" and button29["text"] == "X" and button35["text"] == "X") or \
   (button12["text"] == "X" and button18["text"] == "X" and button24["text"] == "X" and button30["text"] == "X" and button36["text"] == "X") or \
   (button1["text"] == "X" and button8["text"] == "X" and button15["text"] == "X" and button22["text"] == "X" and button29["text"] == "X") or \
   (button2["text"] == "X" and button9["text"] == "X" and button16["text"] == "X" and button23["text"] == "X" and button30["text"] == "X") or \
   (button7["text"] == "X" and button14["text"] == "X" and button21["text"] == "X" and button28["text"] == "X" and button35["text"] == "X") or \
   (button8["text"] == "X" and button15["text"] == "X" and button22["text"] == "X" and button29["text"] == "X" and button36["text"] == "X"):
       # Thay đổi màu nền và hiển thị thông báo
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")

        win = True
        messagebox.showinfo("OX Game", "Player 1 WINNER!!")
        disableButtons()

    # Các điều kiện để người chơi 2 [O] chiến thắng
    elif(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O") or \
   (button2["text"] == "O" and button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O") or \
   (button3["text"] == "O" and button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" and button7["text"] == "O") or \
   (button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O") or \
   (button5["text"] == "O" and button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O") or \
   (button6["text"] == "O" and button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" and button10["text"] == "O") or \
   (button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" and button10["text"] == "O" and button11["text"] == "O") or \
   (button8["text"] == "O" and button9["text"] == "O" and button10["text"] == "O" and button11["text"] == "O" and button12["text"] == "O") or \
   (button9["text"] == "O" and button10["text"] == "O" and button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O") or \
   (button10["text"] == "O" and button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O" and button14["text"] == "O") or \
   (button11["text"] == "O" and button12["text"] == "O" and button13["text"] == "O" and button14["text"] == "O" and button15["text"] == "O") or \
   (button12["text"] == "O" and button13["text"] == "O" and button14["text"] == "O" and button15["text"] == "O" and button16["text"] == "O") or \
   (button17["text"] == "O" and button18["text"] == "O" and button19["text"] == "O" and button20["text"] == "O" and button21["text"] == "O") or \
   (button18["text"] == "O" and button19["text"] == "O" and button20["text"] == "O" and button21["text"] == "O" and button22["text"] == "O") or \
   (button19["text"] == "O" and button20["text"] == "O" and button21["text"] == "O" and button22["text"] == "O" and button23["text"] == "O") or \
   (button20["text"] == "O" and button21["text"] == "O" and button22["text"] == "O" and button23["text"] == "O" and button24["text"] == "O") or \
   (button21["text"] == "O" and button22["text"] == "O" and button23["text"] == "O" and button24["text"] == "O" and button25["text"] == "O") or \
   (button22["text"] == "O" and button23["text"] == "O" and button24["text"] == "O" and button25["text"] == "O" and button26["text"] == "O") or \
   (button23["text"] == "O" and button24["text"] == "O" and button25["text"] == "O" and button26["text"] == "O" and button27["text"] == "O") or \
   (button24["text"] == "O" and button25["text"] == "O" and button26["text"] == "O" and button27["text"] == "O" and button28["text"] == "O") or \
   (button25["text"] == "O" and button26["text"] == "O" and button27["text"] == "O" and button28["text"] == "O" and button29["text"] == "O") or \
   (button26["text"] == "O" and button27["text"] == "O" and button28["text"] == "O" and button29["text"] == "O" and button30["text"] == "O") or \
   (button27["text"] == "O" and button28["text"] == "O" and button29["text"] == "O" and button30["text"] == "O" and button31["text"] == "O") or \
   (button28["text"] == "O" and button29["text"] == "O" and button30["text"] == "O" and button31["text"] == "O" and button32["text"] == "O") or \
   (button29["text"] == "O" and button30["text"] == "O" and button31["text"] == "O" and button32["text"] == "O" and button33["text"] == "O") or \
   (button30["text"] == "O" and button31["text"] == "O" and button32["text"] == "O" and button33["text"] == "O" and button34["text"] == "O") or \
   (button31["text"] == "O" and button32["text"] == "O" and button33["text"] == "O" and button34["text"] == "O" and button35["text"] == "O") or \
   (button32["text"] == "O" and button33["text"] == "O" and button34["text"] == "O" and button35["text"] == "O" and button36["text"] == "O") or \
   (button1["text"] == "O" and button7["text"] == "O" and button13["text"] == "O" and button19["text"] == "O" and button25["text"] == "O") or \
   (button2["text"] == "O" and button8["text"] == "O" and button14["text"] == "O" and button20["text"] == "O" and button26["text"] == "O") or \
   (button3["text"] == "O" and button9["text"] == "O" and button15["text"] == "O" and button21["text"] == "O" and button27["text"] == "O") or \
   (button4["text"] == "O" and button10["text"] == "O" and button16["text"] == "O" and button22["text"] == "O" and button28["text"] == "O") or \
   (button5["text"] == "O" and button11["text"] == "O" and button17["text"] == "O" and button23["text"] == "O" and button29["text"] == "O") or \
   (button6["text"] == "O" and button12["text"] == "O" and button18["text"] == "O" and button24["text"] == "O" and button30["text"] == "O") or \
   (button7["text"] == "O" and button13["text"] == "O" and button19["text"] == "O" and button25["text"] == "O" and button31["text"] == "O") or \
   (button8["text"] == "O" and button14["text"] == "O" and button20["text"] == "O" and button26["text"] == "O" and button32["text"] == "O") or \
   (button9["text"] == "O" and button15["text"] == "O" and button21["text"] == "O" and button27["text"] == "O" and button33["text"] == "O") or \
   (button10["text"] == "O" and button16["text"] == "O" and button22["text"] == "O" and button28["text"] == "O" and button34["text"] == "O") or \
   (button11["text"] == "O" and button17["text"] == "O" and button23["text"] == "O" and button29["text"] == "O" and button35["text"] == "O") or \
   (button12["text"] == "O" and button18["text"] == "O" and button24["text"] == "O" and button30["text"] == "O" and button36["text"] == "O") or \
   (button1["text"] == "O" and button8["text"] == "O" and button15["text"] == "O" and button22["text"] == "O" and button29["text"] == "O") or \
   (button2["text"] == "O" and button9["text"] == "O" and button16["text"] == "O" and button23["text"] == "O" and button30["text"] == "O") or \
   (button7["text"] == "O" and button14["text"] == "O" and button21["text"] == "O" and button28["text"] == "O" and button35["text"] == "O") or \
   (button8["text"] == "O" and button15["text"] == "O" and button22["text"] == "O" and button29["text"] == "O" and button36["text"] == "O"):
       # Thay đổi màu nền và hiển thị thông báo
        button1.config(bg="#80ffaa")
        button2.config(bg="#80ffaa")
        button3.config(bg="#80ffaa")
        button4.config(bg="#80ffaa")
        button5.config(bg="#80ffaa")
        button6.config(bg="#80ffaa")
        button7.config(bg="#80ffaa")
        button8.config(bg="#80ffaa")
        button9.config(bg="#80ffaa")
        button10.config(bg="#80ffaa")
        button11.config(bg="#80ffaa")
        button12.config(bg="#80ffaa")
        button13.config(bg="#80ffaa")
        button14.config(bg="#80ffaa")
        button15.config(bg="#80ffaa")
        button16.config(bg="#80ffaa")
        button17.config(bg="#80ffaa")
        button18.config(bg="#80ffaa")
        button19.config(bg="#80ffaa")
        button20.config(bg="#80ffaa")
        button21.config(bg="#80ffaa")
        button22.config(bg="#80ffaa")
        button23.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button24.config(bg="#80ffaa")
        button25.config(bg="#80ffaa")
        button26.config(bg="#80ffaa")
        button27.config(bg="#80ffaa")
        button28.config(bg="#80ffaa")
        button29.config(bg="#80ffaa")
        button30.config(bg="#80ffaa")
        button31.config(bg="#80ffaa")
        button32.config(bg="#80ffaa")
        button33.config(bg="#80ffaa")
        button34.config(bg="#80ffaa")
        button35.config(bg="#80ffaa")
        button36.config(bg="#80ffaa")

        win = True
        messagebox.showinfo("OX Game", "Player 2 WINNER!!")
        disableButtons()

def checkDraw():
    global count, win
    if count == 36 and not win:
        messagebox.showinfo("OX Game", "DRAW!!")

def buttonClicked(button):
    global clicked, count
    if button["text"] == ' ' and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkwinner()
        checkDraw()
    elif button["text"] == ' ' and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkwinner()
        checkDraw()
    elif button["text"] != ' ':
        messagebox.showerror("OX Game", "LỖI!! Vui lòng chọn lại")

def start():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button13, button14, button15, button16,button17, button18, button19, button20, button21, button22, button23, button24, button25, button26, button27, button28, button29, button30, button31, button32, button33, button34, button35, button36
    global clicked, count
    clicked = True
    count = 0

    button1 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button1))
    button2 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button2))
    button3 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button3))
    button4 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button4))
    button5 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button5))
    button6 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button6))
    button7 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button7))
    button8 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button8))
    button9 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button9))
    button10 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button10))
    button11 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button11))
    button12 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button12))
    button13 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button13))
    button14 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button14))
    button15 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button15))
    button16 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button16))
    button17 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button17))
    button18 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button18))
    button19 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button19))
    button20 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button20))
    button21 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button21))
    button22 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button22))
    button23 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button23))
    button24 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button24))
    button25 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button25))
    button26 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button26))
    button27 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button27))
    button28 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button28))
    button29 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button29))
    button30 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button30))
    button31 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button31))
    button32 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button32))
    button33 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button33))
    button34 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button34))
    button35 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button35))
    button36 = Button(win, text=' ', font=('Helvetica', 20), height=3, width=7, bg='SystemButtonFace', command=lambda: buttonClicked(button36))
    

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=0, column=5)
    button7.grid(row=1, column=0)
    button8.grid(row=1, column=1)
    button9.grid(row=1, column=2)
    button10.grid(row=1, column=3)
    button11.grid(row=1, column=4)
    button12.grid(row=1, column=5)
    button13.grid(row=2, column=0)
    button14.grid(row=2, column=1)
    button15.grid(row=2, column=2)
    button16.grid(row=2, column=3)
    button17.grid(row=2, column=4)
    button18.grid(row=2, column=5)
    button19.grid(row=3, column=0)
    button20.grid(row=3, column=1)
    button21.grid(row=3, column=2)
    button22.grid(row=3, column=3)
    button23.grid(row=3, column=4)
    button24.grid(row=3, column=5)
    button25.grid(row=4, column=0)
    button26.grid(row=4, column=1)
    button27.grid(row=4, column=2)
    button28.grid(row=4, column=3)
    button29.grid(row=4, column=4)
    button30.grid(row=4, column=5)
    button31.grid(row=5, column=0)
    button32.grid(row=5, column=1)
    button33.grid(row=5, column=2)
    button34.grid(row=5, column=3)
    button35.grid(row=5, column=4)
    button36.grid(row=5, column=5)

# gameMenu = Menu(win)
# win.config(menu=gameMenu)






# Create a menu bar
menu_bar = tk.Menu(win)
win.config(menu=menu_bar)

# Create a "option" menu
optionMenu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)

#Create a "File" menu
File_menu= tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=File_menu)
File_menu.add_command(label="New")
File_menu.add_command(label="Exit",command=win.destroy)

# Create a "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")


start()
win.mainloop()