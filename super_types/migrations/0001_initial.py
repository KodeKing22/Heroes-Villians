# Generated by Django 4.0.4 on 2022-05-26 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('super', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supers.super')),
            ],
        ),
    ]
