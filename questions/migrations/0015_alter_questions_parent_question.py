# Generated by Django 4.2.1 on 2023-05-30 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("questions", "0014_rename_related_question_id_relatedquestions_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questions",
            name="parent_question",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="parent",
                to="questions.questions",
            ),
        ),
    ]
