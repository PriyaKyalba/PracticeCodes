import tkinter # import 
window = tkinter.Tk() # create window
window.title("GUI") # rename winow
label = tkinter.Label(window,text = "Hello World!").pack() # Label widget for single line widget like text ,image.pack is used to show the object in the window
window.mainloop()