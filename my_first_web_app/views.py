from random import randint
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def root(request):
    return HttpResponseRedirect('home')


def home_page(request):
    response = render(request, 'index.html')
    return HttpResponse(response)


def gallery(request):
    return HttpResponseRedirect('/portfolio/')


def portfolio(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0, 100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))

    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)


def about_me(request):
    skills = ['python', 'django', 'watching netflix']
    interests = ['sports', 'music', 'coding']

    context = {'my_skills': skills, 'my_interests': interests}
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)


def favourites(request):
    my_links = ['https://www.thescore.com/', 'https://twitter.com/']

    context = {'fave_links': my_links}
    response = render(request, 'favourites.html', context)
    return HttpResponse(response)
