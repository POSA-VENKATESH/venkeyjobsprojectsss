
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','maheshjobs.settings')
import django
django.setup()

from testapp.models import HydJobs,PuneJobs,BngJobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
    d1 = randint(6,9)
    num = "" + str(d1)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)
def bnpopulate(n):
    #['date','company','title','eligibility','address','email','phonenumber']
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','Phd','Mahesh Sir Student'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_record = BngJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
            )
n = int(input("Enter number of records:"))
bnpopulate(n)
print(f'{n} Records inserted successfully......')
