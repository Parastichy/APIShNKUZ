# Generated by Django 4.0.1 on 2022-01-16 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIBase', '0006_unit_remove_standard_resources_alter_resources_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcerequirement',
            name='standard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APIBase.standard'),
        ),
    ]
