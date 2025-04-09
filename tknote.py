#-Widgets
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st

window = tk.Tk()
window.title("widget")
window.geometry('800x500')

label = tk.Label(window,text = "Name",font=("Times New Roman Bold" ,20),fg="pink")
label.grid(column=0,row=0,padx=0,pady=0)

label_question = tk.Label(window,text = "who are you??",font=("Times New Roman Bold" ,20),fg="pink")
label_question.grid(column=0,row=1,padx=0,pady=0)

label_gender = tk.Label(window,text = "Gender",font=("Times New Roman Bold",20))
label_gender.grid(column=0,row=2,padx=0,pady=0)

label_male = tk.Label(window,text = "male",fg ="blue",font=("Times New Roman Bold",20))
label_male.grid(column=0,row=3)

label_Female = tk.Label(window,text = "Female",fg ="pink",font=("Times New Roman Bold",20))
label_Female.grid(column=0,row=4)

label_other = tk.Label(window,text = "other",fg ="purple",font=("Times New Roman Bold",20))
label_other.grid(column=0,row=5)

label_feed = tk.Label(window,text = "Feedback:",font=("Times New Roman Bold",20))
label_feed.grid(column=0,row=12)

txt = tk.Entry(window, width=16)
txt.grid(column=1,row=0,padx=0,pady=0)

def entered():
    sen = "WelCome "+ txt.get()
    label.configure(text = sen)
entrybt = tk.Button(window,text="Submit", highlightbackground = "pink",fg = "blue",command=entered)
entrybt.grid(column=2,row=0,padx=0,pady=0)

combo = ttk.Combobox(window)
combo['values']=("select","Human","Alien","Robot","IDK")
combo.current(0)
combo.grid(column=1,row=1,padx=0,pady=0)


def clicked():
    hey = "Hello "+ combo.get()
    label_question.configure(text = hey)
bt = tk.Button(window,text="Submit", highlightbackground = "pink",fg = "blue",command=clicked)
bt.grid(column=2,row=1,padx=10,pady=0)

chk_male = tk.BooleanVar()
chk_female = tk.BooleanVar()
chk_other = tk.BooleanVar()

chkbox_male = tk.Checkbutton(window, text="Select", variable=chk_male)
chkbox_male.grid(column=1, row=3, padx=5, pady=5)

chkbox_female = tk.Checkbutton(window, text="Select", variable=chk_female)
chkbox_female.grid(column=1, row=4, padx=5, pady=5)

chkbox_other = tk.Checkbutton(window, text="Select", variable=chk_other)
chkbox_other.grid(column=1, row=5, padx=5, pady=5)

rad1 = tk.Radiobutton(window,text="child",value=1,font = ("Times New Roman Bold",20))
rad2 = tk.Radiobutton(window,text="teen",value=2,font = ("Times New Roman Bold",20))
rad3 = tk.Radiobutton(window,text="Adult",value=3,font = ("Times New Roman Bold",20))
rad1.grid(column=0,row=11)
rad2.grid(column=1,row=11)
rad3.grid(column=2,row=11)

text_area = st.ScrolledText(window, width=40, height=10, wrap=tk.WORD)
text_area.grid(column=0, row=15, padx=10, pady=10)

# Button to Get Text
def show_text():
    print("User's feedback:\n", text_area.get("1.0", tk.END))  # Get text from ScrolledText

btn = tk.Button(window, text="submit", command=show_text)
btn.grid(column=1, row=15, pady=5)


window.mainloop()


