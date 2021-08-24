# REQUEST EARLIER RETURN - ITEM

Służy do wysłania powiadomienia dłużnikowi z prośbą o wcześniejszy zwrot przedmiotu

## Metoda: ` POST `

- **URL** : ` /lend-app/request-item-return/ `

- **Czy wymagana autoryzacja** : NIE

- **Wymagane dane** : 
```json
{
    "id": "[id]",
    "date": "[date]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : W bazie danych istnieje wypożyczenie przedmiotu o podanym id

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": 200
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : W bazie danych nie istnieje wypożyczenie przedmiotu o podanym id

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": 403
}
```
