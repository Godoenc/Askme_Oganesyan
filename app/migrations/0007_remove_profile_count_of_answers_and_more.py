# Generated by Django 5.1.5 on 2025-01-22 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_likes_of_answers_profile_likes_of_question_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='count_of_answers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='count_of_questions',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='count_of_mentions',
        ),
    ]
