from django.db import models

# Create your models here.
EVENTS = (
    ('B', 'Birth'),
    ('D', 'Death'),
    ('M', 'Marriage'),
    ('G', 'Graduation'),
    ('M', 'Military Service'),
    ('R', 'Relocation'),
    ('O', 'Other')
)


class FamilyMember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} was born on {self.birth_date}"
    
class Comment(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(blank=True)
    

    def __str__(self):
        return self.title

class LifeEvent(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    event_type = models.CharField(
        max_length=1,
        choices=EVENTS,
        # set the default to the first item in the tuple
        default=EVENTS[0][0]
        )
    event_date = models.DateField()
    event_description = models.TextField(blank=True) 
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.event_type + ' on ' + str(self.event_date) + ' for ' + self.family_member.first_name + ' ' + self.family_member.last_name  
    # set the default ordering for the model
    class Meta:
        ordering = ['-event_date'] 