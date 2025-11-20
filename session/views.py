from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    # Use session
    count = request.session.get('hello_count', 0)
    request.session['hello_count'] = count + 1

    # Render page that includes the required string
    context = {
        'required_token': '18642f54',
        'count': request.session['hello_count'],
    }
    # If you prefer render, assign to a variable so you can set cookie on it.
    response = render(request, 'hello/hello.html', context)

    # Set the required cookie
    response.set_cookie('dj4e_cookie', '18642f54', max_age=1000)

    return response

# https://docs.djangoproject.com/en/4.2/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', 
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval : 
        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close
    else : 
        resp.set_cookie('zap', 42) # No expired date = until browser close
    resp.set_cookie('sakaicar', 42, max_age=1000) # seconds until expire
    return resp

# https://www.youtube.com/watch?v=Ye8mB6VsUHw

def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    return resp

