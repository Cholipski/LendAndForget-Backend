# CONTACT    

Służy do pobierania i usuwania kontaktów. 

## Metoda: ` GET LIST `

- **URL** : ` /lend-app/contact/ `

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
        "user_id": user_id,
        "friend_id": friend_id,
        "friend_first_name": "[friend_first_name]",
        "friend_last_name": "[friend_last_name]",
        "friend_email": "[friend_email]"
    },
    ...
]
```

## Metoda: ` GET ITEM `

- **URL** : ` /lend-app/contact/<int:pk> `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "user_id": user_id,
    "friend_id": friend_id,
    "friend_first_name": "[friend_first_name]",
    "friend_last_name": "[friend_last_name]",
    "friend_email": "[friend_email]"
}
```

## Metoda: ` DELETE `

- **URL** : ` /lend-app/contact/<int:pk> `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```
    id
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Kontakt o podanym id istnieje

- **Status** : ` 200 OK `

- **Zawartość** :
```
    "Successfully friend deleted"
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Kontakt o podanym id nieistnieje

- **Status** : ` 400 Bad request `

- **Zawartość** :

```
    "Friend not found"
```
