from django.db import models


GENDER = (
    ('m', 'MALE'),
    ('f', 'FEMALE'),
    ('o', 'OTHER')
)

TEE_SIZE = (
    ('xs', 'XS'),
    ('s' , 'S'),
    ('m' , 'M'),
    ('l' , 'L'),
    ('xl', 'XL')
    )


class Register(models.Model):

    phno = models.CharField(max_length=20)
    fullname = models.CharField(max_length=100, null=True)
    emailid = models.EmailField(max_length=50)
    gender = models.CharField(max_length=100, choices=GENDER)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200,null=True)
    teesize = models.CharField(max_length=100, choices=TEE_SIZE)
    expr = models.IntegerField(null=True, blank=True)
    bibno = models.IntegerField(null=True, blank=True, default=0)
    start = models.TimeField(null=True, blank=True)
    finish = models.TimeField(null=True, blank=True)
    split = models.TimeField(null=True, blank=True)


    def __str__(self):
        return self.fullname
