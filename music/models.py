from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=20)
    instrument_type = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Album(models.Model):
    album_name = models.TextField(max_length=250)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    RATINGS = (
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    )
    rating = models.IntegerField(choices=RATINGS)

    def __str__(self):
        return self.album_name