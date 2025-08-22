from tkinter import *

# tkinter init window
app = Tk()

# size of the window
app.geometry("1020x630+0+0")

# Avoid maximizing
app.resizable(0, 0)

#window title
app.title("Restaurant Management System")

# Background color
app.config(bg="burlywood")

# upper frame
top_frame = Frame(app, bd=1, relief=FLAT)
top_frame.pack(side=TOP)

# upper frame title
label_top = Label(top_frame, text="Sistema de facturación", fg='azure4', font=('Dosis',58),bg='burlywood',width=27)
label_top.grid(row=0,column=0)

# left frame -----------------------------------------------------------------------------------------------------------
left_frame = Frame(app, bd=1, relief=FLAT)
left_frame.pack(side=LEFT)

# cost frame
cost_frame = Frame(left_frame, bd=1, relief=FLAT)
cost_frame.pack(side=BOTTOM)

# meal frame 
meale_frame = LabelFrame(left_frame, text="Comida", font=('Dosis',19,'bold'), bd=1, relief=FLAT, fg='azure4')
meale_frame.pack(side=LEFT)

# drinks frame
drinks_frame = LabelFrame(left_frame, text="Bebidas", font=('Dosis',19,'bold'), bd=1, relief=FLAT, fg='azure4')
drinks_frame.pack(side=LEFT)

# desserts frame
dessert_frame = LabelFrame(left_frame, text="Postres", font=('Dosis',19,'bold'), bd=1, relief=FLAT, fg='azure4')
dessert_frame.pack(side=LEFT)


# right frame ----------------------------------------------------------------------------------------------------------
left_frame = Frame(app, bd=1, relief=FLAT)
left_frame.pack(side=RIGHT)

# calculator frame
calculator_frame = Frame(left_frame, bd=1, relief=FLAT, bg='burlywood')
calculator_frame.pack()

# receipt frame
receipt_frame = Frame(left_frame, bd=1, relief=FLAT, bg='burlywood')
receipt_frame.pack()

# buttons frame
buttons_frame = Frame(left_frame, bd=1, relief=FLAT, bg='burlywood')
buttons_frame.pack()

# Avoid closing
app.mainloop()

