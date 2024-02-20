import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=True)


class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Profile(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(
        upload_to="profile_pictures/", null=True, blank=True
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name="genders", null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField("DOB", blank=True, null=True)
    phone = models.TextField(null=True, default="+1")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.uid)
        super(Profile, self).save(*args, **kwargs)

        if self.profile_picture:
            self.crop_profile_picture()

    def crop_profile_picture(self):
        with Image.open(self.profile_picture.path) as img:
            size = min(img.size)
            left = (img.width - size) / 2
            top = (img.height - size) / 2
            right = (img.width + size) / 2
            bottom = (img.height + size) / 2

            img = img.crop((left, top, right, bottom))
            img = img.resize((300, 300), Image.ANTIALIAS)
            img.save(self.profile_picture.path)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})

    def get_profile_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.user.email
