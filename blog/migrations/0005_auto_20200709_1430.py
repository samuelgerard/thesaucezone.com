# Generated by Django 3.0.7 on 2020-07-09 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20200708_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(default=9508, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
