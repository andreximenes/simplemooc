# -*- coding: utf-8 -*-
from django.db import models

# CustomManager usado para criar consultas personalizadas do objeto.
class CourseManager(models.Manager):

    '''
        Método que busca qualquer curso que contenha no nome ou descrição
        a string passada na query.
    '''
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | models.Q(name__icontains=query)
        )


class Course(models.Model):

    name = models.CharField(verbose_name='Nome', max_length=100)
    slug = models.SlugField(verbose_name='Atalho')
    description = models.TextField(verbose_name='Descrição Simples', blank=True)
    about = models.TextField('Sobre o Curso')
    start_date = models.DateField(verbose_name='Data de Início', null=True, blank=True)
    create_at = models.DateField(verbose_name='Criado em', auto_now_add=True)
    update_at = models.DateField(verbose_name='Atualizado em', auto_now=True)
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagem',
        null=True,
        blank=True
    )

    objects = CourseManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        ordering = ['name']

