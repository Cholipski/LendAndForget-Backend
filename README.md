# Pożycz i zapomnij - Backend  
  
Django Rest Api do projektu "Pożycz i zapomnij"  
  
## Instalacja  
  
1) Skopiować plik ``.env.example``  oraz usunąć `.example`
2) Uzupełnić plik `.env` wprowadzając dane konta mailingowego (połaczenie SMTP) oraz wygenerowany SECRECT KEY
   
  
  **(W pliku nie moze być żadnych spacj)**  
  
    Do wygenerowania SECTECT_KEY można użyć https://djecrety.ir  
  
3) W pliku `settings.py` zmieniamy ustawienia bazy danych
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

## Lista endpointów
### Autoryzacja

* [Login](/endpoints/authorization/login.md) : ` POST /auth/ `
* [Register](/endpoints/authorization/register.md) : ` POST /auth/register/ `
* [Token refresh](/endpoints/authorization/token_refresh.md) : ` POST /auth/token-refresh/ `
* [Email verify](/endpoints/authorization/email_verify.md) : ` POST /auth/email-verify/ `
* [User manage](/endpoints/authorization/user_manage.md/#metoda-get) : ` GET /auth/user-manage/ `
* [User manage](/endpoints/authorization/user_manage.md/#metoda-put) : ` PUT /auth/user-manage/ `
* [User manage](/endpoints/authorization/user_manage.md/#metoda-delete) : ` DELETE /auth/user-manage/ `

### Aplikacja do pożyczania

#### Kategorie
* [Category](/endpoints/lendapp/category.md/#metoda-post) : ` POST /lend-app/category/ `
* [Category](/endpoints/lendapp/category.md/#metoda-get-list) : ` GET /lend-app/category/ `
* [Category](/endpoints/lendapp/category.md/#metoda-get-item) : ` GET /lend-app/category/<int:pk> `

#### Statusy wypożyczeń
* [Loan status](/endpoints/lendapp/loan_status.md/#metoda-post) : ` POST /lend-app/loan-status/ `
* [Loan status](/endpoints/lendapp/loan_status.md/#metoda-get-list) : ` GET /lend-app/loan-status/ `
* [Loan status](/endpoints/lendapp/loan_status.md/#metoda-get-item) : ` GET /lend-app/loan-status/<int:pk> `

#### Wypożyczenia
* [Item loan](/endpoints/lendapp/item_loan.md/#metoda-post) : ` POST /lend-app/item-loan/ `
* [Item loan](/endpoints/lendapp/item_loan.md/#metoda-get-list) : ` GET /lend-app/item-loan/ `
* [Item loan](/endpoints/lendapp/item_loan.md/#metoda-get-item) : ` GET /lend-app/item-loan/<int:pk> `
* [Item loan](/endpoints/lendapp/item_loan.md/#metoda-put) : ` PUT /lend-app/item-loan/<int:pk> `
* [Item loan](/endpoints/lendapp/item_loan.md/#metoda-delete) : ` DELETE /lend-app/item-loan/<int:pk> `
* [Money loan](/endpoints/lendapp/money_loan.md/#metoda-post) : ` POST /lend-app/money-loan/ `
* [Money loan](/endpoints/lendapp/money_loan.md/#metoda-get-list) : ` GET /lend-app/money-loan/ `
* [Money loan](/endpoints/lendapp/money_loan.md/#metoda-get-item) : ` GET /lend-app/money-loan/<int:pk> `
* [Money loan](/endpoints/lendapp/money_loan.md/#metoda-put) : ` PUT /lend-app/money-loan/<int:pk> `
* [Money loan](/endpoints/lendapp/money_loan.md/#metoda-delete) : ` DELETE /lend-app/money-loan/<int:pk> `

#### Zwroty wypożyczeń
* [Return a item loan](/endpoints/lendapp/item_return.md) : ` POST /lend-app/item-return/ `
* [Return a money loan](/endpoints/lendapp/money_return.md) : ` POST /lend-app/money-return/ `

#### Powiadomienia
* [Notifications](/endpoints/lendapp/notifications.md/#metoda-post) : ` POST /lend-app/notifications/ `
* [Notifications](/endpoints/lendapp/notifications.md/#metoda-get-list) : ` GET /lend-app/notifications/ `
* [Notifications](/endpoints/lendapp/notifications.md/#metoda-get-item) : ` GET /lend-app/notifications/<int:pk> `
* [Delete notifications](/endpoints/lendapp/delete_notifications.md) : ` DELETE /lend-app/delete-notifications/ `
* [Delete all notifications](/endpoints/lendapp/delete_all_notifications.md) : ` DELETE /lend-app/delete-all-notifications/ `
* [Mark notification as seen](/endpoints/lendapp/notifications_mark_seen.md) : ` POST /lend-app/notifications-mark-seen/ `
* [Mark all notification as seen](/endpoints/lendapp/all_notifications_mark_seen.md) : ` POST /lend-app/all-notifications-mark-seen/ `
* [Request earlier return - item](/endpoints/lendapp/request_item_return.md) : ` POST /lend-app/request-item-return/ `
* [Request longer return time - item](/endpoints/lendapp/request_item_longer_time.md) : ` POST /lend-app/request-item-longer-time/ `
* [Set reminding notification - item](/endpoints/lendapp/create_item_reminder.md) : ` POST /lend-app/create-item-reminder/ `
* [Request earlier return - money](/endpoints/lendapp/request_money_return.md) : ` POST /lend-app/request-money-return/ `
* [Request longer return time - money](/endpoints/lendapp/request_money_longer_time.md) : ` POST /lend-app/request-money-longer-time/ `
* [Set reminding notification - money](/endpoints/lendapp/create_money_reminder.md) : ` POST /lend-app/create-money-reminder/ `

#### Lista kontaktów 
* [Contact](/endpoints/lendapp/contact.md/#metoda-get-list) : ` GET /lend-app/contact/ `
* [Contact](/endpoints/lendapp/contact.md/#metoda-get-item) : ` GET /lend-app/contact/<int:pk> `
* [Contact](/endpoints/lendapp/contact.md/#metoda-delete) : ` DELETE /lend-app/contact/ `

## Schemat bazy danych projektu
![Schemat bazy danych](/endpoints/databaseModel.png)
