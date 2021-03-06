# Generated by Django 4.0.1 on 2022-01-16 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIBase', '0004_resources_resourcerequirement_standard_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcerequirement',
            name='consumptionRate',
            field=models.IntegerField(verbose_name='Норма расхода '),
        ),
        migrations.RemoveField(
            model_name='resourcerequirement',
            name='expenditure',
        ),
        migrations.AddField(
            model_name='resourcerequirement',
            name='expenditure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APIBase.resources'),
        ),
    ]
