# REGISTER

Służy do zarejestrowania konta użytkownika

## Method: ` POST `

- **URL** : `/auth/register/`

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : 
```json
{
    "username": "[username]",
    "email": "[email]",
    "first_name": "[first_name]",
    "last_name": "[last_name]",
    "password": "[password]",
    "confirm_password": "[confirm_password]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Podane dane do rejestracji są poprawne

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "username": "[username]",
    "email": "[email]",
    "first_name": "[first_name]",
    "last_name": "[last_name]"
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Użytkownik o podanym username już istnieje w bazie danych
- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "username": [
        "A user with that username already exists."
    ]
}
```

- **Warunek wystąpienia** : Użytkownik o podanym adresie email już istnieje w bazie danych
- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "email": [
        "Account with this email exists!"
    ]
}
```

- **Warunek wystąpienia** : Brak zgodności haseł
- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "password": [
        "Passwords must match!"
    ]
}
```

- **Warunek wystąpienia** : Użytkownik podał hasło krótsze niż 8 znaków
- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "password": [
        "Ensure this field has at least 8 characters."
    ],
    "confirm_password": [
        "Ensure this field has at least 8 characters."
    ]
}
```

- **Warunek wystąpienia** : Użytkownik podał nieprawidłowy format adresu email
- **Status** : ` 400 Bad request `

- **Zawartość** :

```json
{
    "email": [
        "Enter a valid email address."
    ]
}
```





