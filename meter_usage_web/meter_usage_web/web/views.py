from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('pages/home.html')
    context = {
        'start_date': "2019-01-01",
        'end_date': "2019-01-31",
    }
    return HttpResponse(template.render(context, request))
