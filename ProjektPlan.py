import random,time

operatory = [] 

kroki = [] 

porządek = [] 

związki = [] 

miejsca = ['dom']

artykuły = []

artykułyWSklepie = []

informacje = []


class ArtykułWSklepie:
#Klasa pozwala na utworzenie obiektów, reprezentujących relacje pomiędzy sklepami a sprzedawanymi artykułami.

    def __init__(self,sklep,artykuł):
        self.sklep = sklep
        self.artykuł = artykuł

class Operator:
#Klasa, któej instancje odpowiadają operatorom języka STRIPS.
#Zawierają listy warunków i następników oraz nazwę wykonywanej akcji.
#Obiekty tej klasy zapisane sa na liście operatory[].
    
    def __init__(self,akcja = None,następniki = [],warunki = []):
        self.warunki = warunki
        self.akcja = akcja
        self.następniki = następniki
        operatory.append(self)           


class Stan:
#Klasa przeznaczona do przechowywania treści warunków wykonania akcji oraz informacji o ich spełnieniu.

    def __init__(self,nazwa,jestSpełniony = False):
        self.nazwa = nazwa
        self.jestSpełniony = jestSpełniony

class Związek:
#Instancje klasy Związek zawierają informację o związku między dwoma krokami i warunku spełnianym przez ten związek.
    def __init__(self,krokA,krokB,warunek):
        self.krokA = krokA
        self.krokB = krokB
        self.warunek = warunek.nazwa 

#Funkcje należące do modułu Problem, pozwalające na implementację problemu za pomocą operatorów języka STRIPS 


def utworzOperatorStart():
#Funkcja tworząca operator Start wraz z jego następnikami, uzależnionymi od danych wprowadzonych przez użytkownika.

    operatorStart = Operator(akcja = 'Start',następniki = [Stan('Jest(dom)')], warunki = [])
    for i in artykułyWSklepie:
        artykuł = i.artykuł
        sklep = i.sklep
        nowyNastępnik = Stan('Sprzedaje('+sklep+','+artykuł+')')
        operatorStart.następniki.append(nowyNastępnik)

def utworzOperatorCel():
#Funkcja tworząca operator Cel wraz z jego warunkami, uzależnionymi od danych wprowadzonych przez użytkownika.

    operatorCel = Operator(akcja = 'Cel',warunki = [ Stan('Jest(dom)')], następniki = [])
    for i in artykuły:
        nowyWarunek = Stan('Ma('+i+')')
        operatorCel.warunki.append(nowyWarunek)

def utwórzOperatoryIść():
#Funkcja tworzy operatory STRIPS Iść i dodaje je do listy operatory[].
    for i in range(len(miejsca)):
        for j in range(len(miejsca)):
            if i != j:
                operatorIść = Operator(akcja = 'Iść('+miejsca[i]+')',następniki = [Stan('Jest('+miejsca[i]+')'),Stan('!Jest('+miejsca[j]+')')],warunki = [Stan('Jest('+miejsca[j]+')')])
                operatorIść = Operator(akcja = 'Iść('+miejsca[j]+')',następniki = [Stan('Jest('+miejsca[j]+')'),Stan('!Jest('+miejsca[i]+')')],warunki = [Stan('Jest('+miejsca[i]+')')])

    
def utworzOperatoryKupić():
#Funkcja tworzy operatory STRIPS Kupić i dodaje je do listy operatory[].
    for i in artykułyWSklepie:
        artykuł = i.artykuł
        sklep = i.sklep
        operatorKupić = Operator(akcja = 'Kupić('+artykuł+')',następniki = [Stan('Ma('+artykuł+')')],warunki = [Stan('Jest('+sklep+')'),Stan('Sprzedaje('+sklep+','+artykuł+')')])

def określLiczbęSklepówArtykułów():
#Funkcja początkowa, określająca warunki, w jakich bedzie działał program.
    utworzSklepy()
    utworzOperatorStart()
    utworzOperatorCel()
    utworzOperatoryKupić()
    utwórzOperatoryIść()

