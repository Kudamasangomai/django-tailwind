from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    q = 'apple'
    url = ('https://newsapi.org/v2/everything?'
           'q={q}&'
           'from=2022-12-31&'
           'sortBy=popularity&'
           'pageSize=6&'
           # 'apiKey=891989b755b444e8961fe285fa8ccfd2'
           'apiKey=8ba8c66b432e45d691ba3d74b1850436'
           )

    response = requests.get(url)
    q = response.json()
    context = {

        'news': q['articles']

    }
    return render(request, 'main/home.html', context)


def search_news(request):
     url = ('https://newsapi.org/v2/everything?'
           'q={}&'
           'from=2022-12-31&'
           'sortBy=popularity&'
           'pageSize=6&'
           'apiKey=8ba8c66b432e45d691ba3d74b1850436'
           )
     if request.method == 'POST':
       searchedq = request.POST.get('searchq')
       q = requests.get(url.format(searchedq)).json()
       context = {

        'news': q['articles']

        }
       return render(request, 'main/articles.html', context)

def sources(request):
    url =('https://newsapi.org/v2/top-headlines/sources?apiKey=8ba8c66b432e45d691ba3d74b1850436')
    response = requests.get(url)
    q = response.json()
    context = {

        'sources': q['sources']

        }
    return render(request, 'main/sources.html', context)
       