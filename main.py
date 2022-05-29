from brain import *
from colorama import *
init(autoreset=True)
print(Fore.GREEN + "\t\tКалькулятор/справочник by " + Fore.CYAN + "HeLK")
print(Fore.GREEN + "Что вы хотите открыть? \n1> Калькулятор\n2> Справочник" + Back.RED + Fore.WHITE +  "(НЕ работает)")
open_operation = int(input(">>> "))

#КАЛЬКУЛЯТОР
if open_operation == 1:
    while True:
        print(Fore.GREEN + "Вы выбрали: Калькулятор")
        print(Fore.GREEN + "Какой раздел вы хотите выбрать?" + Fore.CYAN + "\n1> Физика" + Fore.CYAN + "\n2> Геометрия")
        number = int(input(">>> "))
            #ФИЗИКА
        if number == 1:
            print(Fore.GREEN + "Операции доступные вам:\n" + Fore.CYAN + "1> Расчёт силы тока " + Fore.GREEN + "{По Закону Ома}" + Fore.CYAN +"\n2> Расчёт сопротивления"+ Fore.GREEN + " {По Закону Ома}")
            print(Fore.CYAN + "3> Рассчёт напряжения" + Fore.GREEN + "{По Закону Ома}")
            phys_calc_oper = int(input(">>> "))
            if phys_calc_oper == 1:
                phys.amper()
            elif phys_calc_oper == 2:
                phys.om()
            elif phys_calc_oper == 3:
                phys.volt()
        if number == 2:
            print(Fore.GREEN + "Операции доступные вам:")
            print(Fore.CYAN + "1> Площадь Круга(не Михаила)")
            print(Fore.CYAN + "2> Площадь прямоугольного треугольника по 2 катетам")
            print(Fore.CYAN + "3> Формула площади треугольника по стороне и высоте")
            print(Fore.CYAN + "4> Площадь треугольника вписанного в окружность")
            print(Fore.CYAN + "5> Нахождение гипотенузы по теореме Пифагора")
            print(Fore.CYAN + "6> Длина вектора")
            geom_calc_oper = int(input(">>> "))
            if geom_calc_oper == 1:
                geom.scyrcle()
            elif geom_calc_oper == 2:
                geom.stre()
            elif geom_calc_oper == 3:
                geom.stre2()
            elif geom_calc_oper == 4:
                geom.stre_cyr()
            elif geom_calc_oper == 5:
                geom.gipo()
            elif geom_calc_oper == 6:
                geom.vektor_dl()

elif open_operation == 2:
    while True:
        print(Fore.GREEN + "Вы выбрали: Справочник")
        print(Fore.GREEN + "Какой раздел вы хотите выбрать?" + Fore.CYAN + "\n1> Физика" + Fore.CYAN + "\n2> Геометрия")
        number = int(input(">>> "))
        if number == 1:
            