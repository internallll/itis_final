# Generated by Django 5.1.6 on 2025-02-28 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_site', '0002_remove_answer_answer_value_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='doneFeedback',
            new_name='done_feedback',
        ),
    ]
