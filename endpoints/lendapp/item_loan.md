# ITEM LOAN

Służy do zarządzania wypożyczeniami przedmiotów

## Metoda: ` POST `

- **URL** : ` /lend-app/item-loan/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```json
{
    "name": "[name]",
    "description": "[description]",
    "startDate": "[start_date]",
    "endDate": "[end_date]",
    "itemAmount": "[item_amount]",
    "borrowerID": "[borrower_email]",
    "itemCategoryID": "[item_category_id]",
    "amount": "[amount]",
    "image": "[image]"
}  
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podane dane wypożyczenia przedmiotu są poprawne

- **Status** : ` 201 Created `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "name": "[name]",
    "description": "[description]",
    "start_date": "[start_date]",
    "end_date": "[end_date]",
    "item_amount": item_amount,
    "borrower_id": "[borrower_username]",
    "item_category_id": "[itemcategory_name]",
    "image": "[image]",
    "loan_status_id": "[loanstatus_name]",
    "lender_id": "[lender_username]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Data zakończenia nie może poprzedzać daty rozpoczęcia

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "end_date": [
        "The end date cannot precede the start date"
    ]
}
```

- **Warunek wystąpienia** : Data zakończenia nie może być wcześniejsza niż dzisiaj

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "end_date": [
        "The end date cannot be earlier than today"
    ]
}
```

- **Warunek wystąpienia** : Użytkownik z podanym adresem email nie istnieje

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "borrower_ird": [
        "Object with email=[borrower_email] does not exist."
    ]
}
```

- **Warunek wystąpienia** : Gdy ustawimy dane borrower'a na dane aktualnie zalogowanego użytkownika 

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "borrower_ird": [
        "You can not lend item for yourself"
    ]
}
```

## Metoda: ` GET LIST `

- **URL** : ` /lend-app/item-loan/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany 

- **Status** : ` 200 OK `

- **Zawartość** :
```json
[
    {
        "pk": pk,
        "url": "[url]",
        "name": "[name]",
        "description": "[description]",
        "start_date": "[start_date]",
        "end_date": "[end_date]",
        "item_amount": item_amount,
        "borrower_id": "[borrower_username]",
        "item_category_id": "[itemcategory_name]",
        "image": "[image]",
        "loan_status_id": "[loanstatus_name]",
        "lender_id": "[lender_username]"
    },
    ...
]
```

## Metoda: ` GET ITEM `

- **URL** : ` /lend-app/item-loan/<int:pk> `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany 

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "name": "[name]",
    "description": "[description]",
    "start_date": "[start_date]",
    "end_date": "[end_date]",
    "item_amount": item_amount,
    "borrower_id": "[borrower_username]",
    "item_category_id": "[itemcategory_name]",
    "image": "[image]",
    "loan_status_id": "[loanstatus_name]",
    "lender_id": "[lender_username]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Użytkownik podał nieistniejące id lub id wypożyczenia do którego nie ma dostępu 

- **Status** : ` 404 Not found `

- **Zawartość** :

```json
{
    "detail": "Not found."
}
```

## Metoda: ` PUT `

- **URL** : ` /lend-app/item-loan/<int:pk> `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```json
{
    "name": "[name]",
    "description": "[description]",
    "start_date": "[any_start_date]",
    "end_date": "[end_date]",
    "item_amount": any_item_ammount,
    "borrower_id": "[any_email]",
    "item_category_id": any_itemcategory_id
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podane dane są poprawne
- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "name": "[name]",
    "description": "[description]",
    "start_date": "[start_date]",
    "end_date": "[end_date]",
    "item_amount": item_amount,
    "borrower_id": "[borrower_username]",
    "item_category_id": "[itemcategory_name]",
    "image": "[image]",
    "loan_status_id": "[loanstatus_name]",
    "lender_id": "[lender_username]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Data zakończenia nie może poprzedzać daty rozpoczęcia

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "end_date": [
        "The end date cannot precede the start date"
    ]
}
```

- **Warunek wystąpienia** : Data zakończenia nie może być wcześniejsza niż dzisiaj

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "end_date": [
        "The end date cannot be earlier than today"
    ]
}
```

## Metoda: ` DELETE `

- **URL** : ` /lend-app/item-loan/<int:pk> `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Wypożyczenie z takim id istnieje i użytkownik jest właścielem przedmiotu

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "name": "[name]",
    "description": "[description]",
    "start_date": "[start_date]",
    "end_date": "[end_date]",
    "item_amount": item_amount,
    "borrower_id": "[borrower_username]",
    "item_category_id": "[itemcategory_name]",
    "image": "[image]",
    "loan_status_id": "[loanstatus_name]",
    "lender_id": "[lender_username]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Wypożyczenie o danym id nie istnieje lub zalogowany użytkownik nie jest jego właścicielem 

- **Status** : ` 404 Not found `

- **Zawartość** :

```json
{
    "detail": "Not found."
}
```


