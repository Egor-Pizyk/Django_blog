# Generated by Django 4.1.1 on 2022-09-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_remove_post_rating_rating_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="rating",
            name="post",
        ),
        migrations.AddField(
            model_name="post",
            name="rating",
            field=models.ManyToManyField(blank=True, null=True, to="blog.rating"),
        ),
    ]