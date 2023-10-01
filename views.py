from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)

def home(request):
    
    html = """
    <html>
    <head><title>Главная страница</title></head>
    <body>
    <h1>Добро пожаловать!</h1>
    </body>
    </html>
    """
    
    
    logger.info('Посещение главной страницы')

    return HttpResponse(html)

def about(request):
    html = """
    <html>
    <head><title>О себе</title></head>
    <body>
    <h1>Обо мне</h1>
    <p>Привет, меня зовут Юрий.</p>
    </body>
    </html>
    """
    

    logger.info('Посещение страницы "О себе"')

    return HttpResponse(html)
