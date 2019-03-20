from hashlib import md5
from django import template

# https://brobin.me/blog/2016/07/super-simple-django-gravatar/

register = template.Library()

@register.filter(name='gravatar')
def gravatar(user, size=35):
    email = str(user.email.strip().lower()).encode('utf-8')
    email_hash = md5(email).hexdigest()
    url = "//www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG"
    return url.format(email_hash, size)

