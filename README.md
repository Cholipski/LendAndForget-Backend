# Pożycz i zapomnij - Backend  
  
Django Rest Api do projektu "Pożycz i zapomnij"  
  
##Instalacja  
  
1) Utworzyć plik ``.env`` w głownym katalogu  
2) W pliku ``.env`` umieścić  `SECRECT_KEY`  
  
  Przykład. `SECRET_KEY=AAAAAAAAAAAAAAAAAAAA`  
  
  **(W pliku nie moze być żadnych spacj)**  
  
    Do wygenerowania można użyć https://djecrety.ir  
  
3) W pliku `settings.py` zmieniamy ustawienia bazy danych oraz dane do konta mailowego SMTP
4) Uruchamiamy polecenie `Poetry install`
5) Następnie `Potery run python manage.py migrate`
6) Tworzymy superusera poleceniem `Poetry run python manage.py createsuperuser`
	jako email podajemy: admin@admin.pl

7) Dodajemy do tabeli `lendapp_loanstatus` 2 wartości 
	* "Wypożyczony" z id = 1
	* "Zwrócony" z id = 2

8) Do tabeli `lendapp_itemcategory` dodajemy kategorie
    * gry komputerowe
    * elektronika
    * ubrania
    * pojazdy
    * narzędzia
    * sprzęt sportowy
    * zabawki
    * płyty CD/DVD
    * inne

9) Uruchamiamy aplikację poleceniem `Poetry run python manage.py runserver`