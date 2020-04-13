import normal 
import binomial
from tkinter import *
from tkinter import messagebox
from prettytable import PrettyTable

lst=[]
def clear():
    if len(lst) != 0:
      for i in lst:
          i.destroy()
    lst.clear()

def gui_manage():
    info = {}
    clear()

    if not lb.get(): min=0
    else: min =lb.get()

    Label(text="Початкова таблиця").grid(row=0, column=2, sticky=W+E)

    if v.get() == 1:
       info = binomial.info_func(int(amount.get()),int(min),int(rb.get()),float(s.get()))

       start = PrettyTable()
       start.add_column('xi', info['xi_copy'])
       start.add_column('mi', info['mi_copy'])
       start.add_column('pi', info['pi_copy'])
       start.add_column('n*pi', info['n*pi_copy'])
      
       str_table = start.get_string()
       tbl_txt = Text(width=str_table.index('\n'), height=str_table.count('\n')+1)
       lst.append(tbl_txt)
       tbl_txt.insert(END, start)
       last_row=str_table.count('\n')-3
       tbl_txt.grid(row=1, column=2,rowspan=last_row,padx=(0,10), sticky=W+E)
       tbl_txt.config(state=DISABLED)
       last_row+=1

       Label(text='Кінцева таблиця' ).grid(row=last_row, column=2, sticky=W+E)
       last_row+=1
       merged = PrettyTable()
       merged.add_column('xi', info['xi'])
       merged.add_column('mi', info['mi'])
       merged.add_column('pi', info['pi'])
       merged.add_column('n*pi', info['n*pi'])
       str_table = merged.get_string()
       tbl_txt = Text(width=str_table.index('\n'), height=str_table.count('\n')+1)
       lst.append(tbl_txt)
       tbl_txt.insert(END, merged)
       tbl_txt.grid(row=last_row, column=2,rowspan=str_table.count('\n')-2,padx=(0,10), sticky=W+E)
       tbl_txt.config(state=DISABLED)
       last_row+=str_table.count('\n')

       lst.append(Label(text='x^2 емпіричне = {}'.format(info['x^2emp'])))
       lst[2].grid(row=last_row, column=2, sticky=W)
       last_row+=1

       lst.append(Label(text='x^2 критичне = {}'.format(info['x^2kr'])))
       lst[3].grid(row=last_row, column=2, sticky=W)
       last_row+=1

       label_text=StringVar()
       if info['x^2emp']<info['x^2kr']: label_text.set('Так як x^2 емпіричне < x^2 критичного, гіпотезу приймаємо')
       else: label_text.set('Так як x^2 емпіричне > x^2 критичного, гіпотезу відхиляємло')
       lst.append(Label(textvariable=label_text))
       lst[4].grid(row=last_row, column=2, columnspan=2, sticky=W)
       last_row+=1

    elif v.get()==2: 
       info = normal.info_func(int(amount.get()),int(min),int(rb.get()),float(s.get()))

       start = PrettyTable()
       start.add_column('(zi-1 ; zi]', info['i-vals_old'])
       start.add_column('zi''', info['zi_copy'])
       start.add_column('mi', info['mi_copy'])
       start.add_column('pi', info['pi_copy'])
       start.add_column('n*pi', info['n*pi_copy'])
      
       str_table = start.get_string()
       tbl_txt = Text(width=str_table.index('\n'), height=str_table.count('\n')+1)
       lst.append(tbl_txt)
       tbl_txt.insert(END, start)
       last_row=str_table.count('\n')-3
       tbl_txt.grid(row=1, column=2,rowspan=last_row,padx=(0,10), sticky=W+E)
       tbl_txt.config(state=DISABLED)
       last_row+=1
 
       lst.append(Label(text='Кінцева таблиця' ))
       lst[1].grid(row=last_row, column=2, sticky=W+E)
       last_row+=1
       merged = PrettyTable()
       merged.add_column('(zi-1 ; zi]', info['i-vals_new'])
       merged.add_column('zi''', info['t']['zi'])
       merged.add_column('mi', info['t']['mi'])
       merged.add_column('pi', info['t']['pi'])
       merged.add_column('n*pi', info['t']['n*pi'])
     
       str_table = merged.get_string()
       tbl_txt = Text(width=str_table.index('\n'), height=str_table.count('\n')+1)
       lst.append(tbl_txt)
       tbl_txt.insert(END, merged)
       tbl_txt.grid(row=last_row, column=2,rowspan=str_table.count('\n')-3,padx=(0,10), sticky=W+E)
       tbl_txt.config(state=DISABLED)
       last_row+=str_table.count('\n')
       
       last_row+=1
       lst.append(Label(text='x^2 емпіричне = {}'.format(info['x^2emp'])))
       lst[3].grid(row=last_row, column=2, sticky=W)
       last_row+=1

       lst.append(Label(text='x^2 критичне = {}'.format(info['x^2kr'])))
       lst[4].grid(row=last_row, column=2, sticky=W)
       last_row+=1

       label_text=StringVar()
       if info['x^2emp']<info['x^2kr']: label_text.set('Так як x^2 емпіричне < x^2 критичного, гіпотезу приймаємо')
       else: label_text.set('Так як x^2 емпіричне > x^2 критичного, гіпотезу відхиляємло')
       lst.append(Label(textvariable=label_text,  ))
       lst[5].grid(row=last_row, column=2, columnspan=2, sticky=W)
    else: 
        messagebox.showerror(title="Помилка розподілу", message="Оберіть тип розподілу")
        return


root = Tk()
root.title("Математична статистика")
v = IntVar() 
Radiobutton(root, text='Біномний розподіл', variable=v, value=1).grid(row=0,column=0)
Radiobutton(root, text='Нормальний розподіл', variable=v, value=2).grid(row=0,column=1) 

amount_label = Label(root, text = "Кількість").grid(row = 1, column = 0, pady=5, padx=10)  
amount = Entry(root)
amount.grid(row = 1, column = 1, pady=5, padx=10)  

lb_label = Label(root, text = "Ліва межа").grid(row = 2, column = 0, pady=5, padx=10) 
lb = Entry(root)
lb.grid(row = 2, column = 1, pady=5, padx=10)  


rb_label = Label(root, text = "Права межа").grid(row = 3, column = 0, pady=5, padx=10)  
rb = Entry(root)
rb.grid(row = 3, column = 1, pady=5, padx=10)  

sig_label = Label(root, text = "Рівень значущості").grid(row = 4, column = 0, pady=5, padx=10)  
s = DoubleVar(value=0.05) 
Radiobutton(root, text='0.001', variable=s, value=0.001).grid(row=5,column=0)
Radiobutton(root, text='0.01', variable=s, value=0.01).grid(row=6,column=0)
Radiobutton(root, text='0.05', variable=s, value=0.05).grid(row=7,column=0)

submit = Button(root,text='Порахувати', command=gui_manage)
submit.grid(row=8,column=0,columnspan=2, pady=5, padx=5, sticky=E + W)
root.mainloop()

