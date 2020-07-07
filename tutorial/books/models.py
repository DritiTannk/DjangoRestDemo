from django.db import models


# Create your models here.


class BookCategory(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class BookDetails(models.Model):
    book_name = models.CharField(max_length=50)
    author_name = models.CharField(max_length=50)
    category = models.ForeignKey('BookCategory', related_name='book_category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Book Detail"
        verbose_name_plural = "Book Details"

    def __str__(self):
        return "%s , %s " % (self.book_name, self.category)
