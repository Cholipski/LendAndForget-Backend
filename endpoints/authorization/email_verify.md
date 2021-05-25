# EMAIL VERIFY

Służy do aktywacji konta użytkownika z wykorzystaniem przesłanego w wiadomości email tokenu
## Method: ` POST `

- **URL** : `/auth/email-verify/`

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : 
```
    token
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podany token jest poprawny

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": "success", 
    "message": "Successfully activated"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Ważność podanego tokenu wygasła 

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": "failed", 
    "message": "Activation expired"
}
```

- **Warunek wystąpienia** : Podany token jest niepoprawny 

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": "failed", 
    "message": "Invalid token"
}
```
