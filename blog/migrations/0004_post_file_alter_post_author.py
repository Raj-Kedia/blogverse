# Generated by Django 4.2.5 on 2023-10-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(default='<str: user', max_length=14),
        ),
    ]