from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, username, numero, password=None):
        if not numero:
            raise ValueError('Usuario debe tener un numero de tel')

        if not username:
            raise ValueError('Usuario debe tener nombre de usuario')

        user = self.model(
            numero = numero,
            username = username,
            #primer_nombre = primer_nombre,
            #apellido = apellido,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, numero, password):
        user = self.create_user(
            numero = numero,
            username = username,
            password = password,
            #primer_nombre = primer_nombre,
            #apellido = apellido,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Cuenta(AbstractBaseUser):
    #primer_nombre = models.CharField(max_length=50)
    #apellido = models.CharField(max_length=50)
    username = models.CharField(verbose_name = "usuario", max_length=50, unique=True)
    numero = models.CharField(max_length=50, unique=True)

    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'numero'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.numero

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
