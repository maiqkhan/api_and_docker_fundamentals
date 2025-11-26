import json
from fastapi import FastAPI
import uvicorn
from enum import Enum
from pydantic import BaseModel, Field

class WatchlistEntry(BaseModel):
    user: str = Field(...)
    title: str = Field(max_length=20)
    recommend: bool
    rating: int = Field(le=5)

watchlist_db = [
    {"user": "Mustafa", "title": "Naruto", "recommend": True, "rating": 5},
    {"user": "Mustafa", "title": "Bleach", "recommend": False, "rating": 2},
    {"user": "Teresa", "title": "Detective Konan", "recommend": True, "rating": 5},
    {"user": "Tasfiah", "title": "Attack on Titan", "recommend": True, "rating": 5},
]

class UserName(str, Enum):
    Mustafa = "Mustafa"
    Teresa = "Teresa"
    Tasfiah = "Tasfiah"


app = FastAPI(title="Anime watchlist Tracker")

@app.get("/")
def root():
    return {"greeting": "Welcome to anime watchlist!"}

@app.get("/watchlists")
def get_all_watchlists():
    return watchlist_db

@app.get("/watchlists/{user_name}")
def get_user_watchlist(user_name: UserName):
    user_watchlist = []
    for watchlist_entry in watchlist_db:
        if watchlist_entry['user'] == user_name.value:
            user_watchlist.append(watchlist_entry)
    
    return user_watchlist

@app.post("/watchlists/")
def add_user_watchlist(watchlist_entry: WatchlistEntry):
    print(watchlist_entry)
    print(watchlist_entry.model_dump())

    watchlist_db.append(watchlist_entry.model_dump())

    return {"status": "Success", "message": f"Thanks {watchlist_entry.user}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
