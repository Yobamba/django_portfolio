# Generated by Django 5.0.4 on 2024-04-30 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_remove_project_projects_remove_project_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='title',
            field=models.CharField(default='Default title', max_length=200),
            preserve_default=False,
        ),
    ]
