from django.db.models import models 
from questions import Question 
from references import Reference

#The 
class Theory(models.Model):
    theory_id = models.BigIntegerField(db_column='Theory_id', primary_key=True)  # Field name made lowercase.
    theorytitle = models.CharField(db_column='TheoryTitle', max_length=40, blank=True, null=True)  # Field name made lowercase.
    theorydesc = models.TextField(db_column='TheoryDesc', blank=True, null=True)  # Field name made lowercase.
    parent_t = models.ForeignKey('self', models.DO_NOTHING, db_column='Parent_T_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theory'


class TheoryQuestion(models.Model):
    opinion = models.OneToOneField(Question, models.DO_NOTHING, db_column='Opinion_id', primary_key=True)  # Field name made lowercase. The composite primary key (Opinion_id, species_id, Theory_id) found, that is not supported. The first column is selected.
    species_id = models.BigIntegerField()
    theory = models.ForeignKey(Theory, models.DO_NOTHING, db_column='Theory_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theory_question'
        unique_together = (('opinion', 'species_id', 'theory'),)


class TheoryReference(models.Model):
    ref = models.OneToOneField(Reference, models.DO_NOTHING, db_column='Ref_id', primary_key=True)  # Field name made lowercase. The composite primary key (Ref_id, Theory_id) found, that is not supported. The first column is selected.
    theory = models.ForeignKey(Theory, models.DO_NOTHING, db_column='Theory_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theory_reference'
        unique_together = (('ref', 'theory'))