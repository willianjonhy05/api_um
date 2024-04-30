from django.db import models

# Create your models here.


class Autor(models.Model):
    nome = models.CharField("Nome", max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
class Livro(models.Model):
    titulo = models.CharField("Nome", max_length=200)
    data_pub = models.DateField("Data de Publicação")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
    