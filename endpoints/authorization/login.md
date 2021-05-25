# LOGIN

Słyży do pobierania tokenu dla zarejestrowanego użytkownika.

## Metoda: ` POST `

- **URL** : `/auth/`

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : 
```json
{
    "username": "[username]",
    "password": "[password]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podane dane do logowania są poprawne

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "refresh": "[refresh token]",
    "access": "[access token]",
    "username": "[username]",
    "email": "[email]",
    "id": id
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Podane dane do logowania są niepoprawne

- **Status** : ` 401 Unauthorized `

- **Zawartość** :

```json
{
    "detail": "No active account found with the given credentials"
}
```
