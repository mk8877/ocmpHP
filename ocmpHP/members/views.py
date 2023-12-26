from django.shortcuts import render

# Create your views here.

def member_page(request):
    return render(request, 'members.html')