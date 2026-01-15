from django.db import models

class Couleur(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Dragon(models.Model):
    nom = models.CharField(max_length=100)

    # N–N : un dragon peut avoir plusieurs couleurs
    couleurs = models.ManyToManyField(Couleur)

    # 1–N : plusieurs dragons pour une catégorie
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="dragons"
    )

    taille = models.FloatField(help_text="Taille")
    age = models.IntegerField(help_text="Âge")
    description = models.TextField()

    image = models.ImageField(upload_to='images/%Y/%m', blank=True)

    def __str__(self):
        return self.nom
