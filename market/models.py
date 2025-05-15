from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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
    username = models.CharField("Nome de usuário", max_length=200)
    email = models.EmailField("Email", max_length=200, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "user"

    def __str__(self):
        return self.email


class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artesões')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='clientes')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    TIPO_CHOICES = [
        ('reciclagem', 'Reciclagem'),
        ('cosmeticos', 'Cosméticos'),
        ('velas', 'Velas'),
        ('croche', 'Crochê'),
        ('bijuterias', 'Bijuterias'),
    ]
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES, unique=True)
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"

    def __str__(self):
        return self.tipo


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(verbose_name='Preço',  max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='product_images/')

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.nome


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(verbose_name='quantidade', max_digits=10, decimal_places=2)
    STATUS_VISITANTE = [
        ('EM_ANDAMENTO', 'Em Andamento'),
        ('CONCLUIDO','Transação concluida')
    ]
    
    status =  models.CharField( verbose_name='status', max_length=30,choices=STATUS_VISITANTE, default='EM_ANDAMENTO')
    timestamp = models.DateTimeField(auto_now_add=True)
