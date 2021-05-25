# MARK ALL NOTIFICATION AS SEEN

Służy do odznaczania wszystkich powiadomień użytkownika jako przeczytane

## Metoda: ` POST `

- **URL** : ` /lend-app/all-notifications-mark-seen/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```
    pk
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany 

- **Status** : ` 200 OK `

- **Zawartość** :
```
    "Successfully set all notification as seen"
```


