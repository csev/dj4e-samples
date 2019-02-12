from django.shortcuts import render

# Create your views here.

def main(request) :
    host = request.META['HTTP_HOST']   # 127.0.0.1:8000
    pos = host.find(':')
    if pos > 0 :
        host = host[0:pos]
    ctx = { 'host': host}
    return render(request, 'main.html', ctx)

