from django.db import models


# Create your models here.
class Datacenter(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Vlan(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    datacenter = models.ForeignKey(Datacenter, null=False, default=1)

    def __unicode__(self):
        return self.name


class VlanGroup(models.Model):
    name = models.CharField(max_length=50)
    datacenter = models.ForeignKey(Datacenter, null=False, default=1)

    def __unicode__(self):
        return self.name


class VlanGroupContainsVlans(models.Model):
    vlanGroup = models.ForeignKey(VlanGroup)
    vlan = models.ForeignKey(Vlan)

    def __unicode__(self):
        return self.vlanGroup + self.vlan


class Device(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=True)
    os = models.CharField(max_length=50)
    ip = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    datacenter = models.ForeignKey(Datacenter, null=False, default=1)

    def __unicode__(self):
        return self.name


class DeviceContainsVlans(models.Model):
    device = models.ForeignKey(Device)
    vlan = models.ForeignKey(Vlan)

    def __unicode__(self):
        return self.device + self.vlan


class DeviceContainsVlanGroups(models.Model):
    device = models.ForeignKey(Device)
    vlanGroup = models.ForeignKey(VlanGroup)

    def __unicode__(self):
        return self.device + self.vlanGroup
