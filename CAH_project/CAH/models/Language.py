from django.db import models

#* Models where this model is a foreign key:
#* Extension

class Language(models.Model):
    LanguageID = models.AutoField(primary_key=True)
    LanguageName = models.CharField(max_length=20)

    def __str__(self):
        return str(self.LanguageID + " " + self.LanguageName)
