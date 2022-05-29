from colorama import *
init(autoreset=True)
class phys_theory():
    def archimed():
        print(Fore.CYAN + "Выталкивающая" + Fore.GREEN +  " или " +  Fore.CYAN + "подъёмная сила " + Fore.GREEN +  "по направлению противоположна " +  Fore.CYAN + " силе тяжести" + Fore.GREEN +  ", прикладывается к " +  Fore.CYAN + "центру тяжести объёма" + Fore.GREEN +  ", вытесняемого телом из " +  Fore.CYAN + "жидкости или газа.")
        print(Fore.GREEN + "\nНапример, воздушный шарик объемом " + Fore.RED + "V" + Fore.GREEN +  ", наполненный гелием, летит вверх из-за того, что " + Fore.RED + "плотность" + Fore.GREEN +  " гелия меньше " + Fore.RED + "плотности" + Fore.GREEN +  " воздуха")
        print(Fore.CYAN + "\nФормула сие закона: " + Fore.GREEN +  "Fa = pgV \nFa" +  Fore.CYAN + " — Сила Архимеда\n" + Fore.GREEN +  "p" +  Fore.CYAN + " — Плотность жидкости/газа на кг/м3\n" + Fore.GREEN +  "g " +  Fore.CYAN + "— ускорение свободного падения в м/с2\n" + Fore.GREEN +  "V " +  Fore.CYAN + "— объём части тела, погружённой в жидкость или газ на м3")
    def boyl_mar():
        print(Fore.CYAN + "При постоянных " + Fore.GREEN +  " температуре" +  Fore.CYAN + " и " + Fore.GREEN +  "массе газа" +  Fore.CYAN + " произведение " + Fore.GREEN +  " давления газа " +  Fore.CYAN + "на его " + Fore.GREEN +  "объём " +  Fore.CYAN + "постоянно.")
        print(Fore.CYAN + "\nВ математической форме это выглядит так: " + Fore.GREEN +  "pV=C" +  Fore.CYAN + "\n" + Fore.GREEN +  "p" +  Fore.CYAN + " — давление газа\n" + Fore.GREEN +  "V" +  Fore.CYAN + " — объём газа\n" + Fore.GREEN +  "C" +  Fore.CYAN + " — постоянная в оговоренных условиях величина")
        print(Fore.CYAN + "\nИз этого следует вот эта формула: "+ Fore.GREEN + "p = C/V")
class geom_theory():
    pass

phys_theory.boyl_mar()