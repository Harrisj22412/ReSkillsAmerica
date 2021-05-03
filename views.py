from django.http import HttpResponse

# Create your views here.

data = {
    ' Name : Jalen Harris',
    ' City : Washington, DC',
    ' Course : Banckend, Python',
    " Message :" " Focused on being a valuable part of any team I am on and believe in the team rising together. "
}

def index(request):
    return HttpResponse(data)