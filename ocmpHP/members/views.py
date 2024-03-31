from django.shortcuts import render
from .models import Member

# Create your views here.

def member_page(request):
    members_all = Member.objects.filter(is_public=True)
    members_PhD = Member.objects.filter(is_public=True, is_PhD=True)
    members_master2 = Member.objects.filter(is_public=True, is_Master2=True)
    members_master1 = Member.objects.filter(is_public=True, is_Master1=True)
    members_bachelor = Member.objects.filter(is_public=True, is_Bachelor=True)
    contents = {'members_all':members_all, 'members_PhD': members_PhD, 'members_master2': members_master2, 'members_master1': members_master1, 'members_bachelor': members_bachelor}
    return render(request, 'members.html', contents)