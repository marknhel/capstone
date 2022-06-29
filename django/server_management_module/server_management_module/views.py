from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from ipware import get_client_ip
from getmac import get_mac_address
from register.models import User, Profile
from server_management.models import Log, Server
from django.utils import timezone
import datetime


def get_ip(request):

    ip_addr, is_routable = get_client_ip(request)

    if ip_addr is None:
        ip_addr = "0.0.0.0"

    return ip_addr


def get_mac(ip_addr):
    mac = get_mac_address(ip=ip_addr)
    if mac is None:
        return HttpResponseRedirect('htpp://10.162.165.140:8000')
    else:
        return str(mac)


def log(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    server = Server.objects.get(ip="10.162.165.138")
    log = Log(user_id = user, server = server, time_logged = datetime.datetime.now())
    log.save()
    return HttpResponseRedirect('http://10.162.165.140')

def index(request):

    try:
        user = User.objects.get(mac_address=get_mac(get_ip(request)))
    except:
        return HttpResponseRedirect(reverse('register:index'))

    user = User.objects.get(mac_address=get_mac(get_ip(request)))


    return render(request, 'server_management/index.html', { 'user' : user })
