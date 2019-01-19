from django.shortcuts import render
from django.http import HttpResponse
import logging
import html

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    logging.error('Top level index was called...')
    response = """<html><body><p>Welcome to DJ4E sample code</p><ul>
    <li><p><a href="form/guess">Play a guessing game</p></li>
    </ul></body></html>"""
    return HttpResponse(response)
