import tkinter
win = tkinter.Tk()
win.title("수식 계산기")
win.geometry("380x130")
entry1 = tkinter.Entry(win)
entry1.config(font="None 15 bold")
entry1.config(fg="Green", bg="LightYellow")
entry1.place(x=40, y=30)
button1 = tkinter.Button(win)
button1.config(text="계산하기")
button1.place(x=280, y=30)
label1 = tkinter.Label(win)
label1.config(text="계산결과는?")
label1.config(font="None 15 bold", fg="Red")
label1.place(x=40, y=70)
# 여기서부터 코드를 작성하세요.

win.mainloop()