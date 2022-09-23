from django.db import models

#Items Model 
class Items(models.Model):
    name = models.CharField(max_length = 20)

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length = 30),
    type = models.CharField(max_length = 10),
    weight = models.IntegerField(),
    items = models.ManyToManyField(Items)

# A tuple of 2
LOCATION = (
    ('1', "Grassland"),
    ('2', "Mountains"),
    ('3', "Sea:")
)

#Catch Date model 
class Location(models.Model):
    date = models.DateField('feeding date')
    location  = models.CharField(
        max_length=1,
            choices=LOCATION,
            default=LOCATION[0][0]
        )


#POKEMON FK 
pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.get_location_display()} on {self.date}"
class Meta:
    ordering = ['-date']