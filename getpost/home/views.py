from django.shortcuts import render
from django.http import HttpResponse
import logging
import html

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    logging.error('Index was called...')
    response = """<html><body><p>Welcome to sample getpost code</p><ul>
    <li><p><a href="dump">Dump Request GET and POST</p></li>
    <li><p><a href="guess">Play a guessing game</p></li>
    </ul></body></html>"""
    return HttpResponse(response)

def dump(request):
    response = '<p>Dumping the POST data...</p>'

    response += '''<form method="post">
        <p><label for="abc123">Tsugi</label>
        <input type="text" name="tsugi" size="40" id="abc123"/><br/>
        <label for="xyzzy">SakaiCar</label>
        <input type="text" name="sakaicar" size="40" id="xyzzy"/><br/>
        <input type="submit"/></p>
        </form><hr/>
        '''
    response += '<p>Incoming GET data:<br/>\n'
    for key, value in request.GET.items():
        response += html.escape(key) + '=' + html.escape(value) + '</br>\n'
    response += '</p>\n'


    response += '<p>Incoming POST data:<br/>\n'
    for key, value in request.POST.items():
        response += html.escape(key) + '=' + html.escape(value) + '</br>\n'
    response += '</p>\n'

    return HttpResponse(response)

def guess(request):
    response = '<p>Guessing game...</p>'
    guess = request.POST.get('guess')
    msg = False
    if guess :   # We have a guess in POST data
        try:
            if int(guess) < 42 : 
                msg = 'Guess too low'
            elif int(guess) > 42 : 
                msg = 'Guess too high'
            else:
                msg = 'Congratulations!'
        except:
            msg = 'Bad format for guess:' + html.escape(guess)
        
    if msg : 
        response += '<p>' + msg + '</p>\n'

    response += '''<form method="post">
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="submit"/>
        </form>
        '''

    return HttpResponse(response)

