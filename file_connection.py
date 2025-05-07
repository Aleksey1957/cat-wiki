import json


def get_articles():
    with open("articles.json", "r", encoding="utf-8") as f:
        text = json.load(f)
    return text

def save_article(name, text):
    start_text = get_articles()
    start_text[name] = text
    with open("articles.json", "w", encoding="utf-8") as f:
        json.dump(start_text, f, ensure_ascii=False)

def delete_article(name):
    text = get_articles()
    with open("articles.json", "w", encoding="utf-8") as f:
        del text[name]
        json.dump(text, f, ensure_ascii=False)

