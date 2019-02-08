import datetime
from django.db import models
from django.contrib.auth.models import User

# Models of drScratch

class CSVs(models.Model):
    filename = models.CharField(max_length=100)
    directory = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        get_latest_by = 'date'

class File(models.Model):
    filename = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    time = models.DateField(auto_now=False)
    language = models.TextField(default="es")
    score = models.IntegerField()
    abstraction = models.IntegerField()
    parallelization = models.IntegerField()
    logic = models.IntegerField()
    synchronization = models.IntegerField()
    flowControl = models.IntegerField()
    userInteractivity = models.IntegerField()
    dataRepresentation = models.IntegerField()
    spriteNaming = models.IntegerField()
    initialization = models.IntegerField()
    deadCode = models.IntegerField()
    duplicateScript = models.IntegerField()

class Student(models.Model):
    student = models.ForeignKey(User, unique=True)  

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    #student = models.ManyToManyField(Student)

class Teacher(models.Model):
    teacher = models.ForeignKey(User, unique=True)
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
    hashkey = models.TextField()
    #classroom = models.ManyToManyField(Classroom)

class Organization(User):
    hashkey = models.TextField()

class OrganizationHash(models.Model):
    hashkey = models.TextField()

class Dashboard(models.Model):
    user = models.TextField()
    frelease = models.DateField()

class Project(models.Model):
    name = models.TextField()
    version = models.IntegerField()
    score = models.IntegerField()
    level = models.TextField()
    path = models.TextField()
    fupdate = models.TextField()
    dashboard = models.ForeignKey(Dashboard)

class Attribute(models.Model):
    myproject = models.ForeignKey(Project)
    character = models.TextField()
    orientation = models.IntegerField()
    position = models.IntegerField()
    costume = models.IntegerField()
    visibility = models.IntegerField()
    size = models.IntegerField()

class Dead(models.Model):
    myproject = models.ForeignKey(Project)
    character = models.TextField()
    blocks = models.IntegerField()

class Duplicate(models.Model):
    myproject = models.ForeignKey(Project)
    numduplicates = models.IntegerField()

class Sprite(models.Model):
    myproject = models.ForeignKey(Project)
    character = models.TextField()

class Mastery(models.Model):
    myproject = models.ForeignKey(Project)
    abstraction = models.IntegerField()
    paralel = models.IntegerField()
    logic = models.IntegerField()
    synchronization = models.IntegerField()
    flowcontrol = models.IntegerField()
    interactivity = models.IntegerField()
    representation = models.IntegerField()
    scoring = models.IntegerField()	

class Comment(models.Model):
    user = models.TextField()
    text = models.TextField()
    date = models.DateField()

class Activity(models.Model):
    text = models.TextField()
    date = models.DateField()

class Stats(models.Model):
    daily_score = models.TextField()
    basic = models.TextField(default="")
    development = models.TextField(default="")
    master = models.TextField(default="")
    daily_projects = models.TextField(default="")
    parallelism = models.IntegerField(default=int(0))
    abstraction = models.IntegerField(default=int(0))
    logic = models.IntegerField(default=int(0))
    synchronization = models.IntegerField(default=int(0))
    flowControl = models.IntegerField(default=int(0))
    userInteractivity = models.IntegerField(default=int(0))
    dataRepresentation = models.IntegerField(default=int(0))
    deadCode = models.IntegerField(default=int(0))
    duplicateScript = models.IntegerField(default=int(0))
    spriteNaming = models.IntegerField(default=int(0))
    initialization = models.IntegerField(default=int(0))
    
class Creator(User):
    hashkey = models.TextField()

class CreatorHash(models.Model):
    hashkey = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(default="")
    creator = models.CharField(max_length=100)
    
class Participant(User):    
    creator_username = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
    
class Challenge(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    parallelism = models.IntegerField(default=int(0))
    logic = models.IntegerField(default=int(0))
    flowControl = models.IntegerField(default=int(0))
    userInteractivity = models.IntegerField(default=int(0))
    dataRepresentation = models.IntegerField(default=int(0))
    abstraction = models.IntegerField(default=int(0))
    synchronization = models.IntegerField(default=int(0))
    creator = models.CharField(max_length=100)
    
class Tournament(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(default="")
    creator = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team)
    challenges = models.ManyToManyField(Challenge, through='ChallengesOfTournament')
    manualValidation = models.BooleanField(default=False)
    def get_challenges(self):
        return self.challenges.order_by('chall')
    
class ChallengesOfTournament (models.Model):
    position = models.PositiveIntegerField()
    tournament = models.ForeignKey(Tournament)
    challenge = models.ForeignKey(Challenge, related_name='chall')
    class Meta:
        ordering = ('position',)

class Game (models.Model):
    parallelism = models.IntegerField(default=int(0))
    logic = models.IntegerField(default=int(0))
    flowControl = models.IntegerField(default=int(0))
    userInteractivity = models.IntegerField(default=int(0))
    dataRepresentation = models.IntegerField(default=int(0))
    abstraction = models.IntegerField(default=int(0))
    synchronization = models.IntegerField(default=int(0))
    completed = models.IntegerField(default=int(0))
    challengeOfTournament = models.ForeignKey(ChallengesOfTournament)
    team = models.ForeignKey(Team)
    