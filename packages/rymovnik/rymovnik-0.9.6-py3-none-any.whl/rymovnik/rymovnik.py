#!/usr/bin/python3

"""
Tento program je velmi jednoduchý vyhledávač výrazů ve slovníku
českých slov, který lze například použít pro vyhledávání rýmů.

Vytvořil Lukáš Růžička (lruzicka@redhat.com), 2022.

Program je vytvořen pod licencí GPL. Pokud jste s programem
neobdrželi licenci, najdete ji na adrese 
https://www.gnu.org/licenses/gpl-3.0.html.

Program se poskytuje bez jakýchkoliv záruk na jeho funkčnost.
"""

import argparse
import os
import pkgutil
import re

class Prikazy:
    """ Reprezentuje vyhledávací kritéria z příkazového řádku. """
    def __init__(self):
        """ Inicialize čtečku příkazového řádku. """
        self.radek = argparse.ArgumentParser()
        self.radek.add_argument('-k', '--konec', help="Najde konec slova podle vzoru.")
        self.radek.add_argument('-s', '--shoda', help="Najde shodu kdekoliv ve slově.")
        self.radek.add_argument('-d', '--delka', help="Omezí výsledky na slova s určenou délkou.")
        self.radek.add_argument('-r', '--regex', help="Vyhledá slova podle regulárního výrazu.")
        self.radek.add_argument('-l', '--slovnik', help="Načte navíc slova ze slovníku zvoleného souboru.")

    def prikazy(self):
        """ Vrátí načtená vyhledávací kritéria. """
        return self.radek.parse_args()


class Slovnik:
    """ Reprezentuje slovník českých slov. """
    def __init__(self, externi=None):
        """ Načte slovník z externího souboru a připraví jej jako seznam slov. """
        # Načti obsah přibaleného souboru s daty.
        soubor = pkgutil.get_data('rymovnik','slovnik.dic')
        # Dekóduj binární string na normální string, přičemž na konci
        # řádků vzniknou symboly \r a \n
        soubor = soubor.decode("utf-8")
        # Rozděl jednotlivé řádky podle \r
        data = soubor.split('\r')
        # Projdi data a očisti je od bílých symbolů
        ocistena_data = [radek.strip() for radek in data]
        self.slovnik = ocistena_data
        # Jestliže chceme externí data, tak se načtou
        # zde:
        if externi:
            with open(externi, 'r') as extradata:
                data = extradata.readlines()
            data = [x.strip() for x in data]
            self.slovnik = self.slovnik + data
        
    def najdi_shodu(self, vyraz):
        """ Najde všechny slova, která obsahují daný výraz. """
        shody = []
        for slovo in self.slovnik:
            if vyraz in slovo:
                shody.append(slovo)
        return shody

    def najdi_regex(self, vyraz):
        """ Najde všechny slova, která odpovídají regulárnímu výrazu. """
        vyraz = re.compile(vyraz)
        shody = []
        for slovo in self.slovnik:
            if re.match(vyraz, slovo):
                shody.append(slovo)
        return shody

    def najdi_konec(self, vyraz):
        """ Najde všechny slova, která končí na zadaný výraz. """
        shody = []
        rozsah = (len(vyraz) * -1)
        for slovo in self.slovnik:
            konec = slovo[rozsah:]
            if konec == vyraz:
                shody.append(slovo)
        return shody

        
class Tiskarna:
    """ Reprezentuje jednoduchý výstupní mechanismus. """
    def __init__(self):
        pass
        
    def tisk(self, pocet, zaznamy):
        """ Zobrazí nalezené záznamy a mírně je graficky upraví. """
        print(f"================ Nalezeno {pocet} vyhovujících slov. ================== ")
        for z in zaznamy:
            print(z)
        
        print("--------------------- Konec ---------------------------")


def main():
    """ Provádí hlavní tělo programu.  """
    # Vyřešíme příkazový řádek
    prikazovy_radek = Prikazy()
    vyber = prikazovy_radek.prikazy()
    
    # Podle toho, jestli si uživatel přeje externí data,
    # vytvoříme datový objekt.
    if vyber.slovnik:
        slova = Slovnik(vyber.slovnik)
    else:
        slova = Slovnik()
    # Načteme objekt tiskárny
    tisk = Tiskarna()
    
    # Podle příkazového řádku vybereme slova ze slovníku
    if vyber.konec:
        nalezeno = slova.najdi_konec(vyber.konec)
    elif vyber.shoda:
        nalezeno = slova.najdi_shodu(vyber.shoda)
    elif vyber.regex:
        nalezeno = slova.najdi_regex(vyber.regex)
    else:
        nalezeno = slova.slovnik
    
    if vyber.delka:
        delka = int(vyber.delka)
        omezeno = []
        for slovo in nalezeno:
            if len(slovo) == delka:
                omezeno.append(slovo)
        nalezeno = omezeno
                
    tisk.tisk(len(nalezeno), nalezeno)    

if __name__ == '__main__':
    main()