#Funkcje należące do modułu Metoda, realizujące implementację ogólnego algorytmu tworzenia planu

def utwórzPlanPoczątkowy(operatorS,operatorC):
#Funkcja tworzy plan złożony jedynie z operatorów Start i Cel.Są one dodawane do list kroki[] oraz porządek[]
    porządek.append(operatorS)
    kroki.append(operatorS)
    operatory.remove(operatorS)
    porządek.append(operatorC)
    kroki.append(operatorC)
    operatory.remove(operatorC)

def sprawdzKompletnośćPlanu(k):
#Funkcja sprawdza, czy dla każdego kroku spełnione są wszystkie warunki.   
    for krok in k:
        for warunek in krok.warunki:
            if warunek.jestSpełniony == False:
                #print('Niespełniony waruenk:',krok.akcja,warunek.nazwa)
                return False
    return True

def wybierzKrok(krokiPlanu):
#Funkcja, która wybiera podcel, czyli krok planu, którego warunek nie został jeszcze spełniony.
    for k in krokiPlanu:
        for warunek in k.warunki:   
            if warunek.jestSpełniony == False:
                result = (k,warunek)
                return result
    return False
            

def sprawdźSpełnienieWarunków(o,w):
#Funkcja zwraca informację, czy nsatępnik przekazanego operatora spełnia przekazany warunek.
    for następnik in o.następniki:
        if w.nazwa == następnik.nazwa:
            return True

def dodajKrokPoprzedzający(o,k,wybranyKrok,wybranyWarunek):
#Funkcja pobiera wybrane przez funkcje WybierzKrok() krok oraz warunek, następnie
#przeszukuje listę kroki[] oraz, jeżeli jest to konieczne, operatory[]. Jeżeli 
#dany krok spełnia warunek, tworzony jest odpowiedni związek, a krok dodawany jest do porządku planu.
#Uzupełniana jest lista porządek[].Dodany krok jest zwracany w celu sprawdzenia potencjalnych zagrożeń 
#dla istniejących związków.
#Jeżeli operator spełnia warunek, jest on dodawany do listy kroki[]. Funkcja zwraca wówczas False.
    for krok in k:
        if krok.akcja != wybranyKrok.akcja:
            if sprawdźSpełnienieWarunków(krok,wybranyWarunek) == True:
                licznik = porządek.count(krok)
                if licznik == 0:
                    indeks = porządek.index(wybranyKrok)
                    porządek.insert(indeks,krok)
                    info = 'Do planu dodano krok:' + krok.akcja
                    informacje.append(info)
                wybranyWarunek.jestSpełniony = True
                związek = Związek(krok,wybranyKrok,wybranyWarunek)
                związki.append(związek)
                info = 'Do planu dodano związek: '+związek.krokA.akcja+'->'+związek.krokB.akcja
                informacje.append(info)
                
                return krok

    for operator in o:
        if operator.akcja != wybranyKrok.akcja:
            if sprawdźSpełnienieWarunków(operator,wybranyWarunek) == True:
                kroki.append(operator)
                info = 'Do planu dodano krok: '+operator.akcja
                informacje.append(info)
                return False

def promocja(k1,k2,p):
#Funkcja zamienia miejscami kroki w sposób realizujący promocję.
#Warunek w niej zawarty gwarantuje, że operator Start znajdzie sie na początku planu. 
    if k2.akcja != 'Start':
        p.remove(k1)
        indeks = p.index(k2)
        p.insert(indeks,k1)
        info = 'Wykonano promocję kroku: '+k1.akcja
        informacje.append(info)
        return

def degradacja(k1,k2,p):
#Funkcja zamienia miejscami kroki w sposób realizujący degradację.
#Warunek w niej zawarty gwarantuje, że operator Cel znajdzie sie na końcu planu. 
    if k2.akcja != 'Cel':
        p.remove(k1)
        indeks = p.index(k2)
        p.insert(indeks+1,k1)
        info = 'Wykonano degradację kroku :' + k1.akcja
        informacje.append(info)
        return

