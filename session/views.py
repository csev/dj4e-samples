from django.http import HttpResponse

def myview(request):
    # Track and increment view count in session
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    
    if num_visits > 4:
        del request.session['num_visits']
        
    # Build response including the view count and required string
    resp = HttpResponse(f'view count={num_visits} ff7b1297')
    
    # Set the required cookie with the matching code string
    resp.set_cookie('dj4e_cookie', 'ff7b1297', max_age=1000)
    
    return resp
