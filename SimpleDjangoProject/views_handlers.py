from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings



def maintenance(the_func):
    """
    Make another a function more beautiful.
    """
    def _decorated(*args, **kwargs):
        if settings.MAINTENANCE_MOD:
            print('MAINTENANCE MOD ON')
            return render(*args, 'maintenance.html', {})
        else:
            return the_func(*args, **kwargs)
    return _decorated


@maintenance
def page_one(request):

    return render(request, 'page1.html')

@maintenance
def page_two(request):

    return render(request, 'page2.html')