def wykonajNawrót(o,wybranyKrok,wybranyWarunek):
#Funkcja wykonywana w przypadku, gdy promocja i degradacja nie rozwiązały zagrożenia dla planu.
#Dodaje ona do planu operator, który spełnia zanegowany przez dodany krok warunek.
    for operator in o:
        if operator.akcja != wybranyKrok.akcja:
            if sprawdźSpełnienieWarunków(operator,wybranyWarunek) == True:
                kroki.append(operator)
                porządek.insert(len(porządek)-1,operator)
                wybranyWarunek.jestSpełniony = True
                info = 'Do planu dodano krok: ' + operator.akcja
                print(info)
                return 

def rozwiążZagrożenia(k,z,p):
#Funkcja, która wykrywa zagrożenia dla istniejących związków, wynikające z dodania do planu nowego kroku.
#W przypadku wykrycia zagrożenia, następuje próba poprawy planu poprzez zastosowanie promocji, degradacji lub nawrotu.    
    for związek in z:
        licznik = p.count(związek.krokB)
        if licznik != 0:
            indeksKrokA = p.index(związek.krokA)
            indeksKrokB = p.index(związek.krokB)
            indeksSprawdzany = p.index(k)
            if indeksSprawdzany > indeksKrokA and indeksSprawdzany < indeksKrokB:
                warunek = związek.warunek
                negacja = '!' + warunek
                for następnik in k.następniki:
                    if następnik.nazwa == negacja:
                        promocja(k,związek.krokA,p)
    for związek in z:
        licznik = p.count(związek.krokB)
        if licznik != 0:
            indeksKrokA = p.index(związek.krokA)
            indeksKrokB = p.index(związek.krokB)
            indeksSprawdzany = p.index(k)
            if indeksSprawdzany > indeksKrokA and indeksSprawdzany < indeksKrokB:
                warunek = związek.warunek
                negacja = '!' + warunek
                for następnik in k.następniki:
                    if następnik.nazwa == negacja:
                        degradacja(k,związek.krokB,p)
    for związek in z:
        licznik = p.count(związek.krokB)
        if licznik != 0:
            indeksKrokA = p.index(związek.krokA)
            indeksKrokB = p.index(związek.krokB)
            indeksSprawdzany = p.index(k)
            if indeksSprawdzany > indeksKrokA and indeksSprawdzany < indeksKrokB:
                warunek = związek.warunek
                negacja = '!' + warunek
                for następnik in k.następniki:
                    if następnik.nazwa == negacja:
                        for w in związek.krokB.warunki:   
                            if w.nazwa == warunek:
                                w.jestSpełniony = False
                                związki.remove(związek)
                                info = 'Z planu usunięto związek: ' + związek.krokA.akcja + '->' + związek.krokB.akcja
                                informacje.append(info)
                                wykonajNawrót(operatory,związek.krokB,w)
                                return

#Funkcje należące do modułu Sterowanie, pobierające od użytkownika informacje o liczbie sklepów i artykułów. 
#Prezentują również operacje wykonane w poszczególnych krokach tworzenia planu oraz umożliwiają zapis 
#rezultatów do pliku lub zakończenie pracy programu.

def utworzSklepy():
#Funkcja pobierająca liczbę sklepów i artykułów od użytkownika i losowo przyporządkowująca je.
#w wyniku jej działania powstają instancje klasy ArtykułWSklepie, któe następnie są dodawane
# do listy artykułyWSklepie[].
    ileSklepów = int(input("Proszę podać liczbę sklepów: "))
    for i in range(ileSklepów):
        miejsca.append('sklep'+str(i+1))
    ileArtykułów = int(input('Proszę podać liczbę artykułów: '))
    for i in range(ileArtykułów):
        artykuły.append('artykuł'+str(i+1))
    for i in range(len(artykuły)):
        j = random.choice(range(1,len(miejsca)))
        nowyArtykułWSklepie = ArtykułWSklepie(miejsca[j],artykuły[i])
        artykułyWSklepie.append(nowyArtykułWSklepie) 
        
