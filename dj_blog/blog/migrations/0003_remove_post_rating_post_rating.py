# Generated by Django 4.1.1 on 2022-09-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_comments_alter_post_rating_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="rating",
        ),
        migrations.AddField(
            model_name="post",
            name="rating",
            field=models.ManyToManyField(blank=True, null=True, to="blog.rating"),
        ),
    ]
