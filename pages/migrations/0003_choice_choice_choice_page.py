# Generated by Django 4.2.2 on 2023-06-30 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice',
            field=models.CharField(choices=[('0', 'A'), ('1', 'B')], default='', max_length=10),
        ),
        migrations.AddField(
            model_name='choice',
            name='page',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='pages.page'),
        ),
    ]
