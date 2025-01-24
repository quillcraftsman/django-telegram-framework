from django.shortcuts import render
from .models import create_info_text


def index_view(request):
    return render(request, 'demo/index.html')


def command_view(request, text):
    text = create_info_text(text)
    return render(request, 'demo/command.html', context={'text': text})


def start_command_view(request):
    return command_view(request, '/start')


def help_command_view(request):
    return command_view(request, '/help')


def links_view(request):
    return render(request, 'demo/links.html')
