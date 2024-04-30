from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    gen = [
        ("male", "male"),
        ("female", "female"),

    ]

    countries= [

        ("Nigeria", "Nigeria"),
        ("ghana", "ghana"),
        ("united kingdom", "UK"),
        ("USA", "USA"),
        ]

    ma_status= [

        ("single", "single"),
        ("married", "married"),
        ("divorce", "divorce"),
        ("complicated", "complicated"),
    ]

    state = [
        ("Abia", "Abia"),
        ("Oyo", "Oyo"),
        ("Osun", "Osun"),
        ("Kano", "Kano"),
        ("Abuja", "Abuja"),

    ]
    position = [
        ("chairman", "chairman"),
        ("director", "director"),
        ("supervisor", "supervisor"),
        ("admin", "admin"),
        ("delivery agent", "delivery agent"),
        ("store keeper", "store keeper"),

    ]


    profile_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=50, null=True, blank=True, unique=False)
    phone=models.CharField(max_length=11,null=True, blank=True, unique=False)
    date_of_birth=models.DateField(max_length=11, null=True, unique=False)
    gender=models.CharField(choices=gen, null=True, max_length=11, unique=False)
    nationality=models.CharField(choices=countries, null=True, max_length=50, unique=False)
    state=models.CharField(choices=state, null=True,  max_length=20, unique=False)
    means_of_identity=models.ImageField(upload_to="identityImage/", unique=False, null=True)
    particulars=models.FileField(upload_to="particularsImage/", unique=False, null=True)
    profile_passport=models.ImageField(upload_to="profileImage/", unique=False, null=True)
    position=models.CharField(choices=position, null=True, max_length=25, unique=False)
    marital_status=models.CharField(choices=ma_status, null=True, max_length=20, unique=False)
    staff=models.BooleanField(default=False, unique=False)
    next_of_kin=models.CharField(null=True, max_length=20, unique=False)

    @receiver(post_save, sender =User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender = User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()