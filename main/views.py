from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    url = ('https://newsapi.org/v2/everything?'
           'q=Pele&'
           'from=2022-12-31&'
           'sortBy=popularity&'
           'pageSize=6&'
        #   'apiKey=891989b755b444e8961fe285fa8ccfd2'
         'apiKey=8ba8c66b432e45d691ba3d74b1850436'
           )
         
    response = requests.get(url)
    q = response.json()
    context = {

    'news': q['articles']
     
    }
    return render(request, 'main/home.html',context)

 
