from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
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
    return str(get_mac_address(ip=ip_addr, network_request = True))

def _log(user_id):
#    log = Log(user_id = user_id, time_logged = timezone.now())
    server = Server.objects.get(ip="10.162.165.138")
    log = Log(user_id = user_id, server = server, time_logged = datetime.datetime.now())
    log.save()

def index(request):

    try:
        mac = User.objects.get(mac_address=get_mac(get_ip(request)))
        if mac.blocked:
#            return HttpResponse("Blocked");
            return render(request, 'server_management/blocked.html', { 'user' : mac })

    except:
        return HttpResponseRedirect(reverse('register:index'))
    user = User.objects.get(mac_address=get_mac(get_ip(request)))
    _log(user)

#    return render(request, 'server_management/index.html', { 'user' : user })
    return HttpResponseRedirect('http://192.168.16.19')
