# Generated by Django 2.2.10 on 2021-09-04 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20210904_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='passedquiz',
            name='quiz_name',
            field=models.CharField(default=None, max_length=255, verbose_name='Quiz name'),
            preserve_default=False,
        ),
    ]
