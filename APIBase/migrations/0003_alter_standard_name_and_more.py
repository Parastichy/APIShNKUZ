# Generated by Django 4.0.1 on 2022-01-11 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIBase', '0002_rename_name_standard_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standard',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='originalCipherFromDocument',
            field=models.CharField(max_length=128, verbose_name='Оригинальный шифр с документа'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='searchCode',
            field=models.CharField(max_length=20, unique=True, verbose_name='Шифр поисковый (уникальный)'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='unit',
            field=models.CharField(max_length=64, verbose_name='Единица измерения'),
        ),
    ]