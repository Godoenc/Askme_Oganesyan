# Generated by Django 5.1.5 on 2025-01-21 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes_of_answers',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
        migrations.AddField(
            model_name='likes_of_question',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='likes_of_answers',
            unique_together={('profile', 'answer')},
        ),
        migrations.AlterUniqueTogether(
            name='likes_of_question',
            unique_together={('profile', 'question')},
        ),
    ]
