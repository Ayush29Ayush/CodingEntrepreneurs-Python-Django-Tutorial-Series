"""
To render HTML pages
"""
from django.http import HttpResponse
import random
from articles.models import Article

def home_view(request):
    name = "Ayush Senapati"
    number = random.randint(1,100)
    # HTML_STRING1 = f"""
    # <h1>Hello {name} - {number}</h1>
    # """
    # HTML_STRING2 = f"""
    # <h1>Hello {name} - {number}</h1>
    # """
    article_obj = Article.objects.get(id=2)
    article_title = article_obj.title
    
    article_content = article_obj.content
    return HttpResponse(HTML_STRING1 + HTML_STRING2)