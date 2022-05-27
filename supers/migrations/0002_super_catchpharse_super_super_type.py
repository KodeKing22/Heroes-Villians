# Generated by Django 4.0.4 on 2022-05-26 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0002_remove_supertypes_super'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='catchpharse',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertypes'),
        ),
    ]