def prezentujInformacje(j,info):
#Funkcja wyświetlająca operacje wykonane w danym kroku.
    print('W przejśćiu',j+1,'wykonano następujące operacje:')
    for i in info:
        print(i)
    print('\n')

def zapiszDoPliku(p,z,czas,iteracje,ścieżka):
    print(ścieżka)
    plik = open(ścieżka,'a')

    plik.write('Utworzony plan:\n')
    for i in p:
        plik.write(i.akcja)
        plik.write('\n')
    plik.write('\n')

    plik.write('Związki planu:\n')
    for i in z:
        plik.write(i.krokA.akcja + '--->' + i.krokB.akcja)
        plik.write('\n')
    plik.write('\n')

    plik.write('Porządek:\n')
    for i in porządek:
        akt = i.akcja
        if(akt != 'Start'):
            pop = porządek[porządek.index(i)-1].akcja
            plik.write(pop + ' < ' + akt)
            plik.write('\n')
        else:
            continue
    plik.write('\n')

    plik.write('Czas wykonania: '+str(czas)+' sekund')
    plik.write('\n')
    plik.write('Wykonane kroki: '+str(iteracje))

    plik.close()

def pobierzŚcieżkę():
    while(True):
        pobrane = str(input('Aby zapisać wyniki do pliku, prosze wcisnąć t. Aby zakończyć pracę programu, proszę wcisnąc e.'))
        if pobrane == 't':
            ścieżka = input('Proszę wprowadzić ścieżkę do pliku:' )
            return ścieżka
        if pobrane == 'e':
            exit()




określLiczbęSklepówArtykułów()

startCzas = time.time()
utwórzPlanPoczątkowy(operatory[0],operatory[1])

kompletnyPlan = sprawdzKompletnośćPlanu(porządek)

iteracje =0

while (kompletnyPlan != True):
#Główna pętla, wykonująca się do czasu, aż plan nie będzie kompletny.
    wybórKroku = wybierzKrok(kroki)
    #Wybór podcelu
    if wybórKroku != False:
    #Sprawdzenie, czy podcel został wybrany
        zagrożenie = dodajKrokPoprzedzający(operatory,kroki,wybórKroku[0],wybórKroku[1])
        #Dodanie nowego kroku lub operatora, utworzenie związków i ustalenie kolejności.
                
        if zagrożenie != False:
            #Sprawdzenie, czy po dodaniu kroku wystepuje zagrozenie dla dowolnego związku.
            rozwiążZagrożenia(zagrożenie,związki,porządek)
            #Poprawa planu poprzez promocję, degradację lub nawrót.

    kompletnyPlan = sprawdzKompletnośćPlanu(porządek)
    #Sprawdzenie, czy utworzony plan jest kompletny.

    if kompletnyPlan == True:
        stopCzas = time.time()
        info = 'Tworzenie planu zostało zakończone po '+str(iteracje+1)+' krokach'
        informacje.append(info)

    prezentujInformacje(iteracje,informacje)
    #Monitorowanie procesu tworzenia planu.
    informacje.clear()
    iteracje += 1

print('-'*30)
czasWykonania = stopCzas - startCzas
#Prezentacja utworzonego planu, związków oraz porządku

print('Utworzony plan:\n')
for i in porządek:
    print(i.akcja)
print('\n')

print('Związki planu:\n')
for i in związki:
    print(i.krokA.akcja + '--->' + i.krokB.akcja)
print('\n')

print('Porządek:\n')
for i in porządek:
    akt = i.akcja
    if(akt != 'Start'):
        pop = porządek[porządek.index(i)-1].akcja
        print(pop + ' < ' + akt)
    else:
        continue
print('\n')

print('Czas wykonania:',stopCzas - startCzas,'sekund')
print('Iteracje:',iteracje)
ścieżkaPlik = pobierzŚcieżkę()
zapiszDoPliku(porządek,związki,czasWykonania,iteracje,ścieżkaPlik)



