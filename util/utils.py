

def checkguess(request) :
    guess = request.GET.get('guess','')
    return guess == '42';
