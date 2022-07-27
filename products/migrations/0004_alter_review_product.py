# Generated by Django 3.2.5 on 2022-07-27 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product'),
        ),
    ]