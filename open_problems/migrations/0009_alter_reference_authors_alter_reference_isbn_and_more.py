# Generated by Django 4.2.2 on 2023-07-17 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("open_problems", "0008_alter_reference_doi_alter_reference_isbn_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reference",
            name="authors",
            field=models.ManyToManyField(
                blank=True, null=True, to="open_problems.author"
            ),
        ),
        migrations.AlterField(
            model_name="reference",
            name="isbn",
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="reference",
            name="journal_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="open_problems.journal",
            ),
        ),
        migrations.AlterField(
            model_name="reference",
            name="link",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
