# Generated by Django 3.2.1 on 2021-05-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sale_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]