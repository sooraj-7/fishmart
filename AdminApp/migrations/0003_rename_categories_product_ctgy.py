# Generated by Django 5.1.2 on 2024-12-14 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_product_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='ctgy',
        ),
    ]
