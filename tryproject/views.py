"""
To render HTML pages
"""
from django.http import HttpResponse
import random
from articles.models import Article

def home_view(request):
    name = "Ayush Senapati"
    random_id = random.randint(1,2)
    
    article_obj = Article.objects.get(id=random_id)
    
    HTML_STRING1 = f"""
    <h1>{article_obj.title}, id is ({article_obj.id})</h1>
    """
    HTML_STRING2 = f"""
    <p>{article_obj.content}</p>
    """
    
    return HttpResponse(HTML_STRING1 + HTML_STRING2)