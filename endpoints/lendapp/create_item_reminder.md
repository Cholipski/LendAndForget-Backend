# SET REMINDING NOTIFICATION - ITEM

Służy do utworzenia przypomnienia zwrotu dla pożyczonego przedmiotu

## Metoda: ` POST `

- **URL** : ` /lend-app/create-item-reminder/ `

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** :
```json
{
    "id": "[id]",
    "date": "[date]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : W bazie danych istnieje przedmiot o podanym id oraz wprowadzona data jest w poprawnym formacie YYYY-MM-DD

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": 200
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : W bazie danych nie istnieje przedmiot o podanym id lub wprowadzona data jest w niepoprawnym formacie

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": 403
}
```

- **Warunek wystąpienia** : Istnieje już przypomnienie na podany dzień

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": 400,
}
```
