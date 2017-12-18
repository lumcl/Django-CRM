import json

from django.db import models


# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=10)
    pid = models.IntegerField()
    tel = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    position = models.CharField(max_length=30)
    department = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def json(self):
        return "{{\"name\":\"{}\",\"pid\":\"{}\",\"tel\":\"{}\",\"phone\":\"{}\",\"email\":\"{}\",\"position\":\"{}\",\"department\":\"{}\"}}".format(
            self.name,
            self.pid,
            self.tel,
            self.phone,
            self.email,
            self.position,
            self.department).replace("'", "\"")


class Activity(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    people = models.ManyToManyField(Person)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField()
    money = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

    def json(self):
        return "{{\"name\":\"{}\",\"description\":\"{}\",\"date\":\"{}\",\"time\":\"{}\",\"status\":\"{}\",\"money\":\"{}\",\"people\":{}}}".format(
            self.name,
            self.description,
            self.date,
            self.time,
            self.status,
            self.money,
            [json.loads(i.json()) for
             i in
             self.people.all()]).replace("'", "\"")


class Case(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    people = models.ManyToManyField(Person)
    activities = models.ManyToManyField(Activity)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def json(self):
        return "{{\"name\":\"{}\",\"description\":\"{}\",\"start_date\":\"{}\",\"end_date\":\"{}\",\"status\":\"{}\",\"people\":{},\"activities\":{}}}".format(
            self.name, self.description, self.start_date, self.end_date, self.status,
            [json.loads(i.json()) for i in self.people.all()],
            [json.loads(i.json()) for i in self.activities.all()]).replace("'", "\"")
