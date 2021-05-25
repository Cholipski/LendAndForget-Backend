# CATEGORY

Służy do pobierania i zarządzania kategoriami. 

## Metoda: ` POST `

- **URL** : ` /lend-app/category/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```json
{
    "category_name": "[category_name]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podana nazwa kategorii jest poprawna

- **Status** : ` 201 Created `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "category_name": "[category_name]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Podane nazwa kategorii jest zbyt długa 

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "category_name": [
        "Ensure this field has no more than 20 characters."
    ]
}
```

## Metoda: ` GET LIST `

- **URL** : `/lend-app/category/ `

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : 

- **Status** : ` 200 OK `

- **Zawartość** :
```json
[
    {
        "pk": pk,
        "url": "[url]",
        "category_name": "[category_name]"
    },
    ...
]
```

## Metoda: ` GET ITEM `

- **URL** : ` /lend-app/category/<int:pk> `

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Kategoria o podanym id istnieje

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "category_name": "[category_name]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Kategoria o podanym id nie istnieje

- **Status** : ` 404 Not found `

- **Zawartość** :

```json
{
    "detail": "Not found."
}
```
