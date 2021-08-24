# USER MANAGE

Służy do pobrania danych zalogowanego użytkownika

## Metoda: ` GET `

- **URL** : `/auth/user-manage/`

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany 

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "username": "[username]",
    "email": "[email]",
    "first_name": "[first_name]",
    "last_name": "[last_name]",
    "phone": phone
}
```

## Metoda: ` PUT `

- **URL** : `/auth/user-manage/`

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```json
{
    "first_name": "[first_name || empty]",
    "last_name": "[last_name || empty]",
    "phone":"[phone || empty]",
    "old_password":"[old_password || empty]",
    "new_password":"[new_password || empty]",
    "re_password":"[re_password || empty]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowowany oraz podane dane są poprawne

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": "Data changed successfully"
}
```

### Odpowiedź neutralna

- **Warunek wystąpienia** :  Użytkownik jest zalogowowany oraz nie podał danych (wszystkie pola są puste)

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": [
        "Nothing was changed"
    ]
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Użytkownik nie jest zalogowany lub nie wypełnił poprawnie wszystkich pól

- **Status** : ` 400 BAD REQUEST`

- **Zawartość** :

```json
{
    "status": "Something went wrong"
}
```

## Metoda: ` DELETE `

- **URL** : `/auth/user-manage/`

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany 

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": "success",
    "message": "Successfully account deleted"
}
```

