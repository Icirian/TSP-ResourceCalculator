from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='Titanium Alloy')
        self.lbl2 = Label(win, text='Basic Materials')
        self.lbl3 = Label(win, text='Basic Tools')
        self.lbl4 = Label(win, text='Repair Packets')
        self.lbl5 = Label(win, text='Mining Tools')
        self.lbl6 = Label(win, text='Steel Ingots')
        self.lbl7 = Label(win, text='Graphene')
        self.lbl8 = Label(win, text='Titanium Ingots')
        self.lbl9 = Label(win, text='Silicon')
        self.lbl10 = Label(win, text='Chemical Fuel')
        self.lbl11 = Label(win, text='Iron')
        self.lbl12 = Label(win, text='Carbon')
        self.lbl13 = Label(win, text='Titanium')
        self.lbl14 = Label(win, text='Silicate')
        self.lbl15 = Label(win, text='Water')
        self.lbl16 = Label(win, text='Gold')
        self.lbl17 = Label(win, text='Rover')
        self.lbl18 = Label(win, text='Buggy')
        self.lbl19 = Label(win, text='Truck')
        self.lbl20 = Label(win, text='Steel Ingots')
        self.lbl21 = Label(win, text='Graphene')
        self.lbl22 = Label(win, text='Titanium Ingots')
        self.lbl23 = Label(win, text='Silicon')
        self.lbl25 = Label(win, text='Gold bar')
        self.lbl26 = Label(win, text='Credit')

        self.t1 = Entry(bd=3)
        self.t2 = Entry(bd=3)
        self.t3 = Entry(bd=3)
        self.t4 = Entry(bd=3)
        self.t5 = Entry(bd=3)
        self.t6 = Entry(bd=3)
        self.t7 = Entry(bd=3)
        self.t8 = Entry(bd=3)
        self.t9 = Entry(bd=3)
        self.t10 = Entry(bd=3)
        self.t11 = Entry(bd=3)
        self.t12 = Entry(bd=3)
        self.t13 = Entry(bd=3)
        self.t14 = Entry(bd=3)
        self.t15 = Entry(bd=3)
        self.t16 = Entry(bd=3)
        self.t17 = Entry(bd=3)
        self.t18 = Entry(bd=3)
        self.t19 = Entry(bd=3)
        self.t20 = Entry(bd=3)
        self.t21 = Entry(bd=3)
        self.t22 = Entry(bd=3)
        self.t23 = Entry(bd=3)
        self.t25 = Entry(bd=3)
        self.t26 = Entry(bd=3)

        self.t1.insert(0, '0')
        self.t2.insert(0, '0')
        self.t3.insert(0, '0')
        self.t4.insert(0, '0')
        self.t5.insert(0, '0')
        self.t6.insert(0, '0')
        self.t7.insert(0, '0')
        self.t8.insert(0, '0')
        self.t9.insert(0, '0')
        self.t10.insert(0, '0')
        self.t11.insert(0, '0')
        self.t12.insert(0, '0')
        self.t13.insert(0, '0')
        self.t14.insert(0, '0')
        self.t15.insert(0, '0')
        self.t16.insert(0, '0')
        self.t17.insert(0, '0')
        self.t18.insert(0, '0')
        self.t19.insert(0, '0')
        self.t20.insert(0, '0')
        self.t21.insert(0, '0')
        self.t22.insert(0, '0')
        self.t23.insert(0, '0')
        self.t25.insert(0, '0')
        self.t26.insert(0, '0')

        self.btn1 = Button(win, text='Calc')
        self.lbl1.place(x=30, y=30)
        self.t1.place(x=40, y=60, width=50)
        self.lbl2.place(x=120, y=30)
        self.t2.place(x=130, y=60, width=50)
        self.lbl3.place(x=220, y=30)
        self.t3.place(x=220, y=60, width=50)
        self.lbl4.place(x=300, y=30)
        self.t4.place(x=310, y=60, width=50)
        self.lbl5.place(x=390, y=30)
        self.t5.place(x=400, y=60, width=50)
        self.lbl6.place(x=30, y=90)
        self.t6.place(x=40, y=120, width=50)
        self.lbl7.place(x=130, y=90)
        self.t7.place(x=130, y=120, width=50)
        self.lbl8.place(x=200, y=90)
        self.t8.place(x=220, y=120, width=50)
        self.lbl9.place(x=310, y=90)
        self.t9.place(x=310, y=120, width=50)
        self.lbl10.place(x=380, y=90)
        self.t10.place(x=400, y=120, width=50)
        self.lbl11.place(x=50, y=300)
        self.t11.place(x=40, y=330, width=50)
        self.lbl12.place(x=140, y=300)
        self.t12.place(x=130, y=330, width=50)
        self.lbl13.place(x=230, y=300)
        self.t13.place(x=220, y=330, width=50)
        self.lbl14.place(x=320, y=300)
        self.t14.place(x=310, y=330, width=50)
        self.lbl15.place(x=410, y=300)
        self.t15.place(x=400, y=330, width=50)
        self.lbl16.place(x=520, y=300)
        self.t16.place(x=510, y=330, width=50)
        self.lbl17.place(x=515, y=30)
        self.t17.place(x=510, y=60, width=50)
        self.lbl18.place(x=515, y=90)
        self.t18.place(x=510, y=120, width=50)
        self.lbl19.place(x=515, y=150)
        self.t19.place(x=510, y=180, width=50)
        self.lbl20.place(x=30, y=240)
        self.t20.place(x=40, y=270, width=50)
        self.lbl21.place(x=130, y=240)
        self.t21.place(x=130, y=270, width=50)
        self.lbl22.place(x=200, y=240)
        self.t22.place(x=220, y=270, width=50)
        self.lbl23.place(x=310, y=240)
        self.t23.place(x=310, y=270, width=50)
        self.lbl25.place(x=515, y=240)
        self.t25.place(x=510, y=270, width=50)
        self.lbl26.place(x=585, y=30)
        self.t26.place(x=580, y=60, width=50)

        self.b1 = Button(win, text='Calculate', command=self.calc)
        self.b2 = Button(win, text='Reset', command=self.rst)
        self.b1.bind('<Button-1>', self.calc)
        self.b2.bind('<Button-1>', self.rst)
        self.b1.place(x=150, y=180)
        self.b2.place(x=300, y=180)

    def calc(self):
        self.t11.delete(0, 'end')
        self.t12.delete(0, 'end')
        self.t13.delete(0, 'end')
        self.t14.delete(0, 'end')
        self.t15.delete(0, 'end')
        self.t16.delete(0, 'end')
        self.t20.delete(0, 'end')
        self.t21.delete(0, 'end')
        self.t22.delete(0, 'end')
        self.t23.delete(0, 'end')
        self.t25.delete(0, 'end')
        ti_al = int(self.t1.get())
        bas_mat = int(self.t2.get())
        bas_tool = int(self.t3.get())
        repair = int(self.t4.get())
        min_tool = int(self.t5.get())
        steel = int(self.t6.get())
        graphene = int(self.t7.get())
        ti_ing = int(self.t8.get())
        silicon = int(self.t9.get())
        fuel = int(self.t10.get())
        rover = int(self.t17.get())
        buggy = int(self.t18.get())
        truck = int(self.t19.get())
        credit = int(self.t26.get())
        iron = carbon = titanium = silicate = water = gold = gold_ing= 0

        # Product
        # rover
        steel += 5 * rover
        # buggy
        steel += 10 * buggy
        ti_ing += 2 * buggy
        # truck

        # Credit
        gold_ing += credit / 150
        gold += gold_ing * 5
        # tier_2 relation
        # repair
        steel += repair
        ti_ing += repair
        silicon += repair
        # titanium Alloy
        steel += ti_al
        ti_ing += ti_al
        silicon += ti_al
        # Basic Material
        steel += bas_mat * 3
        silicate += bas_mat * 5
        ti_ing = bas_mat
        # Basic Tools
        steel += 2 * bas_tool
        graphene += 2 * bas_tool
        ti_ing += bas_tool
        # mining tools
        steel += 3 * min_tool
        graphene += min_tool
        ti_ing += min_tool

        # tier_1 relation
        # Steel
        iron += steel * 5
        carbon += steel
        # Graphene
        carbon += graphene * 5
        # Titanium ingot
        titanium += ti_ing * 5
        # Silicon
        silicon += silicate * 5
        # Fuel
        water += fuel * 2
        carbon += fuel * 2

        self.t11.insert(0, str(iron))
        self.t12.insert(0, str(carbon))
        self.t13.insert(0, str(titanium))
        self.t14.insert(0, str(silicon))
        self.t15.insert(0, str(water))
        self.t16.insert(0, str(gold))
        self.t20.insert(0, str(steel))
        self.t21.insert(0, str(graphene))
        self.t22.insert(0, str(ti_ing))
        self.t23.insert(0, str(silicate))
        self.t25.insert(0, str(gold_ing))


    def rst(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')
        self.t6.delete(0, 'end')
        self.t7.delete(0, 'end')
        self.t8.delete(0, 'end')
        self.t9.delete(0, 'end')
        self.t10.delete(0, 'end')
        self.t11.delete(0, 'end')
        self.t12.delete(0, 'end')
        self.t13.delete(0, 'end')
        self.t14.delete(0, 'end')
        self.t15.delete(0, 'end')
        self.t16.delete(0, 'end')
        self.t17.delete(0, 'end')
        self.t18.delete(0, 'end')
        self.t19.delete(0, 'end')
        self.t20.delete(0, 'end')
        self.t21.delete(0, 'end')
        self.t22.delete(0, 'end')
        self.t23.delete(0, 'end')
        self.t25.delete(0, 'end')
        self.t26.delete(0, 'end')
        self.t1.insert(0, '0')
        self.t2.insert(0, '0')
        self.t3.insert(0, '0')
        self.t4.insert(0, '0')
        self.t5.insert(0, '0')
        self.t6.insert(0, '0')
        self.t7.insert(0, '0')
        self.t8.insert(0, '0')
        self.t9.insert(0, '0')
        self.t10.insert(0, '0')
        self.t11.insert(0, '0')
        self.t12.insert(0, '0')
        self.t13.insert(0, '0')
        self.t14.insert(0, '0')
        self.t15.insert(0, '0')
        self.t16.insert(0, '0')
        self.t17.insert(0, '0')
        self.t18.insert(0, '0')
        self.t19.insert(0, '0')
        self.t20.insert(0, '0')
        self.t21.insert(0, '0')
        self.t22.insert(0, '0')
        self.t23.insert(0, '0')
        self.t25.insert(0, '0')
        self.t26.insert(0, '0')


window = Tk()
mywin = MyWindow(window)
window.title('Resource Calculator')
window.geometry("700x400+10+10")
window.mainloop()
