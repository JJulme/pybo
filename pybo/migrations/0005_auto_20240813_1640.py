# Generated by Django 2.2.5 on 2024-08-13 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_answer_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
