from django.http import HttpResponse # only used in class

def home(request):
    html = """
    <h1>Welcome to Route Demo Home</h1>
    <h3>You got here via {}</h3>
    """.format(request.path)
    return HttpResponse(html)
