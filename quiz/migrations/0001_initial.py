# Generated by Django 2.2.10 on 2021-09-04 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Question text')),
                ('type', models.CharField(choices=[(1, 'Text answer'), (2, 'Single choice'), (3, 'Multiple choices')], max_length=100)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Quiz name')),
                ('start_time', models.DateTimeField(auto_now_add=True, verbose_name='Quiz start time')),
                ('end_time', models.DateTimeField(verbose_name='Quiz end time')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Quiz description')),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(blank=True, null=True, verbose_name='Answer text')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quiz.Question', verbose_name='Question ID')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
