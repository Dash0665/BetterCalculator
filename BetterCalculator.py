from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()


    def init_window(self):
        self.master.title("Basic Calculator")

        self.pack(fill=BOTH, expand=1)


        def clear_text():
            e.delete(0, END)

        def set_text(text):
            global ans
            if '=' in e.get() and ans in e.get() and text != '=':
                e.delete(0, END)

                if text == ' + ' or ' - ' or  ' * ' or ' / ':
                    e.insert(END,ans)

            e.insert(END, text)
            return


        operation = StringVar()
        e = Entry(self, textvariable=operation)
        e.grid(row=1, column=1, columnspan=4, sticky=W+E, padx = 2, pady = 2, ipadx = 10, ipady = 10)


        #Menu bar
        menu = Menu(self.master)
        self.master.config(menu=menu)

        #File menu
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        #Edit menu
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)



        #Oporator Buttons
        cButton = Button(self, text='C', command=lambda:clear_text())
        cButton.grid(row=2, column=4, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        plusButton = Button(self, text='+', command=lambda:set_text(' + '))
        plusButton.grid(row=3, column=4, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        minusButton = Button(self, text='-', command=lambda:set_text(' - '))
        minusButton.grid(row=4, column=4, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        multiButton = Button(self, text='x', command=lambda:set_text(' * '))
        multiButton.grid(row=5, column=4, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        divideButton = Button(self, text='/', command=lambda:set_text(' / '))
        divideButton.grid(row=5, column=3, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        equalButton = Button(self, text="=", command=lambda: equal_operation())
        equalButton.grid(row=6, column=1, columnspan=4, sticky=W+E, padx = 2, pady = 2, ipadx = 10, ipady = 10)


        #number buttons
        oneButton = Button(self, text='1', command=lambda:set_text('1'))
        oneButton.grid(row=2, column=1, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        twoButton = Button(self, text='2', command=lambda:set_text('2'))
        twoButton.grid(row=2, column=2, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        threeButton = Button(self, text='3', command=lambda:set_text('3'))
        threeButton.grid(row=2, column=3, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        fourButton = Button(self, text='4', command=lambda:set_text('4'))
        fourButton.grid(row=3, column=1, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        fiveButton = Button(self, text='5', command=lambda:set_text('5'))
        fiveButton.grid(row=3, column=2, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        sixButton = Button(self, text='6', command=lambda:set_text('6'))
        sixButton.grid(row=3, column=3, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        sevenButton = Button(self, text='7', command=lambda:set_text('7'))
        sevenButton.grid(row=4, column=1, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        eightButton = Button(self, text='8', command=lambda:set_text('8'))
        eightButton.grid(row=4, column=2, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        nineButton = Button(self, text='9', command=lambda:set_text('9'))
        nineButton.grid(row=4, column=3, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        zeroButton = Button(self, text='0', command=lambda:set_text('0'))
        zeroButton.grid(row=5, column=2, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        dotButton = Button(self, text='.', command=lambda:set_text('.'))
        dotButton.grid(row=5, column=1, padx = 2, pady = 2, ipadx = 10, ipady = 10)

        def equal_operation():
            global ans
            ans = str(eval(operation.get()))
            set_text(' = ')
            set_text(ans)

    def client_exit(self):
        exit()

root = Tk()

app = Window(root)

root.mainloop()



'''
print('Answer: ' + str(eval(input('Enter equation: '))))
'''