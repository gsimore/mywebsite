# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-23 20:34
from __future__ import unicode_literals

from django.db import migrations


def create_gabby_and_resume(apps, schema_editor):
    """
    Create the 'Gabby' person and a resume with other required models.
    :param apps:
    :param schema_editor:
    :return:
    """
    Person = apps.get_model('me', 'Person')
    gabby = Person.objects.create(
        first_name='Gabrielle',
        last_name='Simard-Moore'
    )
    # Create basic experience types.
    ExperienceType = apps.get_model('me', 'ExperienceType')
    values = ['Work', 'Volunteer']
    for value in values:
        ExperienceType.objects.create(
            value=value
        )

    Experience = apps.get_model('me', 'Experience')
    Location = apps.get_model('me', 'Location')
    portland = Location.objects.create(
        city='Portland',
        state='OR',
        country='US'
    )
    cloudbolt = Experience.objects.create(
        type=ExperienceType.objects.get(value='Work'),
        title='Software Engineer',
        description='Core contributor to the product in python and django, improving integrations with '
                    'cloud services.',
        entity='CloudBolt Software',
        location=portland,
    )

    djangogirls = Experience.objects.create(
        type=ExperienceType.objects.get(value='Volunteer'),
        title='Coach',
        description='Empowering women with programming skills in a day-long workshop '
                    'which provides a space for new learners to have mentorship and guidance '
                    'while doing the Django Girls tutorial.',
        entity='DjangoGirls',
        location=portland,
    )

    Resume = apps.get_model('me', 'Resume')
    resume = Resume.objects.create(
        person=gabby
    )
    resume.experiences.add(cloudbolt)
    resume.experiences.add(djangogirls)


class Migration(migrations.Migration):

    dependencies = [
        ('me', '0002_auto_20180623_2049'),
    ]

    operations = [
        migrations.RunPython(create_gabby_and_resume),
    ]
