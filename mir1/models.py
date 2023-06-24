from django.db import models
import datetime
# Create your models here.


class users(models.Model):
    user_id = models.IntegerField(max_length=5, primary_key = True)
    user_name = models.CharField(max_length= 100)
    phone_number = models.BigIntegerField()
    email=models.EmailField(max_length=50)
    userstatechoices=[('1','Andhra Pradesh'),('2','Arunachal Pradesh'),('3','Assam'),('4','Bihar'),('5','Chhattisgarh'),('6','Goa'),('7','Gujarat'),('8','Haryana'),('9','Himachal Pradesh'),('10','Jharkhand'),('11','Karnataka'),('12','Kerala'),('13','Madhya Pradesh'),('14','Maharashtra'),('15','Manipur'),('16','Meghalaya'),('17','Mizoram'),('18','Nagaland'),('19','Odisha'),('20','Punjab'),('21','Rajasthan'),('22','Sikkim'),('23','Tamil Nadu'),('24','Telangana'),('25','Tripura'),('26','Uttarakhand'),('27','Uttar Pradesh'),('28','West Bengal'),]
    user_state = models.CharField(max_length = 30, choices = userstatechoices)
    user_type = models.CharField(max_length = 10)
    view_level = models.IntegerField(max_length=1)
    def __str__(self):
	    return self.user_name