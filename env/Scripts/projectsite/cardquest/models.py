from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Trainer(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class PokemonCard(BaseModel):
    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
    )
    CARDTYPE_CHOICES = (
        ('Normal', 'Normal'),
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Electric', 'Electric'),
        ('Grass', 'Grass'),
        ('Ice', 'Ice'),
        ('Fighting', 'Fighting'),
        ('Poison', 'Poison'),
        ('Ground', 'Ground'),
        ('Flying', 'Flying'),
        ('Psychic', 'Psychic'),
        ('Bug', 'Bug'),
        ('Rock', 'Rock'),
        ('Ghost', 'Ghost'),
        ('Dragon', 'Dragon'),
        ('Dark', 'Dark'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    rarity = models.CharField(max_length=100, null=True, blank=True, choices=RARITY_CHOICES)
    hp = models.IntegerField(null=True, blank=True)
    card_type = models.CharField(max_length=100, null=True, blank=True, choices=CARDTYPE_CHOICES)
    attack = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    weakness = models.CharField(max_length=250, null=True, blank=True)
    card_number = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    evolution_stage = models.CharField(max_length=250, null=True, blank=True)
    abilities = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class Collection(BaseModel):
    trainer = models.ForeignKey(Trainer, null=True, blank=True, on_delete= models.CASCADE)
    card = models.ForeignKey(PokemonCard, blank=True, null=True, on_delete=models.CASCADE)
    collection_date = models.DateField()

    def __str__(self):
        return self.trainer