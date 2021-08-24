# REQUEST LONGER RETURN TIME - ITEM

Służy do wysłania prośby właścicielowi przedmiotu o przedłużenie terminu zwrotu

## Metoda: ` POST `

- **URL** : ` /lend-app/request-item-longer-time/ `

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
