from tkinter import *

window = Tk()


class MyWindow:
    def __init__(self, win):
        self.lblAdvMaterials = Label(win, text='Advance Materials')
        self.lblAdvTools = Label(win, text="Advance Tools")
        self.lblTianiumAlloy = Label(win, text='Titanium Alloy')
        self.lblBasicMaterials = Label(win, text='Basic Materials')
        self.lblBasicTools = Label(win, text='Basic Tools')
        self.lblRepair = Label(win, text='Repair Packets')
        self.MiningTools = Label(win, text='Mining Tools')
        self.lblSteel = Label(win, text='Steel Ingots')
        self.lblGraphene = Label(win, text='Graphene')
        self.lblTiIngot = Label(win, text='Titanium Ingots')
        self.lblSilicon = Label(win, text='Silicon')
        self.lblFuel = Label(win, text='Chemical Fuel')
        self.lblIron = Label(win, text='Iron')
        self.lblCarbon = Label(win, text='Carbon')
        self.lblTitanium = Label(win, text='Titanium')
        self.lblSilicate = Label(win, text='Silicate')
        self.lblWater = Label(win, text='Water')
        self.lblGold = Label(win, text='Gold')
        self.lblRover = Label(win, text='Rover')
        self.lblBuggy = Label(win, text='Buggy')
        self.lblTruck = Label(win, text='Truck')
        self.lblGoldBar = Label(win, text='Gold bar')
        self.lblCredit = Label(win, text='Credit')

        self.tAdvMaterials = Entry(bd=3, width=5)
        self.tAdvTools = Entry(bd=3, width=5)
        self.tTitaniumAlloy = Entry(bd=3, width=5)
        self.tBasicMaterial = Entry(bd=3, width=5)
        self.tBasicTools = Entry(bd=3, width=5)
        self.tRepair = Entry(bd=3, width=5)
        self.tMiningTools = Entry(bd=3, width=5)
        self.tSteel = Entry(bd=3, width=5)
        self.tGraphene = Entry(bd=3, width=5)
        self.tTiIngot = Entry(bd=3, width=5)
        self.tSilicon = Entry(bd=3, width=5)
        self.tFuel = Entry(bd=3, width=5)
        self.tIron = Entry(bd=3, width=5)
        self.tCarbon = Entry(bd=3, width=5)
        self.tTitanium = Entry(bd=3, width=5)
        self.tSilicate = Entry(bd=3, width=5)
        self.tWater = Entry(bd=3, width=5)
        self.tGold = Entry(bd=3, width=5)
        self.tRover = Entry(bd=3, width=5)
        self.tBuggy = Entry(bd=3, width=5)
        self.tTruck = Entry(bd=3, width=5)
        self.tGoldBar = Entry(bd=3, width=5)
        self.tCredit = Entry(bd=3, width=5)

        self.tAdvMaterials.insert(0, '0')
        self.tAdvTools.insert(0, '0')
        self.tTitaniumAlloy.insert(0, '0')
        self.tBasicMaterial.insert(0, '0')
        self.tBasicTools.insert(0, '0')
        self.tRepair.insert(0, '0')
        self.tMiningTools.insert(0, '0')
        self.tSteel.insert(0, '0')
        self.tGraphene.insert(0, '0')
        self.tTiIngot.insert(0, '0')
        self.tSilicon.insert(0, '0')
        self.tFuel.insert(0, '0')
        self.tIron.insert(0, '0')
        self.tCarbon.insert(0, '0')
        self.tTitanium.insert(0, '0')
        self.tSilicate.insert(0, '0')
        self.tWater.insert(0, '0')
        self.tGold.insert(0, '0')
        self.tRover.insert(0, '0')
        self.tBuggy.insert(0, '0')
        self.tTruck.insert(0, '0')
        self.tGoldBar.insert(0, '0')
        self.tCredit.insert(0, '0')

        self.lblAdvMaterials.grid(row=0, column=0)
        self.tAdvMaterials.grid(row=1, column=0)
        self.lblAdvTools.grid(row=0, column=1)
        self.tAdvTools.grid(row=1, column=1)
        self.lblTianiumAlloy.grid(column=0, row=2)
        self.tTitaniumAlloy.grid(column=0, row=3)
        self.lblBasicMaterials.grid(column=1, row=2)
        self.tBasicMaterial.grid(column=1, row=3)
        self.lblBasicTools.grid(column=2, row=2)
        self.tBasicTools.grid(column=2, row=3)
        self.lblRepair.grid(column=3, row=2)
        self.tRepair.grid(column=3, row=3)
        self.MiningTools.grid(column=4, row=2)
        self.tMiningTools.grid(column=4, row=3)
        self.lblSteel.grid(column=0, row=4)
        self.tSteel.grid(column=0, row=5)
        self.lblGraphene.grid(column=1, row=4)
        self.tGraphene.grid(column=1, row=5)
        self.lblTiIngot.grid(column=2, row=4)
        self.tTiIngot.grid(column=2, row=5)
        self.lblSilicon.grid(column=3, row=4)
        self.tSilicon.grid(column=3, row=5)
        self.lblFuel.grid(column=4, row=4)
        self.tFuel.grid(column=4, row=5)
        self.lblIron.grid(column=0, row=6)
        self.tIron.grid(column=0, row=7)
        self.lblCarbon.grid(column=1, row=6)
        self.tCarbon.grid(column=1, row=7)
        self.lblTitanium.grid(column=2, row=6)
        self.tTitanium.grid(column=2, row=7)
        self.lblSilicate.grid(column=3, row=6)
        self.tSilicate.grid(column=3, row=7)
        self.lblWater.grid(column=4, row=6)
        self.tWater.grid(column=4, row=7)
        self.lblGold.grid(column=6, row=6)
        self.tGold.grid(column=6, row=7)
        self.lblRover.grid(column=2, row=0)
        self.tRover.grid(column=2, row=1)
        self.lblBuggy.grid(column=3, row=0)
        self.tBuggy.grid(column=3, row=1)
        self.lblTruck.grid(column=4, row=0)
        self.tTruck.grid(column=4, row=1)
        self.lblGoldBar.grid(column=6, row=3)
        self.tGoldBar.grid(column=6, row=4)
        self.lblCredit.grid(column=6, row=0)
        self.tCredit.grid(column=6, row=1)

        self.bCalc = Button(win, text='Calculate', command=self.calc)
        self.bRst = Button(win, text='Reset', command=self.rst)
        self.bCalc.bind('<Button-1>', self.calc)
        self.bRst.bind('<Button-1>', self.rst)
        self.bCalc.grid(column=1, row=9)
        self.bRst.grid(column=3, row=9)

    def calc(self):
        adv_mat = int(self.tAdvMaterials.get())
        adv_tool = int(self.tAdvTools.get())
        ti_al = int(self.tTitaniumAlloy.get())
        bas_mat = int(self.tBasicMaterial.get())
        bas_tool = int(self.tBasicTools.get())
        repair = int(self.tRepair.get())
        min_tool = int(self.tMiningTools.get())
        steel = int(self.tSteel.get())
        graphene = int(self.tGraphene.get())
        ti_ing = int(self.tTiIngot.get())
        silicon = int(self.tSilicon.get())
        fuel = int(self.tFuel.get())
        rover = int(self.tRover.get())
        buggy = int(self.tBuggy.get())
        truck = int(self.tTruck.get())
        credit = int(self.tCredit.get())
        iron = carbon = titanium = silicate = water = gold = gold_ing = 0

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
        # tier 3 relation
        # adv_mat
        bas_mat += adv_mat
        graphene += adv_mat * 2
        ti_al += adv_mat * 3
        # adv_tool
        bas_tool += adv_tool
        graphene += adv_tool * 2
        ti_al += adv_tool

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
        silicate += silicon * 5
        # Fuel
        water += fuel * 2
        carbon += fuel * 2

        self.tIron.delete(0, 'end')
        self.tCarbon.delete(0, 'end')
        self.tTitanium.delete(0, 'end')
        self.tSilicate.delete(0, 'end')
        self.tWater.delete(0, 'end')
        self.tGold.delete(0, 'end')
        self.tSteel.delete(0, 'end')
        self.tGraphene.delete(0, 'end')
        self.tTiIngot.delete(0, 'end')
        self.tSilicon.delete(0, 'end')
        self.tGoldBar.delete(0, 'end')

        self.tIron.insert(0, str(iron))
        self.tCarbon.insert(0, str(carbon))
        self.tTitanium.insert(0, str(titanium))
        self.tSilicate.insert(0, str(silicate))
        self.tWater.insert(0, str(water))
        self.tGold.insert(0, str(gold))
        self.tSteel.insert(0, str(steel))
        self.tGraphene.insert(0, str(graphene))
        self.tTiIngot.insert(0, str(ti_ing))
        self.tSilicon.insert(0, str(silicon))
        self.tGoldBar.insert(0, str(gold_ing))

    def rst(self):
        self.tAdvTools.delete(0, 'end')
        self.tAdvMaterials.delete(0, 'end')
        self.tTitaniumAlloy.delete(0, 'end')
        self.tBasicMaterial.delete(0, 'end')
        self.tBasicTools.delete(0, 'end')
        self.tRepair.delete(0, 'end')
        self.tMiningTools.delete(0, 'end')
        self.tSteel.delete(0, 'end')
        self.tGraphene.delete(0, 'end')
        self.tTiIngot.delete(0, 'end')
        self.tSilicon.delete(0, 'end')
        self.tFuel.delete(0, 'end')
        self.tIron.delete(0, 'end')
        self.tCarbon.delete(0, 'end')
        self.tTitanium.delete(0, 'end')
        self.tSilicate.delete(0, 'end')
        self.tWater.delete(0, 'end')
        self.tGold.delete(0, 'end')
        self.tRover.delete(0, 'end')
        self.tBuggy.delete(0, 'end')
        self.tTruck.delete(0, 'end')
        self.tGoldBar.delete(0, 'end')
        self.tCredit.delete(0, 'end')
        self.tAdvMaterials.insert(0, '0')
        self.tAdvTools.insert(0, '0')
        self.tTitaniumAlloy.insert(0, '0')
        self.tBasicMaterial.insert(0, '0')
        self.tBasicTools.insert(0, '0')
        self.tRepair.insert(0, '0')
        self.tMiningTools.insert(0, '0')
        self.tSteel.insert(0, '0')
        self.tGraphene.insert(0, '0')
        self.tTiIngot.insert(0, '0')
        self.tSilicon.insert(0, '0')
        self.tFuel.insert(0, '0')
        self.tIron.insert(0, '0')
        self.tCarbon.insert(0, '0')
        self.tTitanium.insert(0, '0')
        self.tSilicate.insert(0, '0')
        self.tWater.insert(0, '0')
        self.tGold.insert(0, '0')
        self.tRover.insert(0, '0')
        self.tBuggy.insert(0, '0')
        self.tTruck.insert(0, '0')
        self.tGoldBar.insert(0, '0')
        self.tCredit.insert(0, '0')


mywin = MyWindow(window)
window.title('Resource Calculator')
window.geometry("500x220+10+10")
window.mainloop()
