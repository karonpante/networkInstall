from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from .models import *


# Create your views here.
def index(request, datacenter_id=None):
    datacenters = Datacenter.objects.all()

    vlans = []
    if datacenter_id is not None:
        for vlan in Vlan.objects.all():
            if vlan.datacenter.pk == int(datacenter_id):
                vlans.append(vlan)

    context = RequestContext(request, {
        'datacenters': datacenters,
        'vlans': vlans,
    })
    return render(request, 'confNetwork/index.html', context)