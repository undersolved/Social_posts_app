from fastapi import FastAPI, HTTPException  # noqa
from app.schemas import PostCreate  # noq

app = FastAPI()


text_posts = {
    1: {"title": "New Post", "content": "cool test post"},
    2: {
        "title": "Getting Started with Python",
        "content": "Python is versatile and easy to learn.",
    },
    3: {
        "title": "Morning Routine Tips",
        "content": "Start your day with a glass of water and sunlight.",
    },
    4: {
        "title": "Favorite Books of 2026",
        "content": "A curated list of must-read fiction and non-fiction.",
    },
    5: {
        "title": "Healthy Quick Lunches",
        "content": "Meal prep ideas that take under 15 minutes.",
    },
    6: {
        "title": "Introduction to APIs",
        "content": "Understanding REST, requests, and JSON responses.",
    },
    7: {
        "title": "Desk Setup Inspiration",
        "content": "Minimalist ergonomics for long coding sessions.",
    },
    8: {
        "title": "Why Walking Helps Productivity",
        "content": "Taking short 10-minute walks clears mental fog.",
    },
    9: {
        "title": "Database Basics",
        "content": "The fundamental differences between SQL and NoSQL.",
    },
    10: {
        "title": "Weekend Project Ideas",
        "content": "Fun mini-projects to build your software portfolio.",
    },
}


@app.get("/posts")
def get_all_posts(limit: int | None = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def get_post_by_id(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
