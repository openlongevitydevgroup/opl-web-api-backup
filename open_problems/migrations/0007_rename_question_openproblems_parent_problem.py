# Generated by Django 4.2.2 on 2023-07-17 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("open_problems", "0006_rename_question_id_openproblems_problem_id_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="openproblems",
            old_name="question",
            new_name="parent_problem",
        ),
    ]
