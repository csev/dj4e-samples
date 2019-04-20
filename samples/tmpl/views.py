from django.shortcuts import render
from django.views import View

# Create your views here.

def simple(request):
    return render(request, 'tmpl/simple.html')

def guess(request) :
    context = {'zap' : '42' }
    return render(request, 'tmpl/guess.html', context)

def special(request) :
    context = {'txt' : '<b>bold</b>',
               'zap' : '42' }
    return render(request, 'tmpl/special.html', context)

def loop(request) :
    f = ['Apple', 'Orange', 'Banana', 'Lychee']
    n = ['peanut', 'cashew']
    x = {'fruits' : f, 'nuts' : n, 'zap' : '42' }
    return render(request, 'tmpl/loop.html', x)

def cond(request) :
    x = {'guess' : '42' }
    return render(request, 'tmpl/cond.html', x)

def nested(request) :
    x = {'outer' : { 'inner' : '42' } }
    return render(request, 'tmpl/nested.html', x)
    
# Call this with a parameter number
class GameView(View) :
    def get(self, request, guess) :
        x = {'guess' : int(guess) }
        return render(request, 'tmpl/cond.html', x)

# Using inheritance (extend)
class Game2View(View) :
    def get(self, request, guess) :
        x = {'guess' : int(guess) }
        return render(request, 'tmpl/cond2.html', x)

