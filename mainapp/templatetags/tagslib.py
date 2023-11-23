from django import template
import os, json
from django.template.defaultfilters import stringfilter
register = template.Library()
@register.filter(name="orderava")
def orderava(nick: str): # Из Hello_World получаем Hello World
    if not os.path.isfile(f"C:/Users/dos12/.vscode/re_self/mainapp/media/{nick}.png"):
        y = "/static/images/nop.png"
    else:
        y = f"/media/{nick}.png"
    return y
@register.simple_tag
def get_companion(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None
@register.simple_tag
def get_url(request):
    host = request.META["HTTP_HOST"]
    return host
@register.filter
def decode(x):
    x = x.replace("'", '"')
    return json.loads(x)
@register.simple_tag
def get_el(dct, key, i):
    return dct[key][i]
@register.filter
def keyscount(dct):
    dct = json.loads(dct)
    return len(list(dct.keys()))
@register.filter
@stringfilter
def get_chat(chaat):
    print("aaa", chaat)
    chaat = json.loads(chaat.replace("'", "'"))
    return sorted(list(chaat.keys()))
