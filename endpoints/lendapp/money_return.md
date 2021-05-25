# MONEY RETURN

Show all Accounts the active User can access and with what permission level.
Includes their own Account if they have one.

## Metoda: ` POST `

- **URL** : ` /lend-app/money-return/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```
    pk
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Zwrot przebiegł pomyślnie

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": 200
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Nieudany zwrot np. wypożyczenie o takim id nie istnieje lub został usunięty

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": 403
}
```
