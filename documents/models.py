from django.db import models

# Modello per i documenti
class Document(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Modello per gli interventi
class Intervention(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    comment = models.TextField()
    intervention_type = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Intervento su {self.document.title}'

# Modello per il test
class Test(models.Model):
    question = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question