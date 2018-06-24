from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return str(self.full_name)


class ExperienceType(models.Model):
    value = models.CharField(max_length=100)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)


class Location(models.Model):
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        result = ''
        if self.city:
            result += self.city
        if self.state:
            result += self.state
        if self.country:
            result += self.country

        return result


class Experience(models.Model):
    title = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    entity = models.CharField(max_length=200, null=True, blank=True)
    type = models.ForeignKey(ExperienceType)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class Resume(models.Model):
    person = models.ForeignKey(Person)
    experiences = models.ManyToManyField(Experience)

    def __str__(self):
        return str(self.person)

    @property
    def work_experiences(self):
        return self.experiences.filter(type__value='Work')

    @property
    def volunteer_experiences(self):
        return self.experiences.filter(type__value='Volunteer')
