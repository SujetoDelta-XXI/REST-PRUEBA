from django.db import models

class EnglishWord(models.Model):
    word = models.CharField(max_length=100)
    meaning = models.TextField()
    translation = models.TextField()
    method = models.CharField(max_length=100, choices=[
        ('flashcard', 'Flashcard'),
        ('active reading', 'Active Reading'),
        ('language learning apps', 'Language Learning Apps'),
    ], default='flashcard')
    date_added = models.DateField(auto_now_add=True)
