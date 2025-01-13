# Flash News

Flash News is a dynamic and responsive web application built using the Django framework. It allows users to stay updated with the latest news in real-time by leveraging the power of the News API for fetching news articles. The app features a user-friendly interface designed with HTML and CSS for seamless navigation and an engaging user experience.

---

## Features
- Real-time news updates from multiple sources.
- Responsive and intuitive user interface.
- Search functionality to find news articles by keywords.
- Categorized news for easy navigation (e.g., Business, Technology, Sports).

---

## Technologies Used
- **Backend:** Django Framework (Python)
- **Frontend:** HTML, CSS
- **API Integration:** News API
- **Database:** SQLite (default Django database)

---

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (version 3.8 or higher)
- pip (Python package manager)
- Django (version 4.0 or higher)

Additionally, you need a valid **News API key**. Sign up at [News API](https://newsapi.org/) to obtain one.

---

## Installation and Setup
Follow these steps to set up and run the Flash News application locally:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/flash-news.git
cd flash-news
```

### 2. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

---

## Step-by-Step Development Guide

### 1. Set Up the Django Project
```bash
django-admin startproject flash_news
cd flash_news
```

### 2. Create the News App
```bash
python manage.py startapp news
```

### 3. Register the App in `settings.py`
Add `news` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'news',
]
```

### 4. Set Up Models
Define the structure of your news articles in the `models.py` file of the `news` app.

Example:
```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title
```

### 5. Fetch Data from News API
Create a service function in `news/utils.py` to fetch articles:

```python
import requests
import os

def fetch_news():
    api_key = os.getenv('NEWS_API_KEY')
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    return response.json()
```

### 6. Create Views and Templates
- Define views in `views.py` to display articles:

```python
from django.shortcuts import render
from .utils import fetch_news

def home(request):
    articles = fetch_news().get('articles', [])
    return render(request, 'news/home.html', {'articles': articles})
```

- Create a `templates/news/home.html` file for the frontend:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flash News</title>
    <link rel="stylesheet" type="text/css" href="/static/css/style.css">
</head>
<body>
    <h1>Flash News</h1>
    <div class="news-container">
        {% for article in articles %}
            <div class="news-article">
                <h2>{{ article.title }}</h2>
                <p>{{ article.description }}</p>
                <a href="{{ article.url }}" target="_blank">Read more</a>
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

### 7. Add Static Files for Styling
- Create a `static/css/style.css` file for custom styling.

Example:
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.news-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    padding: 20px;
}

.news-article {
    background: white;
    border: 1px solid #ddd;
    padding: 15px;
    border-radius: 5px;
    width: 300px;
}
```

### 8. Add URL Patterns
Define URL routes in `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

---

## Future Enhancements
- User authentication for personalized news feeds.
- Add support for news categories.
- Save articles for offline reading.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this application.

---

## Support
If you encounter any issues, feel free to [open an issue](https://github.com/Shakir555/flash_news/issues).

