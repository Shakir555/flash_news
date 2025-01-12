# Libraries
from django.shortcuts import render

# Request index.html
def index(request):
    articles = [
        {'title': 'First News Article', 'content': 'This is the first article content.', 'published_date': '2025-01-12'},
        {'title': 'Second News Article', 'content': 'This is the second article content.', 'published_date': '2025-01-11'},
        {'title': 'Third News Article', 'content': 'This is the third article content.', 'published_date': '2025-01-10'},
        {'title': 'Fourth News Article', 'content': 'This is the fourth article content.', 'published_date': '2025-01-09'},
        {'title': 'Fifth News Article', 'content': 'This is the fifth article content.', 'published_date': '2025-01-08'},
        {'title': 'Sixth News Article', 'content': 'This is the sixth article content.', 'published_date': '2025-01-07'},
        {'title': 'Seventh News Article', 'content': 'This is the seventh article content.', 'published_date': '2025-01-06'},
        {'title': 'Eight News Article', 'content': 'This is the eight article content.', 'published_date': '2025-01-06'},
        {'title': 'Nine News Article', 'content': 'This is the nine article content.', 'published_date': '2025-01-06'},
    ]
    return render(request, 'index.html', {'articles': articles})
