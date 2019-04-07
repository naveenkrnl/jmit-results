import csv
import time
import os,sys,uuid
sys.path.append("/home/naveen/djangoecom/ecommerce/scrapper/dealnloot")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'results.settings')
try:
        from django.core.management import execute_from_command_line
except ImportError as exc:
        raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
) from exc
execute_from_command_line(sys.argv)
from result.models import ResultData


def create_data():
        ResultData.objects.create()
        

def getcsvdata():
    a=open('onlinetest.csv')
    red=csv.reader(a)
    # print(red[0])
    for row in red:
        ID=row[0]
        username=row[1]
        marks=int(row[2])
        percentage=float(row[3])
        position=row[4]
        if position is "":
                position=10
        email=row[5]
        fullname=row[6]
        dob=row[7]
        phonenumber=row[8]
        schoolname=row[9]
        rollno=row[10]
        fathersname=row[11]
        gender=row[12][2:]
        obj=ResultData(studentid=ID,username=username,email=email,fullname=fullname,phonenumber=phonenumber,fathersname=fathersname,schoolname=schoolname,gender=gender,stream='Non-Medical',dob=dob,rollno=rollno,marks=marks,percentage=percentage,position=position)
        obj.save()
        print(ID,username,marks,percentage,position,email,fullname,dob)
        print(phonenumber,schoolname,rollno,fathersname,gender)


if __name__=='__main__':
        getcsvdata()
        # create_data()