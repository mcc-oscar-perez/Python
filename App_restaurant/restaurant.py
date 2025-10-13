from tkinter import *

# Variable 
operador = ''

def clik_button(numero):
    global operador
    operador = operador + numero
    visor_calculator.delete(0,END)
    visor_calculator.insert(END,operador)
    
def delete_data ():
    global operador
    operador = ''
    visor_calculator.delete(0,END)
    
def restult():
    global operador
    result_a = str(eval(operador))
    visor_calculator.delete(0,END)
    visor_calculator.insert(0,result_a)
    
def revisar_check():
    x= 0
    for i in meal_frame:
        if meal_variables[x].get() == 1:
            meal_frame[x].config(state=NORMAL)
    x +=1 
    

# tkinter init window
app = Tk()

# size of the window
app.geometry("1170x630+0+0")

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
cost_frame = Frame(left_frame, bd=1, relief=FLAT, bg='azure4', padx=85)
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
    
    # Create checkbutton
    meal_variables.append('')
    meal_variables[contador] = IntVar()
    i = Checkbutton(meal_frame, 
                    text = i.title(), 
                    font=('Dosis',19,'bold'),
                    onvalue=1, 
                    offvalue=0,
                    variable=meal_variables[contador],
                    command=revisar_check)
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
                    variable=drinks_variables[contador],
                    command=revisar_check)
    
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
                    variable=dessert_variables[contador],
                    command=revisar_check)
    
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


# Variables
var_cost_meal=StringVar()
var_cost_drink=StringVar()
var_cost_dessert=StringVar()
var_subtotal=StringVar()
var_tax=StringVar()
var_total=StringVar()

# Cost labels and input fields (food) --------------------------------
labels_cost_meal = Label(cost_frame,
                            text="Costo comida",
                            font= ('Dosis',12, 'bold'),
                            bg='azure4',
                            fg='white')
labels_cost_meal.grid(row=0, column=0)

text_cost_meal = Entry(cost_frame,
                        font=('Dosis',12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_cost_meal)
text_cost_meal.grid(row=0, column=1, padx = 41)



# Cost labels and input fields (Drinks) --------------------------------
labels_cost_drink = Label(cost_frame,
                            text="Costo bebida",
                            font= ('Dosis',12, 'bold'),
                            bg='azure4',
                            fg='white')
labels_cost_drink.grid(row=1, column=0)

text_cost_drink = Entry(cost_frame,
                        font=('Dosis',12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_cost_drink)
text_cost_drink.grid(row=1, column=1, padx = 41)


# Cost labels and input fields (Dessert) --------------------------------
labels_cost_dessert = Label(cost_frame,
                            text="Costo postre",
                            font= ('Dosis',12, 'bold'),
                            bg='azure4',
                            fg='white')
labels_cost_dessert.grid(row=2, column=0)

text_cost_dessert = Entry(cost_frame,
                        font=('Dosis',12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_cost_dessert)
text_cost_dessert.grid(row=2, column=1, padx = 41)



# Cost labels and input fields (Subtotal) --------------------------------
labels_subtotal = Label(cost_frame,
                            text="Subtotal",
                            font= ('Dosis',12, 'bold'),
                            bg='azure4',
                            fg='white')
labels_subtotal.grid(row=0, column=2)

text_subtotal = Entry(cost_frame,
                        font=('Dosis',12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_subtotal)
text_subtotal.grid(row=0, column=3, padx = 41)

# Cost labels and input fields (Tax) --------------------------------
labels_tax = Label(cost_frame,
                            text="tax",
                            font= ('Dosis',12, 'bold'),
                            bg='azure4',
                            fg='white')
labels_tax.grid(row=1, column=2)

text_tax = Entry(cost_frame,
                        font=('Dosis',12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_tax)
text_tax.grid(row=1, column=3, padx = 41)

# Cost labels and input fields (Total) --------------------------------
labels_total = Label(cost_frame,
                            text="Total",
                            font= ('Dosis',12, 'bold'),
                            bg='azure4',
                            fg='white')
labels_total.grid(row=2, column=2)

text_total = Entry(cost_frame,
                        font=('Dosis',12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_total)
text_total.grid(row=2, column=3, padx = 41)

#buttons 

buttons = ['Total', 'Ticket', 'Save','Reset']
Columns = 0 

for i in buttons:
    i = Button(buttons_frame,
                text=i.title(),
                font=('Dosis',14, 'bold'),
                fg='white',
                bg= 'azure4',
                bd= 1,
                width= 9)
    
    i.grid(row=0,column=Columns)
    Columns+=1
    


# ticket area 
receipt_text = Text(receipt_frame,
                    font=('Dosis',12,'bold'),
                    bd = 1,
                    width = 42,
                    height= 10)

receipt_text.grid(row=0,column=0)


# Calculator
visor_calculator = Entry(calculator_frame,
                        font=('dosis',16,'bold'),
                        width=32,
                        bd=1)

visor_calculator.grid(row=0, column=0, columnspan= 4)


# calulator buttons
calculator_buttons = ['7','8','9','+','4','5','6','-',
                    '1','2','3','x','R','B','0','/']

saved_buttons = []

fila = 1
columna = 0 

for i in calculator_buttons:
    i = Button(calculator_frame,
                text=i.title(),
                font= ('dosis',16,'bold'),
                fg='white',
                bg='azure4',
                bd=1,
                width=8)
    
    saved_buttons.append(i)
    
    i.grid(row=fila, column= columna)
    
    if columna == 3:
        fila +=1
    
    columna += 1
    
    if columna == 4:
        columna = 0


saved_buttons[0].config(command =  lambda: clik_button("7"))
saved_buttons[1].config(command =  lambda: clik_button("8"))
saved_buttons[2].config(command =  lambda: clik_button("9"))
saved_buttons[3].config(command =  lambda: clik_button("+"))
saved_buttons[4].config(command =  lambda: clik_button("4"))
saved_buttons[5].config(command =  lambda: clik_button("5"))
saved_buttons[6].config(command =  lambda: clik_button("6"))
saved_buttons[7].config(command =  lambda: clik_button("-"))
saved_buttons[8].config(command =  lambda: clik_button("1"))
saved_buttons[9].config(command =  lambda: clik_button("2"))
saved_buttons[10].config(command =  lambda: clik_button("3"))
saved_buttons[11].config(command =  lambda: clik_button("*"))
saved_buttons[12].config(command =  restult)
saved_buttons[13].config(command =  delete_data)
saved_buttons[14].config(command =  lambda: clik_button("0"))
saved_buttons[15].config(command =  lambda: clik_button("/"))


# Avoid closing
app.mainloop() 