from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

class Genre(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='books',
    )
    isbn = models.CharField(max_length=32, unique=True)
    publication_year = models.IntegerField()
    genres = models.CharField(max_length=255)
    co_authors = models.CharField(max_length=255)
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title
