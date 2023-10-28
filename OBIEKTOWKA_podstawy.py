class Auto:
    #init pozwala na ustalenie co to auto ma, jakie dane
    def __init__(self,kolor, kondycja, wiek, przebieg):
        self.kolor = kolor #self jest po to zeby mozna bylo do danych dla klasy wejsc z poziomu programu
        self.ilosc_paliwa = 10
        self.kondycja = kondycja #zalozmy ze od 1-5 ale kondycja moze byc rowna stan jezeli po init tez bedzie stan zamiast kondycja
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.rocznik = 2023-wiek
        self.przebieg = przebieg
    def __str__(self): #jak wpiszemy print auto.Kamila to wyrzuci nam te dane co wypiszemy w funkcji str
        return(f'Auto o przebiegu {self.przebieg}, rocznik {self.rocznik}')
    def tryb_eco(self):
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 10
    def tryb_normal(self):
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
    def zasieg(self):
        zasieg =self.ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)

    def zmiana_trybu(self,tryb):
        #user_choice = int(input('Wybierz Tryb [1] eco [2] normal'))
        if tryb == 'eco':
            self.tryb_ekonomiczny = True
            self.spalanie_na_100 = 10
            print(f'Wlaczono tryb eco')
        elif tryb == "normal":
            self.tryb_ekonomiczny = False
            self.spalanie_na_100 = 14
            print(f'Wlaczono tryb normal')
        else:
            self.tryb_eco()
            print(f'Nie rozpoznano wyboru, zostawiam tryb ekonomiczny {self.tryb_ekonomiczny}')
    def zmien_przebieg(self, ile):
        if ile > 0:
            self.przebieg += ile


  #  def __eq__(self,kolor):

auto_Kamila = Auto('zielone',4,12,55)

print(auto_Kamila.kolor)
auto_Kamila.kolor = "niebieskie"
print(auto_Kamila.kolor)
auto_Sylwii = Auto('fioletowe',5,1, 44)

print(f'spalanie na 100 przed zmiana {auto_Kamila.spalanie_na_100}')

tryb = input('Wybierz tryb [eco] lub [normal]')
auto_Kamila.zmiana_trybu(tryb.lower())


print(f'spalanie na 100 po zmianie {auto_Kamila.spalanie_na_100}')

print(f'Przejedziesz jeszcze {auto_Kamila.zasieg()} km')
print(auto_Kamila)