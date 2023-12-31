# Generated by Django 4.2.1 on 2023-08-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('with_medicine_userapp', '0002_rename_address_customuser_phone_unmber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남성(Man)'), ('W', '여성(Woman)'), ('O', '기타(Other)')], max_length=1, null=True, verbose_name='성별'),
        ),
    ]
