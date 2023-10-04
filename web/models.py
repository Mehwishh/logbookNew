from django.db import models

# Create your models here.


class recordOfInvention(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    name_of_invention = models.CharField(max_length=1200, default="")
    problem_it_solves = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class statementOfOriginality(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    inventor1 = models.CharField(max_length=1200, default="")
    schoolnamegrade1 = models.CharField(max_length=1200, default="")
    sig1 = models.CharField(max_length=1200, default="")
    date1 = models.CharField(max_length=1200, default="")

    inventor2 = models.CharField(max_length=1200, default="")
    schoolnamegrade2 = models.CharField(max_length=1200, default="")
    sig2 = models.CharField(max_length=1200, default="")
    date2 = models.CharField(max_length=1200, default="")

    inventor3 = models.CharField(max_length=1200, default="")
    schoolnamegrade3 = models.CharField(max_length=1200, default="")
    sig3 = models.CharField(max_length=1200, default="")
    date3 = models.CharField(max_length=1200, default="")

    inventor4 = models.CharField(max_length=1200, default="")
    schoolnamegrade4 = models.CharField(max_length=1200, default="")
    sig4 = models.CharField(max_length=1200, default="")
    date4 = models.CharField(max_length=1200, default="")

    inventor5 = models.CharField(max_length=1200, default="")
    schoolnamegrade5 = models.CharField(max_length=1200, default="")
    sig5 = models.CharField(max_length=1200, default="")
    date5 = models.CharField(max_length=1200, default="")

    inventor6 = models.CharField(max_length=1200, default="")
    schoolnamegrade6 = models.CharField(max_length=1200, default="")
    sig6 = models.CharField(max_length=1200, default="")
    date6 = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class stepOne(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    identify_problems = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class stepTwo(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    p1name1 = models.CharField(max_length=1200, default="")
    p1name2 = models.CharField(max_length=1200, default="")
    p1name3 = models.CharField(max_length=1200, default="")
    p1name4 = models.CharField(max_length=1200, default="")
    p1age1 = models.CharField(max_length=1200, default="")
    p1age2 = models.CharField(max_length=1200, default="")
    p1age3 = models.CharField(max_length=1200, default="")
    p1age4 = models.CharField(max_length=1200, default="")
    p1comment1 = models.CharField(max_length=1200, default="")
    p1comment2 = models.CharField(max_length=1200, default="")
    p1comment3 = models.CharField(max_length=1200, default="")
    p1comment4 = models.CharField(max_length=1200, default="")

    p2name1 = models.CharField(max_length=1200, default="")
    p2name2 = models.CharField(max_length=1200, default="")
    p2name3 = models.CharField(max_length=1200, default="")
    p2name4 = models.CharField(max_length=1200, default="")
    p2age1 = models.CharField(max_length=1200, default="")
    p2age2 = models.CharField(max_length=1200, default="")
    p2age3 = models.CharField(max_length=1200, default="")
    p2age4 = models.CharField(max_length=1200, default="")
    p2comment1 = models.CharField(max_length=1200, default="")
    p2comment2 = models.CharField(max_length=1200, default="")
    p2comment3 = models.CharField(max_length=1200, default="")
    p2comment4 = models.CharField(max_length=1200, default="")

    p3name1 = models.CharField(max_length=1200, default="")
    p3name2 = models.CharField(max_length=1200, default="")
    p3name3 = models.CharField(max_length=1200, default="")
    p3name4 = models.CharField(max_length=1200, default="")
    p3age1 = models.CharField(max_length=1200, default="")
    p3age2 = models.CharField(max_length=1200, default="")
    p3age3 = models.CharField(max_length=1200, default="")
    p3age4 = models.CharField(max_length=1200, default="")
    p3comment1 = models.CharField(max_length=1200, default="")
    p3comment2 = models.CharField(max_length=1200, default="")
    p3comment3 = models.CharField(max_length=1200, default="")
    p3comment4 = models.CharField(max_length=1200, default="")

    p4name1 = models.CharField(max_length=1200, default="")
    p4name2 = models.CharField(max_length=1200, default="")
    p4name3 = models.CharField(max_length=1200, default="")
    p4name4 = models.CharField(max_length=1200, default="")
    p4age1 = models.CharField(max_length=1200, default="")
    p4age2 = models.CharField(max_length=1200, default="")
    p4age3 = models.CharField(max_length=1200, default="")
    p4age4 = models.CharField(max_length=1200, default="")
    p4comment1 = models.CharField(max_length=1200, default="")
    p4comment2 = models.CharField(max_length=1200, default="")
    p4comment3 = models.CharField(max_length=1200, default="")
    p4comment4 = models.CharField(max_length=1200, default="")

    other_notes = models.CharField(max_length=1200, default="")
    describe_problem = models.CharField(max_length=1200, default="")
    specific_solution = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class stepThree(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    factors = models.CharField(max_length=1200, default="")
    ways_to_solve = models.CharField(max_length=1200, default="")
    research = models.CharField(max_length=1200, default="")
    difference = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class stepFour(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    blueprint = models.ImageField(null=True, blank=True)
    teacher_name = models.CharField(max_length=1200, default="")
    teacher_sign = models.CharField(max_length=1200, default="")
    date = models.CharField(max_length=1200, default="")

    i1expert = models.CharField(max_length=1200, default="")
    i1credentials = models.CharField(max_length=1200, default="")
    i1identified = models.CharField(max_length=1200, default="")
    i1problemface = models.CharField(max_length=1200, default="")

    i2expert = models.CharField(max_length=1200, default="")
    i2credentials = models.CharField(max_length=1200, default="")
    i2identified = models.CharField(max_length=1200, default="")
    i2problemface = models.CharField(max_length=1200, default="")

    i3expert = models.CharField(max_length=1200, default="")
    i3credentials = models.CharField(max_length=1200, default="")
    i3identified = models.CharField(max_length=1200, default="")
    i3problemface = models.CharField(max_length=1200, default="")

    sol_design_problem = models.CharField(max_length=1200, default="")
    green_sol = models.CharField(max_length=1200, default="")

    @property
    def imageURL(self):
        try:
            url = self.blueprint.url
        except:
            url = ""
        return url
    
    def __str__(self):
        return str(self.teamId)


class stepFive(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    materials = models.CharField(max_length=1200, default="")
    findings = models.CharField(max_length=1200, default="")
    credit = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class stepSix(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    notes = models.CharField(max_length=1200, default="")
    prototype_pic = models.ImageField(null=True, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.prototype_pic.url
            print(url)
        except:
            url = ""
            print(url)
        return url
    
    def __str__(self):
        return str(self.teamId)


class stepSeven(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    testing = models.CharField(max_length=1200, default="")
    positive = models.CharField(max_length=1200, default="")
    negative = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class stepEight(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    nameinvention = models.CharField(max_length=1200, default="")
    benefits = models.CharField(max_length=1200, default="")
    price = models.CharField(max_length=1200, default="")
    buy = models.CharField(max_length=1200, default="")
    customer_age = models.CharField(max_length=1200, default="")
    customer_gender = models.CharField(max_length=1200, default="")
    customer_education = models.CharField(max_length=1200, default="")
    customer_house = models.CharField(max_length=1200, default="")
    customer_marital = models.CharField(max_length=1200, default="")
    other_notes = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)


class surveyLogbook(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)

    things_enjoyed = models.CharField(max_length=1200, default="")
    thanking = models.CharField(max_length=1200, default="")
    difficulty = models.CharField(max_length=1200, default="")
    future = models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)

class Note(models.Model):
    userId = models.IntegerField()
    teamId = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    
    note_title= models.CharField(max_length=1200, default="")
    note_desc= models.CharField(max_length=1200, default="")

    def __str__(self):
        return str(self.teamId)