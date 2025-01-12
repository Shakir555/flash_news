import requests
from django.shortcuts import render

# Request index.html with articles from News API
def index(request):
    API_KEY = '26b86b8236fc49cf80449fb701424d7a'  # Replace with your News API key
    URL = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'

    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        # Extract articles from the response
        articles = data.get('articles', [])
        news_articles = [
            {
                'title': article.get('title', 'No Title'),
                'content': article.get('description', 'No Content'),
                'published_date': article.get('publishedAt', 'No Date'),
                'url': article.get('url', '#'),
                'image_url': article.get('urlToImage', None),  # Corrected key here
            }
            for article in articles
        ]
    except requests.exceptions.RequestException as e:
        news_articles = []
        print(f"Error fetching news: {e}")

    return render(request, 'index.html', {'articles': news_articles})
