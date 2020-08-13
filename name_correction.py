zaznamy = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']

def vyber_chybne(seznam):
    seznam_chybnych = []
    for i in seznam:
        oddel = i.split()
        if oddel[0].islower() or oddel[1].islower():
            seznam_chybnych.append(i)      
    return seznam_chybnych

def vyber_spravne(seznam):
    seznam_spravnych = []
    for i in seznam:
        oddel = i.split()
        if not oddel[0].islower() and not oddel[1].islower():
            seznam_spravnych.append(i)
    return seznam_spravnych
      
def opravene_zaznamy(seznam):
    opraveny_seznam = []
    for i in seznam:
        oddel = i.split()
        jmeno = oddel[0].capitalize()
        prijmeni = oddel[1].capitalize()
        cele_jmeno = jmeno + ' ' + prijmeni
        opraveny_seznam.append(cele_jmeno)
    return opraveny_seznam

chybne_zaznamy = vyber_chybne(zaznamy)
print(chybne_zaznamy)

spravne_zaznamy = vyber_spravne(zaznamy)
print(spravne_zaznamy)

oprav_zaznamy = opravene_zaznamy(zaznamy)
print(oprav_zaznamy)