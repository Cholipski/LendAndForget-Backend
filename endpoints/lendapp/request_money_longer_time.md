# REQUEST LONGER RETURN TIME - MONEY

Służy do wysłania prośby właścicielowi gotówki o przedłużenie terminu zwrotu

## Metoda: ` POST `

- **URL** : ` /lend-app/request-money-longer-time/ `

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** :
```json
{
    "id": "[id]",
    "date": "[date]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : W bazie danych istnieje wypożyczenie gotówki o podanym id

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": 200
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** :  W bazie danych nie istnieje wypożyczenie gotówki o podanym id

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": 403
}
```
