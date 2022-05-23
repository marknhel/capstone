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
#        if ip_addr == '10.162.165.140':
#            return get_mac_address()
        return HttpResponseRedirect('htpp://10.162.165.140:8000')
    else:
        return str(mac)

#    for i in nif.interfaces():
#        addrs = nif.ifaddresses(i)
#        try:
#            if_mac = addrs[nif.AF_LINK][0]['addr']
#            if_ip = addrs[nif.AF_INET][0]['addr']
#        except( IndexError, KeyError):
#            if_mac = if_ip = None
#        if if_ip == ip:
#            return if_mac

def log(request, user_id):
    user = get_object_or_404(User, pk=user_id)
#    log = Log(user = user, time_logged = timezone.now())
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

    print("Your ip address is : ", get_ip(request))
    print("Your mac address is : ", get_mac(get_ip(request)))

#    return render(request, 'server_management/index.html', { 'user' : user })
    return HttpResponseRedirect('http://10.162.168.140/log/?id=%s' % user.pk )
