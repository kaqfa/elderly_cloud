from django.shortcuts import render


def load_page(request, page = None):
    if page == None:
        return render(request, 'index.html')

    return render(request, page+'.html')
