from django.db import models





qua=(("BHMS","BHMS"),("BAMS","BAMS"),("MBBS","MBBS"),("Physiotherapists","Physiotherapists"),('MD','MD'))
gen=(('male','male'),('female','female'))
qu=(("BSC Nursing","BSC Nursing"),("Graduation+Nursing Course","Graduation+Nursing Course"))

class Ambulance(models.Model):
    patient_name=models.CharField(max_length=50)
    patient_age=models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)

    def __str__(self):
        return self.patient_name


class Appointment(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    previous_visit = models.CharField(max_length=50)
    if_before_visited_visit_detail = models.CharField(max_length=50)
    appointment_date = models.DateField()
    slot=models.CharField(max_length=30)
    contact_number=models.CharField(max_length=30)

    def __str__(self):
        return self.name



class Doctor(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=50,choices=gen)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=50, choices=qua)
    aadhaar_number = models.CharField(max_length=50)

class NursingStaff(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=gen)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    qualification = models.CharField(max_length=50, choices=qu)
    aadhaar_number = models.CharField(max_length=50)

class RoomServiceStaff(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=50, choices=gen)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
    aadhaar_number = models.CharField(max_length=50)


class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    price = models.IntegerField()
    description = models.CharField(max_length=200,default='',null=True,blank=True)
    image = models.ImageField(upload_to='images',default='')
    def __str__(self):
        return self.name




class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='total_orders')
    quantity = models.IntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-ordered_date',)

