import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


incoms = ctrl.Antecedent(np.arange(0, 150, 1), 'incoms')
charges = ctrl.Antecedent(np.arange(0, 150, 1), 'charges')
economy = ctrl.Antecedent(np.arange(0, 100, 1), 'economy')

#accamulation = ctrl.Consequent(np.arange(-10, 100, 1), 'accamulation')
accamulation = ctrl.Consequent(np.arange(-20, 50, 1), 'accamulation')


# экономическая обстановка
economy['bad'] = fuzz.gaussmf(economy.universe, 0,15)#25
economy['average'] = fuzz.gaussmf(economy.universe,50,15)
economy['good'] = fuzz.gaussmf(economy.universe, 100,15) #100 25

# доходы
incoms['low'] = fuzz.gaussmf(incoms.universe, 0,15)
incoms['medium'] = fuzz.gaussmf(incoms.universe, 60,15)
incoms['high'] = fuzz.pimf(incoms.universe,70,100,150,150)

# расходы
charges['low'] = fuzz.pimf(charges.universe, 0,1,15,25)
charges['medium'] = fuzz.pimf(charges.universe, 25,50,70,95)
charges['high'] = fuzz.pimf(charges.universe, 70,100,150,150)

# накопления
#accamulation['dept'] = fuzz.pimf(accamulation.universe, -10,-9,0,5)
#accamulation['low'] = fuzz.trimf(accamulation.universe, [0,5,10])
#accamulation['medium'] = fuzz.pimf(accamulation.universe, 0,20,50,70)
#accamulation['high'] = fuzz.pimf(accamulation.universe, 50,70,100,100)

# накопления
accamulation['dept'] = fuzz.pimf(accamulation.universe, -10,-9,-1,1)
accamulation['low'] = fuzz.trimf(accamulation.universe, [-1,1,25])
accamulation['medium'] = fuzz.trimf(accamulation.universe, [0,25,50])
accamulation['high'] = fuzz.trimf(accamulation.universe, [25,50,50])


fig = incoms.view()
fig.set_tight_layout(True)
fig.savefig('incoms.png')

fig = charges.view()
fig.set_tight_layout(True)
fig.savefig('charges.png')

economy.view()
fig.set_tight_layout(True)
fig.savefig('economy.png')

fig = accamulation.view()
fig.set_tight_layout(True)
fig.savefig('accamulation.png')

# low
rule1 = ctrl.Rule(incoms['low'] & charges['high'] & economy['bad'] ,accamulation['dept'])
rule2 = ctrl.Rule(incoms['low'] & charges['high'] & economy['average'],accamulation['dept'])
rule3 = ctrl.Rule(incoms['low'] & charges['high'] & economy['good'],accamulation['dept'])

rule4 = ctrl.Rule(incoms['low'] & charges['low'] & economy['bad'], accamulation['dept'])
rule5 = ctrl.Rule(incoms['low'] & charges['low'] & economy['good'], accamulation['low'])
rule6 = ctrl.Rule(incoms['low'] & charges['low'] & economy['average'], accamulation['low'])

rule7 = ctrl.Rule(incoms['low'] & charges['medium'] & economy['good'] , accamulation['low'])
rule8 = ctrl.Rule(incoms['low'] & charges['medium'] & economy['average'] , accamulation['dept'])
rule9 = ctrl.Rule(incoms['low'] & charges['medium'] & economy['bad'] , accamulation['dept'])

# medium
rule10 = ctrl.Rule(incoms['medium'] & charges['low'] & economy['bad'], accamulation['low'])
rule11 = ctrl.Rule(incoms['medium'] & charges['low'] & economy['good'], accamulation['medium'])
rule12 = ctrl.Rule(incoms['medium'] & charges['low'] & economy['average'], accamulation['medium'])

rule13 = ctrl.Rule(incoms['medium'] & charges['medium'] & economy['bad'] , accamulation['dept'])
rule14 = ctrl.Rule(incoms['medium'] & charges['medium'] & economy['average'], accamulation['low'])
rule15 = ctrl.Rule(incoms['medium'] & charges['medium'] & economy['good'], accamulation['low'])

rule16 = ctrl.Rule(incoms['medium'] & charges['high'] & economy['bad'], accamulation['dept'])
rule17 = ctrl.Rule(incoms['medium'] & charges['high'] & economy['average'], accamulation['dept'])
rule18 = ctrl.Rule(incoms['medium'] & charges['high'] & economy['good'] , accamulation['low'])

# high
rule19 = ctrl.Rule(incoms['high'] & charges['low'] & economy['bad'] , accamulation['medium'])
rule20 = ctrl.Rule(incoms['high'] & charges['low'] & economy['good'] , accamulation['high'])
rule21 = ctrl.Rule(incoms['high'] & charges['low'] & economy['average'], accamulation['high'])

rule22 = ctrl.Rule(incoms['high'] & charges['medium'] & economy['bad'], accamulation['low'])
rule23 = ctrl.Rule(incoms['high'] & charges['medium'] & economy['good'], accamulation['medium'])
rule24 = ctrl.Rule(incoms['high'] & charges['medium'] & economy['average'], accamulation['medium'])

rule25 = ctrl.Rule(incoms['high'] & charges['high'] & economy['bad'], accamulation['dept'])
rule26 = ctrl.Rule(incoms['high'] & charges['high'] & economy['average'], accamulation['dept'])
rule27 = ctrl.Rule(incoms['high'] & charges['high'] & economy['good'] , accamulation['low'])

money_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,
                                   rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23,rule24,rule25,
                                   rule26, rule27])

money = ctrl.ControlSystemSimulation(money_ctrl)

fig = rule7.view()[0]
fig.set_tight_layout(True)
fig.savefig('rule7.png')


fig = rule17.view()[0]
fig.set_tight_layout(True)
fig.savefig('rule17.png')

fig = rule27.view()[0]
fig.set_tight_layout(True)
fig.savefig('rule27.png')



try:
    money.input['incoms'] = float(input("Введите доходы: "))
    money.input['charges'] = float(input("Введите расходы: "))
    money.input['economy'] = float(input("Введите экономическую обстановку (от 0 до 100): "))
    money.compute()
    acc = money.output['accamulation']
    print()

    print("Рекомендуемые накопления: ", money.output['accamulation'])

    fig = accamulation.view(sim=money)
    fig.set_tight_layout(True)
    fig.savefig('result.png')
except:
    print("Введены некорректные данные, требуются числа")
