from django.db.models import Model, CharField, DateTimeField, TextField, SmallIntegerField, ForeignKey, DO_NOTHING,CASCADE
from datetime import datetime
from django.contrib.auth.models import User

class PartyType(Model):
    type = CharField(max_length=50)

    def __str__(self):
        return f"{self.type}"


class Party(Model):

    date = DateTimeField(null=False, blank=False)
    create_date = DateTimeField(default=datetime.now())
    adress = CharField(max_length=130)
    party_type = ForeignKey(PartyType, on_delete = DO_NOTHING)
    free_space = SmallIntegerField(null = True)
    description = TextField(max_length=200)
    name = TextField(max_length=75, null=True)
    author = ForeignKey(User, on_delete= CASCADE, null=True, blank = True)



    def __str__(self):
        return f"{self.name} {self.date}"

