from string import ascii_letters, digits
from random import choice

from .models import UrlObject
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import UrlObjectForm


def generate_shortcut():
    result = ''
    for sign in range(1, 8):
        result += choice(ascii_letters + digits)
    return result


def home_response(request):
    form = UrlObjectForm(request.POST or None)
    if form.is_valid():
        shortcut = generate_shortcut()
        instance = form.save(commit=False)
        instance.link = form['link'].value()
        instance.shortcut = shortcut
        instance.save()
        return render(request, 'new_url.html', {'shortcut': shortcut})

    return render(request, 'home.html')


def display_short_link(request, shortcut):
    return render(request, 'new_url.html', {'shortcut': shortcut})


def redirect_to_big_link(request, shortcut):
    link = get_object_or_404(UrlObject, shortcut=shortcut)
    return HttpResponseRedirect(link.link)
