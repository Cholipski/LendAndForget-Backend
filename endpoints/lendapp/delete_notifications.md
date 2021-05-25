# DELETE NOTIFICATIONS

Służy do usuwania pojedynczych powiadomień

## Metoda: ` DELETE `

- **URL** : ` /lend-app/delete-notifications/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```
    pk
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Powiadomienie o takim id istnieje

- **Status** : ` 200 OK `

- **Zawartość** :
```
    "Successfully notification deleted"
```

### Odpowiedź negatywna

- **Warunek wystąpienia** : Powiadomienie o takim id nieistnieje lub użytkownik nie ma do niego dostępu 

- **Status** : ` 400 Bad request `

- **Zawartość** :
```
   "Notification not found"
```
