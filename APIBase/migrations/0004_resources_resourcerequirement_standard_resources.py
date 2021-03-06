# Generated by Django 4.0.1 on 2022-01-16 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APIBase', '0003_alter_standard_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(max_length=9, verbose_name='Наименование ресурса (полное)')),
                ('resourceName', models.CharField(max_length=255, verbose_name='Наименование ресурса (полное)')),
                ('unit', models.CharField(max_length=5, verbose_name='Единица измерения')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumptionRate', models.IntegerField(max_length=9, verbose_name='Норма расхода ')),
                ('expenditure', models.ManyToManyField(blank=True, null=True, to='APIBase.Resources')),
            ],
        ),
        migrations.AddField(
            model_name='standard',
            name='Resources',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='APIBase.resourcerequirement'),
        ),
    ]
