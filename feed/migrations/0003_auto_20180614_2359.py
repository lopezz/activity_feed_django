# Generated by Django 2.0.6 on 2018-06-15 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_auto_20180614_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeditems', to='feed.RegisteredUser', verbose_name='Author'),
        ),
    ]
