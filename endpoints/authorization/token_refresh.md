# TOKEN REFRESH

Służy do odnowiednia ważności tokenu dostępu/przedłużenia sesji.

## Method: ` POST `

- **URL** : `/auth/token-refresh/`

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : 
```json
{
    "refresh": "[refresh_token]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podany refresh token jest poprawny 

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "access": "[access_token]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Podany refresh token nie jest poprawny lub ważność tokenu wygasła 

- **Status** : ` 401 Unauthorized `

- **Zawartość** :

```json
{
    "detail": "Token is invalid or expired",
    "code": "token_not_valid"
}
```
