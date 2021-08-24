# MARK NOTIFICATIONS AS SEEN

Służy do odznaczania pojedynczych powiadomień jako przeczytane 

## Metoda: ` POST `

- **URL** : ` /lend-app/notifications-mark-seen/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```
    pk
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Powiadomienie o tym id istnieje

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "status": 200
}
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Powiadomienie o tym id nie istnieje

- **Status** : ` 200 OK `

- **Zawartość** :

```json
{
    "status": 403
}
```
