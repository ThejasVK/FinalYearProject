from tkinter import *
import tkinter as tk

root = Tk()
root.geometry('1000x800')
root.title("TOP Predictor")
root.iconbitmap(r'project.ico')
v = tk.IntVar()
w = tk.IntVar()

#main title
text = Label(root,
             text = 'predictor model',
             font= ('Helvetica', 28),
             bd=1, relief='sunken',
             justify='center')
text.pack(pady=20, ipady=5, ipadx=5)
#select vegetable
text1 = Label(root,
             text = 'Select Vegetable',
             font= ('Helvetica', 18),
             bd=5,
             justify='left')
text1.place(x=100, y=120)
#radio buttons for selecting TOP
radiobutton1 = Radiobutton(root, text="Tomato", font= ('Helvetica', 14), variable=v, value=0, command = lambda: print(v.get()))
radiobutton2 = Radiobutton(root, text="Onion", variable=v, value=1, font= ('Helvetica', 14),command = lambda: print(v.get()))
radiobutton3 = Radiobutton(root, text="Potato", variable=v, value=2, font= ('Helvetica', 14),command = lambda: print(v.get()))
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
radiobutton1.place(x=100, y=160)
radiobutton2.place(x=100, y=190)
radiobutton3.place(x=100, y=220)

#select target
text2 = Label(root,
             text = 'Choose Target for Prediction',
             font= ('Helvetica', 18),
             bd=5,
              justify='left')
text2.place(x=350, y=120)
#radio buttons for choosing target
button1 = Radiobutton(root, text="Production in Quintal", variable=w, value=0, font= ('Helvetica', 14),command = lambda: print(v.get()))
button2 = Radiobutton(root, text="Demand Count", variable=w, value=1, font= ('Helvetica', 14),command = lambda: print(v.get()))
button3 = Radiobutton(root, text="Max Price (in Rs)", variable=w, value=2, font= ('Helvetica', 14),command = lambda: print(v.get()))
button1.pack()
button2.pack()
button3.pack()
button1.place(x=350, y=160)
button2.place(x=350, y=190)
button3.place(x=350, y=220)


#select year
text3 = Label(root,
             text = 'Choose Year',
             font= ('Helvetica', 18),
             bd=5,
              justify='left')
text3.place(x=725, y=120)

#menu for year
mb = Menubutton(root, text='Year', font= ('Helvetica', 14),)
mb.menu = Menu(mb)
mb["menu"]= mb.menu

mb.menu.add_command(label='option 1', font= ('Helvetica', 14),command=lambda:print('this is option 1'))
mb.menu.add_command(label='option 2', font= ('Helvetica', 14),command=lambda:print('this is option 2'))
mb.menu.add_command(label='option 3', font= ('Helvetica', 14),command=lambda:print('this is option 3'))
mb.pack()
mb.place(x=725, y=160)

#Prediction
myButton = Button(root, text= 'Click here for Prediction', font= ('Helvetica', 14),command=lambda:print('predicted' ))
myButton.pack()
myButton.place(x=450, y= 260)

text4 = Label(root,
             text = 'Production         :',
             font= ('Helvetica', 18),
             bd=5,
             justify='left')
text4.place(x=250, y=310)

text5 = Label(root,
             text = 'District               :',
             font= ('Helvetica', 18),
             bd=5,
             justify='left')
text5.place(x=250, y=360)

text6 = Label(root,
             text = 'Max Price(in Rs) :',
             font= ('Helvetica', 18),
             bd=5,
             justify='left')
text6.place(x=250, y=410)

textbox1= Text(root, width=40, height=1.5, font=('Helvetica'))
textbox2= Text(root, width=40, height=1.5, font=('Helvetica'))
textbox3= Text(root, width=40, height=1.5, font=('Helvetica'))
textbox1.pack(pady=20)
textbox2.pack(pady=20)
textbox3.pack(pady=20)
textbox1.place(x=450,y=310)
textbox2.place(x=450,y=360)
textbox3.place(x=450,y=410)

root.mainloop()
# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
#
#
# class SpartanApp(App):
#     def build(self):
#
#         return Label(text='this is spartaa!')
#
# if __name__=="__main__":
#     SpartanApp().run()
