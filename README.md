# MangAdvisor

API backend pour MangAdvisor, une plateforme de recommandation de manga et d'anime.

## Structure du Projet

```
mangadvisor/
├── app/
│   ├── api/
│   │   └── v1/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   └── services/
├── tests/
├── alembic/
├── .env
└── requirements.txt
```

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer les variables d'environnement :
- Copier `.env.example` vers `.env`
- Modifier les variables selon votre configuration

## Développement

### Lancer le serveur de développement
```bash
uvicorn app.main:app --reload
```

### Tests
```bash
pytest
```

### Migration de base de données
```bash
alembic upgrade head
```

## Conventions de Code

- Utilisation de Black pour le formatage
- Respect de PEP 8
- Tests unitaires obligatoires pour les nouvelles fonctionnalités
- Messages de commit descriptifs

## Branches

- `main` : Production
- `develop` : Développement principal
- `feature/*` : Nouvelles fonctionnalités
- `bugfix/*` : Corrections de bugs
- `release/*` : Préparation des releases

## API Documentation

Une fois le serveur lancé, la documentation de l'API est disponible à :
- Swagger UI : `http://localhost:8000/docs`
- ReDoc : `http://localhost:8000/redoc` 