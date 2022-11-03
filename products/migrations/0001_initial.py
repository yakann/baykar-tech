# Generated by Django 4.0.3 on 2022-11-03 18:38

from django.db import migrations, models
import enumfields.fields
import products.enums


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=35)),
                ('type', enumfields.fields.EnumField(blank=True, enum=products.enums.AttributeType, max_length=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=55)),
                ('barcode', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=165)),
                ('type', enumfields.fields.EnumField(blank=True, enum=products.enums.ProductType, max_length=10, null=True)),
                ('attributes', models.JSONField()),
                ('is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
