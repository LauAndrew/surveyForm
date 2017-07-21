from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, "survey/indexS.html")
# Create your views here.
def process(request):

  if request.method == "POST": 
      request.session['apple'] = request.POST['name']
      request.session['orange'] = request.POST['location']
      request.session['strawberry'] = request.POST['lang']
      request.session['mango'] = request.POST['comments']
  try:
      request.session['counter'] += 1
  except:
      request.session['counter'] = 1

  return redirect('/result')

def result(request):
    return render(request, "survey/result.html")
