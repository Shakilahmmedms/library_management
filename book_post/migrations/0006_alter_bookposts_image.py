# Generated by Django 5.0.2 on 2024-02-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_post', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookposts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]