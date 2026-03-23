from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# =========================
# 📦 Modèle Article
# =========================
class Article(BaseModel):
    title: str
    content: str
    author: str
    category: str

# =========================
# 📚 Base de données (mémoire)
# =========================
articles = [
    {
        "title": "Bienvenue sur mon blog",
        "content": "Ceci est mon premier article",
        "author": "Elie",
        "category": "Tech"
    },
    {
        "title": "API FastAPI",
        "content": "Projet backend déployé sur Fly.io",
        "author": "Elie",
        "category": "Programmation"
    }
]

# =========================
# 🌐 Route principale
# =========================
@app.get("/")
def home():
    return {
        "message": "Bienvenue sur mon blog API",
        "status": "fonctionnel",
        "version": "1.0"
    }

# =========================
# 📄 Voir tous les articles
# =========================
@app.get("/articles")
def get_articles():
    return articles

# =========================
# ➕ Ajouter un article
# =========================
@app.post("/articles")
def create_article(article: Article):
    new_article = article.dict()
    articles.append(new_article)
    return {
        "message": "Article ajouté avec succès",
        "article": new_article
    }
