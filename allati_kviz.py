def ellenorizd(valasz1, helyes_valasz):
    global pontszam
    meg_talalgat = True
    probaszam = 0
    while meg_talalgat and probaszam < 3:
        if valasz1.lower() == helyes_valasz.lower():
            print('Helyes válasz')
            pontszam = pontszam + 1
            meg_talalgat = False
        else:
            if probaszam < 2:
                valasz1 = input(
                    'Sajnálom, helytelen válasz. Próbálkozz ismét! : ')
            probaszam = probaszam + 1

    if probaszam == 3:
        print('A helyes válasz: ' + helyes_valasz)


pontszam = 0
print('Állati kvíz!')
valasz1 = input('Melyik medve él az Északi-sarkon? ')
ellenorizd(valasz1, 'jeges medve')
valasz2 = input('Melyik a leggyorsabb szárazföldi állat?')
ellenorizd(valasz2, 'gepárd')
valasz3 = input('Melyik a legnagyobb méretű állat? ')
ellenorizd(valasz3, 'kék bálna')
valasz4 = input('Melyik állatnak van hosszú orrmánya? ')
ellenorizd(valasz4, 'elefánt')
valasz5 = input('Melyik emlős tud repülni? ')
ellenorizd(valasz5, 'denevér')
valasz6 = input('Hány szive van a polipnak? ')
ellenorizd(valasz6, '3')
valasz7 = input(
    'Ezek közül melyik halfajta?\n \ A) Bálna\n B) Delfin\n C) Cápa\n D) Tintahal.\n Válassz A, B, C vagy D-t'
)
ellenorizd(valasz7, 'C')
valasz8 = input('Az egerek emlősök. Igaz vagy hamis? ')
ellenorizd(valasz8, 'igaz')
print('A pontszámod ' + str(pontszam))