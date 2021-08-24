# REQUEST EARLIER RETURN - MONEY

Służy do wysłania powiadomienia dłużnikowi z prośbą o wcześniejszy zwrot gotówki

## Metoda: ` POST `

- **URL** : ` /lend-app/request-money-return/ `

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

- **Warunek wystąpienia** : W bazie danych nie istnieje wypożyczenie gotówki o podanym id

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": 403
}
```
