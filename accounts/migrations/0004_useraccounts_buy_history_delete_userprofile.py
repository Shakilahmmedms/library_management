# Generated by Django 5.0.2 on 2024-02-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_buynow_alter_userprofile_buy_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccounts',
            name='buy_history',
            field=models.ManyToManyField(to='accounts.buynow'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
