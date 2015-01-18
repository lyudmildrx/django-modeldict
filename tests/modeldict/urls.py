from django.conf.urls import patterns, url, include

def dummy_view(request):
    from django.http import HttpResponse
    return HttpResponse()

urlpatterns = patterns('',
    url(r'^$', dummy_view, name='modeldict-home'),
)