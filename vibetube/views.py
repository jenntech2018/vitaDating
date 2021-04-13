from django.shortcuts import render

def page_not_found_view(request):
     return render(request,'myapp/404.html')