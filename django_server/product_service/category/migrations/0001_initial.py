# Generated by Django 4.1.13 on 2024-05-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('type_product', models.CharField(choices=[('Phone', 'Phone'), ('Book', 'Book'), ('Clothes', 'Clothes')], max_length=100, null=True)),
            ],
        ),
    ]
