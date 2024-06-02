from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(validators=[],max_length=30)
    email = models.EmailField()
    Roll=models.IntegerField()
    Float_valur= models.FloatField()
    Auto = models.AutoField(primary_key=True)
    BigInt = models.BigIntegerField()
    Binary = models.BinaryField()
    Boolean = models.BooleanField()
    Date = models.DateField()
    Date_Time  = models.DateTimeField()
    Time= models.TimeField()
    Decimal=models.DecimalField(max_digits=5, decimal_places=2)
    Duration= models.DurationField()
    File_uplode = models.FileField(upload_to='files/')
    Image = models.ImageField(upload_to='images/')
    # File_path=models.FilePathField(path='/path/to/files/')
    # foreign_key = models.ForeignKey(Roll, on_delete=models.CASCADE)
    IP_address= models.GenericIPAddressField()
    Json= models.JSONField()
    # many= models.ManyToManyField()
    NUll = models.BooleanField(null=True,blank=True)
    # one_to_one=models.OneToOneField(OtherModel, on_delete=models.CASCADE)
    positiv_Int= models.PositiveBigIntegerField()
    positiv_small= models.PositiveSmallIntegerField()
    scug=models.SlugField()
    comment= models.TextField()
    url=models.URLField()
    uuid=models.UUIDField()







    
    # def __str__(self):
    #     return self.first_name
