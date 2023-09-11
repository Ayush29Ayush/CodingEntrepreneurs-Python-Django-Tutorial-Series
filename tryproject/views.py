"""
To render HTML pages
"""
from django.http import HttpResponse
import random

def home_view(request):
    name = "Ayush Senapati"
    number = random.randint(1,100)
    HTML_STRING1 = f"""
    <h1>Hello {name} - {number}</h1>
    """
    HTML_STRING2 = f"""
    <h1>Hello {name} - {number}</h1>
"""
    return HttpResponse(HTML_STRING1 + HTML_STRING2)