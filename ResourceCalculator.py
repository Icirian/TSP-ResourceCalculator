from tkinter import *


class MyWindow:
    def __init__(self, win):
        self.lblTianiumAlloy = Label(win, text='Titanium Alloy')
        self.lblBasicMaterials = Label(win, text='Basic Materials')
        self.lblBasicTools = Label(win, text='Basic Tools')
        self.lblRepair = Label(win, text='Repair Packets')
        self.MiningTools = Label(win, text='Mining Tools')
        self.lbl6 = Label(win, text='Steel Ingots')
        self.lbl7 = Label(win, text='Graphene')
        self.lbl8 = Label(win, text='Titanium Ingots')
        self.lbl9 = Label(win, text='Silicon')
        self.lbl10 = Label(win, text='Chemical Fuel')
        self.lblIron = Label(win, text='Iron')
        self.lblCarbon = Label(win, text='Carbon')
        self.lblTitanium = Label(win, text='Titanium')
        self.lblSilicon = Label(win, text='Silicate')
        self.lblWater = Label(win, text='Water')
        self.lblGold = Label(win, text='Gold')
        self.lblRover = Label(win, text='Rover')
        self.lblBuggy = Label(win, text='Buggy')
        self.lblTruck = Label(win, text='Truck')
        self.lbl20 = Label(win, text='Steel Ingots')
        self.lbl21 = Label(win, text='Graphene')
        self.lbl22 = Label(win, text='Titanium Ingots')
        self.lbl23 = Label(win, text='Silicon')
        self.lblGoldBar = Label(win, text='Gold bar')
        self.lblCredit = Label(win, text='Credit')

        self.tTitaniumAlloy = Entry(bd=3)
        self.tBasicMaterial = Entry(bd=3)
        self.tBasicTools = Entry(bd=3)
        self.tRepair = Entry(bd=3)
        self.tMiningTools = Entry(bd=3)
        self.t6 = Entry(bd=3)
        self.t7 = Entry(bd=3)
        self.t8 = Entry(bd=3)
        self.t9 = Entry(bd=3)
        self.t10 = Entry(bd=3)
        self.tIron = Entry(bd=3)
        self.tCarbon = Entry(bd=3)
        self.tTitanium = Entry(bd=3)
        self.tSilicon = Entry(bd=3)
        self.tWater = Entry(bd=3)
        self.tGold = Entry(bd=3)
        self.tRover = Entry(bd=3)
        self.tBuggy = Entry(bd=3)
        self.tTruck = Entry(bd=3)
        self.t20 = Entry(bd=3)
        self.t21 = Entry(bd=3)
        self.t22 = Entry(bd=3)
        self.t23 = Entry(bd=3)
        self.tGoldBar = Entry(bd=3)
        self.tCredit = Entry(bd=3)

        self.tTitaniumAlloy.insert(0, '0')
        self.tBasicMaterial.insert(0, '0')
        self.tBasicTools.insert(0, '0')
        self.tRepair.insert(0, '0')
        self.tMiningTools.insert(0, '0')
        self.t6.insert(0, '0')
        self.t7.insert(0, '0')
        self.t8.insert(0, '0')
        self.t9.insert(0, '0')
        self.t10.insert(0, '0')
        self.tIron.insert(0, '0')
        self.tCarbon.insert(0, '0')
        self.tTitanium.insert(0, '0')
        self.tSilicon.insert(0, '0')
        self.tWater.insert(0, '0')
        self.tGold.insert(0, '0')
        self.tRover.insert(0, '0')
        self.tBuggy.insert(0, '0')
        self.tTruck.insert(0, '0')
        self.t20.insert(0, '0')
        self.t21.insert(0, '0')
        self.t22.insert(0, '0')
        self.t23.insert(0, '0')
        self.tGoldBar.insert(0, '0')
        self.tCredit.insert(0, '0')

        self.btn1 = Button(win, text='Calc')
        self.lblTianiumAlloy.place(x=30, y=30)
        self.tTitaniumAlloy.place(x=40, y=60, width=50)
        self.lblBasicMaterials.place(x=120, y=30)
        self.tBasicMaterial.place(x=130, y=60, width=50)
        self.lblBasicTools.place(x=220, y=30)
        self.tBasicTools.place(x=220, y=60, width=50)
        self.lblRepair.place(x=300, y=30)
        self.tRepair.place(x=310, y=60, width=50)
        self.MiningTools.place(x=390, y=30)
        self.tMiningTools.place(x=400, y=60, width=50)
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
        self.lblIron.place(x=50, y=300)
        self.tIron.place(x=40, y=330, width=50)
        self.lblCarbon.place(x=140, y=300)
        self.tCarbon.place(x=130, y=330, width=50)
        self.lblTitanium.place(x=230, y=300)
        self.tTitanium.place(x=220, y=330, width=50)
        self.lblSilicon.place(x=320, y=300)
        self.tSilicon.place(x=310, y=330, width=50)
        self.lblWater.place(x=410, y=300)
        self.tWater.place(x=400, y=330, width=50)
        self.lblGold.place(x=520, y=300)
        self.tGold.place(x=510, y=330, width=50)
        self.lblRover.place(x=515, y=30)
        self.tRover.place(x=510, y=60, width=50)
        self.lblBuggy.place(x=515, y=90)
        self.tBuggy.place(x=510, y=120, width=50)
        self.lblTruck.place(x=515, y=150)
        self.tTruck.place(x=510, y=180, width=50)
        self.lbl20.place(x=30, y=240)
        self.t20.place(x=40, y=270, width=50)
        self.lbl21.place(x=130, y=240)
        self.t21.place(x=130, y=270, width=50)
        self.lbl22.place(x=200, y=240)
        self.t22.place(x=220, y=270, width=50)
        self.lbl23.place(x=310, y=240)
        self.t23.place(x=310, y=270, width=50)
        self.lblGoldBar.place(x=515, y=240)
        self.tGoldBar.place(x=510, y=270, width=50)
        self.lblCredit.place(x=585, y=30)
        self.tCredit.place(x=580, y=60, width=50)

        self.bCalc = Button(win, text='Calculate', command=self.calc)
        self.bRst = Button(win, text='Reset', command=self.rst)
        self.bCalc.bind('<Button-1>', self.calc)
        self.bRst.bind('<Button-1>', self.rst)
        self.bCalc.place(x=150, y=180)
        self.bRst.place(x=300, y=180)

    def calc(self):
        self.tIron.delete(0, 'end')
        self.tCarbon.delete(0, 'end')
        self.tTitanium.delete(0, 'end')
        self.tSilicon.delete(0, 'end')
        self.tWater.delete(0, 'end')
        self.tGold.delete(0, 'end')
        self.t20.delete(0, 'end')
        self.t21.delete(0, 'end')
        self.t22.delete(0, 'end')
        self.t23.delete(0, 'end')
        self.tGoldBar.delete(0, 'end')
        ti_al = int(self.tTitaniumAlloy.get())
        bas_mat = int(self.tBasicMaterial.get())
        bas_tool = int(self.tBasicTools.get())
        repair = int(self.tRepair.get())
        min_tool = int(self.tMiningTools.get())
        steel = int(self.t6.get())
        graphene = int(self.t7.get())
        ti_ing = int(self.t8.get())
        silicon = int(self.t9.get())
        fuel = int(self.t10.get())
        rover = int(self.tRover.get())
        buggy = int(self.tBuggy.get())
        truck = int(self.tTruck.get())
        credit = int(self.tCredit.get())
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

        self.tIron.insert(0, str(iron))
        self.tCarbon.insert(0, str(carbon))
        self.tTitanium.insert(0, str(titanium))
        self.tSilicon.insert(0, str(silicon))
        self.tWater.insert(0, str(water))
        self.tGold.insert(0, str(gold))
        self.t20.insert(0, str(steel))
        self.t21.insert(0, str(graphene))
        self.t22.insert(0, str(ti_ing))
        self.t23.insert(0, str(silicate))
        self.tGoldBar.insert(0, str(gold_ing))


    def rst(self):
        self.tTitaniumAlloy.delete(0, 'end')
        self.tBasicMaterial.delete(0, 'end')
        self.tBasicTools.delete(0, 'end')
        self.tRepair.delete(0, 'end')
        self.tMiningTools.delete(0, 'end')
        self.t6.delete(0, 'end')
        self.t7.delete(0, 'end')
        self.t8.delete(0, 'end')
        self.t9.delete(0, 'end')
        self.t10.delete(0, 'end')
        self.tIron.delete(0, 'end')
        self.tCarbon.delete(0, 'end')
        self.tTitanium.delete(0, 'end')
        self.tSilicon.delete(0, 'end')
        self.tWater.delete(0, 'end')
        self.tGold.delete(0, 'end')
        self.tRover.delete(0, 'end')
        self.tBuggy.delete(0, 'end')
        self.tTruck.delete(0, 'end')
        self.t20.delete(0, 'end')
        self.t21.delete(0, 'end')
        self.t22.delete(0, 'end')
        self.t23.delete(0, 'end')
        self.tGoldBar.delete(0, 'end')
        self.tCredit.delete(0, 'end')
        self.tTitaniumAlloy.insert(0, '0')
        self.tBasicMaterial.insert(0, '0')
        self.tBasicTools.insert(0, '0')
        self.tRepair.insert(0, '0')
        self.tMiningTools.insert(0, '0')
        self.t6.insert(0, '0')
        self.t7.insert(0, '0')
        self.t8.insert(0, '0')
        self.t9.insert(0, '0')
        self.t10.insert(0, '0')
        self.tIron.insert(0, '0')
        self.tCarbon.insert(0, '0')
        self.tTitanium.insert(0, '0')
        self.tSilicon.insert(0, '0')
        self.tWater.insert(0, '0')
        self.tGold.insert(0, '0')
        self.tRover.insert(0, '0')
        self.tBuggy.insert(0, '0')
        self.tTruck.insert(0, '0')
        self.t20.insert(0, '0')
        self.t21.insert(0, '0')
        self.t22.insert(0, '0')
        self.t23.insert(0, '0')
        self.tGoldBar.insert(0, '0')
        self.tCredit.insert(0, '0')


window = Tk()
mywin = MyWindow(window)
window.title('Resource Calculator')
window.geometry("700x400+10+10")
window.mainloop()
