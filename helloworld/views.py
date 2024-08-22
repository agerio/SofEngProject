from django.shortcuts import render
from helloworld.models import HelloWorld

# Create your views here.
def hello_world(request):
    textFromPsql = HelloWorld.objects.all().first().text
    context = {'text': textFromPsql}
    return render(request, "helloworld.html", context)