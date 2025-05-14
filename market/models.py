from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        user = self.model(
            email = self.normalize_email(email),
        )
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        if password:
            user.set_password(password)

            user.save()
            return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        if password:
            user.set_password(password)

        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Nome de usuário', max_length=200)
    email = models.EmailField(verbose_name='Email do usuário', max_length=200, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_artisan = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'

    def __str__(self):
        return self.email

class Category(models.Model):
    tipo_choices = [
        ('reciclagem', 'Reciclagem'),
        ('cosméticos', 'Cosméticos'),
        ('velas', 'Velas'),
        ('crochê', 'Crochê'),
        ('bijuterias', 'Bijuterias')
    ]
    tipo = models.CharField(max_length=100, choices=tipo_choices, unique=True)
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='produtos')
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.FloatField()
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.nome