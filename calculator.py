from tkinter import * 
import math


sc_w = 1366
sc_h = 768

w = 500
h = 449

main_color = '#121212'
secondary_color = '#9966cc'
abg_color = 'light grey'


sc = Tk()
sc.geometry(f"{w}x{h}+{round(sc_w/2 - w/2)}+{round(sc_h/2 - h/2)}")
sc.title('Calculator')
sc.configure(bg = f'{main_color}')
sc.resizable(False,False)



output = []
length = 0








def w_info(widget):
    widget.pack()
    widget.update()
    print(widget,'width:',widget.winfo_width())
    widget.pack_forget()

def h_info(widget):
    widget.pack()
    widget.update()
    print(widget,'height:', widget.winfo_height())
    widget.pack_forget()





def print_number():
    number = display.get()
    print(number)
    

def clear():
    display.delete(0,END)
    output.clear()


def more():
    pass





def settings():
    sc_w = 1366
    sc_h = 768

    w = 500
    h = 449

    settings = Toplevel()
    settings.title('Settings')
    settings.geometry(f"{w}x{h}+{round(sc_w/2 - w/2)}+{round(sc_h/2 - h/2)}")
    settings.resizable(False,False)
    settings.configure(bg = 'white')
    title = Label(settings,
        text = 'Settings',
        font = ('Arial Black', 20),
        bg = 'white'
    )

    theme_label = Label(settings,
        text = 'Theme:',
        font = ('Verdana', 15),
        bg = 'white',
    )

    light_button = Button(settings,
        text = 'light',
        font = ('Verdana', 30),
        bg = 'light grey',
        fg = 'black',
        relief = 'solid',
        command=light
    )

    dark_button = Button(settings,
        text = 'dark',
        font = ('Verdana', 30),
        bg = f'{main_color}',
        fg = 'white',
        relief = 'solid',
        command=dark
    )

    title.pack()
    theme_label.pack()

    light_button.place(x = 50, y = 150)
    dark_button.place(x = w - 50 - 128, y = 150)


def divide():
    global length
    number = display.get()
    output.insert(0,number)
    output.insert(1,'/')
    display.insert(END, '/')
    length = len(number) + 1


def multiply():
    global length
    number = display.get()
    output.insert(0,number)
    output.insert(1,'*')
    display.insert(END, 'x')
    length = len(number) + 1



def minus():
    global length
    number = display.get()
    output.insert(0,number)
    output.insert(1,'-')
    display.insert(END, '-')
    length = len(number) + 1

    

def plus():
    global length
    number = display.get()
    output.insert(0,number)
    output.insert(1,'+')
    display.insert(END, '+')
    length = len(number) + 1


def enter():
    number = display.get()
    number_2 = number[length:]
    output.insert(2, number_2)
    print(output)


    if output[1] == '/':
        result = int(output[0])/int(output[2])
        print(result)

    elif output[1] == '*':
        result = int(output[0])*int(output[2])
        print(result)

    elif output[1] == '-':
        result = int(output[0])-int(output[2])
        print(result)

    elif output[1] == '+':
        result = int(output[0])+int(output[2])
        print(result)
    

    display.delete(0,END)
    display.insert(0, result)






display = Entry(font = ('Icon',34), justify='right')



button_more = Button(
    text = 'More',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = 'light grey',command = more
)
button_settings = Button(
    text = 'Stngs',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = 'light grey',command = settings
)
button_clear = Button(
    text = 'C',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = 'red',command = clear
)







button_1 = Button(
    text = '1',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,1)
)
button_2 = Button(
    text = '2',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,2)
)
button_3 = Button(
    text = '3',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,3)
)
button_4 = Button(
    text = '4',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,4)
)
button_5 = Button(
    text = '5',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,5)
)
button_6 = Button(
    text = '6',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,6)
)
button_7 = Button(
    text = '7',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,7)
)
button_8 = Button(
    text = '8',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,8)
)
button_9 = Button(
    text = '9',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,9)
)








button_0 = Button(text = '0',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    command = lambda:display.insert(END,0)
)
button_00 = Button(text = '00',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
)
button_dot = Button(text = ',',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
)










button_divide = Button(text = '/',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = f'{secondary_color}',command=divide
)
button_multiply = Button(text = 'x',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = f'{secondary_color}',command=multiply
)
button_minus = Button(text = '-',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = f'{secondary_color}',command=minus
)
button_plus = Button(text = '+',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = f'{secondary_color}',command=plus
)
button_enter = Button(text = '=',font = ('Icon', 30),
    width = 5,relief = 'flat',
    overrelief='solid', activebackground=f'{abg_color}',
    bg = f'{secondary_color}',command = enter
)







display.pack()



bttns_u_r = [button_more, button_settings, button_clear]
bttns_n = [button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]
bttns_l_r = [button_0, button_00, button_dot]
bttns_s = [button_divide, button_multiply, button_minus, button_plus,button_enter]


bg_bttns = bttns_n + bttns_l_r
bg_bttns.append(display)





def dark():
    for bttn in bg_bttns:
        bttn['bg'] = f'{main_color}'
        bttn['fg'] = 'white'
    for bttn in bttns_u_r:
        bttn['bg'] = 'black'
        bttn['fg'] = 'white'
    button_clear['bg'] = 'dark red'

print(button_5.cget('bg'))

def light():
    for bttn in bg_bttns:
        bttn['bg'] = 'SystemButtonFace'
        bttn['fg'] = 'black'
    for bttn in bttns_u_r:
        bttn['bg'] = 'light grey'
        bttn['fg'] = 'black'
    button_clear['bg'] = 'red'
    display['bg'] = 'white'
    

display.pack()


u_r_x = 0
u_r_y = 54
for bttn in bttns_u_r:
    bttn.place(x = u_r_x, y = u_r_y)
    u_r_x += 125


n_x = 0
n_y = 133
counter = 0
for bttn in bttns_n:
    bttn.place(x = n_x, y = n_y)
    n_x += 125
    counter += 1
    if counter == 3:
        n_x = 0
        n_y += 79
    if counter == 6:
        n_x = 0
        n_y += 79

l_r_x = 0
for bttn in bttns_l_r:
    bttn.place(x = l_r_x, y = 370)
    l_r_x += 125

s_y = 54
for bttn in bttns_s:
    bttn.place(x = 375, y = s_y)
    s_y += 79











sc.mainloop()

