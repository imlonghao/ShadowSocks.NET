from django.db import models

class Account(models.Model):
    ip = models.IPAddressField()
    port = models.CharField(max_length=5)
    password = models.CharField(max_length=30)
    encryption = models.CharField(max_length=16)
    country = models.CharField(max_length=15)
    etime = models.CharField(max_length=10)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    spdy = models.IntegerField(max_length=1)
    api = models.CharField(max_length=10)
    qr = models.ImageField(upload_to='qr')
    status = models.CharField(max_length=1,choices=(('0',u'\u5F85\u5BA1'),('1',u'\u6B63\u5E38'),))
    is_on = models.IntegerField(max_length=1)
    def __unicode__(self):
        return "%s %s:%s" % (self.ip,self.status,self.is_on)

class Link(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()
    def __unicode__(self):
        return self.url

class Flag(models.Model):
    country = models.CharField(max_length=15)
    flag = models.ImageField(upload_to='flags')
    def __unicode__(self):
        return self.country
