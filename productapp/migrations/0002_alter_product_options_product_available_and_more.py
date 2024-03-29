# Generated by Django 4.2.9 on 2024-01-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'verbose_name': 'prodcut', 'verbose_name_plural': 'products'},
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2023-12-30'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default='100'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
