import tkinter

window=tkinter.Tk()

window.title("비엘이 최고얌")
window.geometry("500x300+300+300")      
window.resizable(1,1)

label=tkinter.Label(window, text="어떤 공 수를 원해?",width=20, height=5)
label.pack()

button=tkinter.Button(window, text="조폭공 한명 추가요", width=15, relief="solid", overrelief="groove", bg="light blue")
button.pack(side="left")

button=tkinter.Button(window, text="가난수 한명 추가요", width=15,relief="solid", overrelief="groove", bg="light pink")
button.pack(side="right")

window.mainloop()