# LOAN STATUS

Służy do pobierania i zarządzania statusami wypożyczeń. 

## Metoda: ` POST `

- **URL** : ` /lend-app/loan-status/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```json
{
    "status_name": "[status_name]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podana nazwa statusu jest poprawna

- **Status** : ` 201 Created `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "status_name": "[status_name]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Podane nazwa statusu jest zbyt długa 

- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "status_name": [
        "Ensure this field has no more than 15 characters."
    ]
}
```

## Metoda: ` GET LIST `

- **URL** : ` /lend-app/loan-status/ `

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
        "status_name": "[status_name]"
    },
    ...
]
```

## Metoda: ` GET ITEM `

- **URL** : ` /lend-app/loan-status/<int:pk> `

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Status o podanym id istnieje

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "status_name": "[status_name]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Status o podanym id nie istnieje

- **Status** : ` 404 Not found `

- **Zawartość** :

```json
{
    "detail": "Not found."
}
```
