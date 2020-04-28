
# Declare Variables
iron = carbon = titanium = silicate = water = gold = 0
steel = graphene = ti_ing = silicon = fuel = gold_ing = 0
ti_al = bas_mat = bas_tool = repair = min_tool = 0
rover = buggy = truck = 0

# Product
# rover
steel += 5 * rover
# buggy
steel += 10 * buggy
ti_ing += 2 * buggy
# truck
steel += 20*truck
ti_ing += 5*truck
graphene += 5*truck

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
ti_ing += bas_mat
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


base = [iron, carbon, titanium, silicate, water, gold]
tier_1 = [steel, graphene, ti_ing, silicon, fuel, gold_ing]
tier_2 = [ti_al, bas_mat, bas_tool, repair, min_tool]
print(ti_al, bas_mat, bas_tool, repair, min_tool)
print(steel, graphene, ti_ing, silicon, fuel, gold_ing)
print(iron, carbon, titanium, silicate, water, gold)
