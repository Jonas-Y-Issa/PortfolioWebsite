# Generated by Django 4.1.1 on 2022-10-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_project_delete_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='/home/kyuudou/Desktop/Main Directory/Projects/Programming/Work/Website/MyWebsite/staticfiles/images'),
        ),
    ]
