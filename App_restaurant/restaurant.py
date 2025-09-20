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
meal_frame = LabelFrame(left_frame, text="Comida", font=('Dosis',19,'bold'), bd=1, relief=FLAT, fg='azure4')
meal_frame.pack(side=LEFT)

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

# products list -------------------------------------------------------------------------------------------------------

food_list = ['Pollo', 'Carne', 'Pescado', 'Arroz', 'Pasta', 'Ensalada', 'Sopa', 'Pan']
drinks_list = ['Agua', 'Refresco', 'Cerveza', 'Vino', 'Zumo', 'Café', 'Té', 'Leche']
dessert_list = ['Helado', 'Tarta', 'Fruta', 'Yogur', 'Galletas', 'Flan', 'Natillas', 'Chocolates']

# generate meal items ------------------------------------------------------------------------------------------------
meal_variables = []
frame_0 = []
text_0 = []
contador = 0

for i in food_list:
    
    # ceate checkbutton
    meal_variables.append('')
    meal_variables[contador] = IntVar()
    i = Checkbutton(meal_frame, 
                    text = i.title(), 
                    font=('Dosis',19,'bold'),
                    onvalue=1, 
                    offvalue=0,
                    variable=meal_variables[contador])
    i.grid(row=contador,
            column=0, 
            sticky=W)
    
    #create entry frames
    frame_0.append('')
    text_0.append('')
    text_0[contador] = StringVar()
    text_0[contador].set('0')
    
    
    frame_0[contador] = Entry(meal_frame,
                                font=('Dosis',18,'bold'), 
                                bd=1, 
                                width=6, 
                                state=DISABLED,
                                textvariable=text_0[contador])
    frame_0[contador].grid(row=contador, 
                                column=1)
    contador += 1

# generate drinks items --------------------------------------------------------------------------------------------------------
drinks_variables = []
frame_1 = []
text_1 = []
contador = 0

for i in drinks_list:
    
    # ceate checkbutton
    drinks_variables.append('')
    drinks_variables[contador] = IntVar()
    i = Checkbutton(drinks_frame,
                    text = i.title(),
                    font=('Dosis',19,'bold'),
                    onvalue=1,
                    offvalue=0,
                    variable=drinks_variables[contador])
    i.grid(row=contador,
            column=0,
            sticky=W)
    
    #create entry frames
    frame_1.append('')
    text_1.append('')
    text_1[contador] = StringVar()
    text_1[contador].set('0')
    
    frame_1[contador] = Entry(drinks_frame,
                                font=('Dosis',18,'bold'), 
                                bd=1, 
                                width=6, 
                                state=DISABLED,
                                textvariable=text_1[contador])
    frame_1[contador].grid(row=contador, 
                                column=1)
    contador += 1


# generate drinks items --------------------------------------------------------------------------------------------------------
dessert_variables = []
frame_2 = []
text_2 = []
contador = 0

for i in dessert_list:
    
    # ceate checkbutton
    dessert_variables.append('')
    dessert_variables[contador] = IntVar()
    i = Checkbutton(dessert_frame,
                    text = i.title(),
                    font=('Dosis',19,'bold'),
                    onvalue=1,
                    offvalue=0,
                    variable=dessert_variables[contador])
    i.grid(row=contador,
            column=0,
            sticky=W)
    
    #create entry frames
    frame_2.append('')
    text_2.append('')
    text_2[contador] = StringVar()
    text_2[contador].set('0')
    
    frame_2[contador] = Entry(dessert_frame,
                                font=('Dosis',18,'bold'), 
                                bd=1, 
                                width=6, 
                                state=DISABLED,
                                textvariable=text_2[contador])
    frame_2[contador].grid(row=contador, 
                                column=1)
    contador += 1



# Avoid closing
app.mainloop()