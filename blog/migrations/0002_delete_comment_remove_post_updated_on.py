# Generated by Django 5.1.4 on 2024-12-30 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_on',
        ),
    ]
