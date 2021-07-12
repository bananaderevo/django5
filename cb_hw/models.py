from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Author'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/author/{self.id}'


class Publisher(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/publisher/{self.id}'


class Comments(models.Model):
    comment = models.CharField(max_length=1000, unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return f'/comment/{self.id}'


class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    rating = models.FloatField(null=True)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, to_field='name', default=None)
    pubdate = models.DateField(null=True)
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, null=True, to_field='comment', default=None)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def display_authors(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([authors.name for authors in self.authors.all()[:3]])

    display_authors.short_description = 'Authors'

    def get_absolute_url(self):
        return f'/book/{self.id}'


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def display_books(self):
        """Creates a string for the Genre. This is required to display genre in Admin."""
        return ', '.join([books.name for books in self.books.all()[:3]])

    display_books.short_description = 'Books'

    def get_absolute_url(self):
        return f'/store/{self.id}'
