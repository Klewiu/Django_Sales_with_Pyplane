# Generated by Django 3.2.1 on 2021-05-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_sale_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]