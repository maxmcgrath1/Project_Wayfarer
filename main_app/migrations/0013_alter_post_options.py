# Generated by Django 4.0.2 on 2022-02-17 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_post_user_alter_profile_posts_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]
