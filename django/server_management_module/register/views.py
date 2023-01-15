from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from ipware import get_client_ip
from getmac import get_mac_address
from .models import User, Profile


def get_ip(request):

    ip_addr, is_routable = get_client_ip(request)

    if ip_addr is None:
        ip_addr = "0.0.0.0"

    return ip_addr


def get_mac(ip_addr):
    mac = get_mac_address(ip=ip_addr)
    if mac is None:
        return HttpResponseRedirect('http://10.162.165.140:8000')
    else:
        return str(mac)



def index(request):
    try:
        mac = User.objects.get(mac_address=get_mac(get_ip(request)))
        print(mac)
        if mac is not None:
            return HttpResponseRedirect('/')
    except:
        return render(request, 'register/register.html')


def _check_mac(self):
    pass

def register(request):
    if request.method == 'POST':
        _first_name = request.POST['first_name']
        _last_name = request.POST['last_name']
        _college = request.POST['college']
        _course = request.POST['course']
        _user_type = request.POST['user_type']
        _mac_addr = get_mac(get_ip(request))
        print(_mac_addr)

        new_profile = Profile(first_name = _first_name, last_name = _last_name, college = _college, course = _course)
        new_user = User(profile_id = new_profile, usertype = _user_type, mac_address = _mac_addr)
        new_profile.save()
        new_user.save()

        return HttpResponseRedirect('/')
