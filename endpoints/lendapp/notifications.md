# NOTIFICATIONS

Służy do zarządzania powiadomieniami 

## Metoda: ` POST `

- **URL** : ` /lend-app/notifications/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : 
```json
{
    "title": "[title]",
    "description": "[description]",
    "is_seen": "[is_seen]",
    "show_date": "[show_date]",
    "receiver_id": "[reveiver_id]"
}
```

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany

- **Status** : ` 201 Created `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "title": "[title]",
    "description": "[description]",
    "is_seen": "[is_seen]",
    "show_date": "[url]",
    "receiver_id": "[receiver_id]",
    "frontend_url": "[frontend_url]"
}
```

## Metoda: ` GET LIST `

- **URL** : ` /lend-app/notifications/ `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany 

- **Status** : ` 200 OK `

- **Zawartość** :
```json
[
    {
        "pk": pk,
        "url": "[url]",
        "title": "[title]",
        "description": "[description]",
        "is_seen": "[is_seen]",
        "show_date": "[show_date]",
        "receiver_id": receiver_id,
        "frontend_url": "[frontend_url]"
    },
    ...
]
```

## Metoda: ` GET ITEM `

- **URL** : ` /lend-app/notifications/<int:pk> `

- **Czy wymagana autoryzacja** : TAK

- **Wymagane dane** : brak

### Odpowiedź pozytywna

- **Warunek wystąpienia** : Użytkownik jest zalogowany oraz powiadomienie o takim id istnieje

- **Status** : ` 200 OK `

- **Zawartość** :
```json
{
    "pk": pk,
    "url": "[url]",
    "title": "[title]",
    "description": "[description]",
    "is_seen": "[is_seen]",
    "show_date": "[show_date]",
    "receiver_id": receiver_id,
    "frontend_url": "[frontend_url]"
}
```
