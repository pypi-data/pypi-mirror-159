from django.db import models

from .abstracts import ObjectRelation


class Model(models.Model):
    model_id = models.AutoField(db_column='modelid', primary_key=True)
    model_code = models.CharField(db_column='modelcode', max_length=255)
    model_name = models.CharField(db_column='modelname', max_length=255)
    model_description = models.CharField(
        db_column='modeldescription', max_length=500, blank=True
    )
    version = models.CharField(db_column='version', blank=True, max_length=255)
    model_link = models.CharField(
        db_column='modellink', blank=True, max_length=255
    )

    def __repr__(self):
        return "<Model('%s', '%s', '%s', '%s')>" % (
            self.model_id,
            self.model_code,
            self.model_name,
            self.version,
        )

    class Meta:
        db_table = 'models'


class RelatedModel(ObjectRelation):
    model = models.ForeignKey(
        'Model',
        related_name='related_model_model',
        db_column='modelid',
        on_delete=models.CASCADE,
    )
    related_model = models.ForeignKey(
        'Model',
        related_name='related_model_related_model',
        db_column='relatedmodelid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return "<RelatedModel('%s', Model['%s', '%s'], Model['%s', '%s'])>" % (
            self.relation_id,
            self.model_id,
            self.model,
            self.related_model_id,
            self.related_model,
        )

    class Meta:
        db_table = 'relatedmodels'


class Simulation(models.Model):
    simulation_id = models.AutoField(
        db_column='simulationid', primary_key=True
    )
    action = models.ForeignKey(
        'Action',
        related_name='simulations',
        db_column='actionid',
        on_delete=models.CASCADE,
    )
    simulation_name = models.CharField(
        db_column='simulationname', max_length=255
    )
    simulation_description = models.CharField(
        db_column='simulationdescription', max_length=500, blank=True
    )
    simulation_start_datetime = models.DateTimeField(
        db_column='simulationstartdatetime'
    )
    simulation_start_datetime_utc_offset = models.IntegerField(
        db_column='simulationstartdatetimeutcoffset'
    )
    simulation_end_datetime = models.DateTimeField(
        db_column='simulationenddatetime'
    )
    simulation_end_datetime_utc_offset = models.IntegerField(
        db_column='simulationenddatetimeutcoffset'
    )
    time_step_value = models.FloatField(db_column='timestepvalue')
    time_step_unit = models.ForeignKey(
        'Unit',
        related_name='simulations',
        db_column='timestepunitsid',
        on_delete=models.CASCADE,
    )
    input_data_set = models.ForeignKey(
        'DataSet',
        related_name='simulations',
        db_column='inputdatasetid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    model = models.ForeignKey(
        'Model',
        related_name='simulations',
        db_column='modelid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return "<Simulation('%s', '%s', '%s', '%s')>" % (
            self.simulation_id,
            self.simulation_name,
            self.simulation_start_datetime,
            self.simulation_end_datetime,
        )

    class Meta:
        db_table = 'simulations'


class Citation(models.Model):
    citation_id = models.AutoField(db_column='citationid', primary_key=True)
    title = models.CharField(db_column='title', max_length=255)
    publisher = models.CharField(db_column='publisher', max_length=255)
    publication_year = models.IntegerField(db_column='publicationyear')
    citation_link = models.CharField(
        db_column='citationlink', blank=True, max_length=255
    )

    extension_property_values = models.ManyToManyField(
        'ExtensionProperty',
        related_name='citations',
        through='CitationExtensionPropertyValue',
    )
    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='citations',
        through='CitationExternalIdentifier',
    )

    def __repr__(self):
        return "<Citation('%s', '%s', '%s', '%s')>" % (
            self.citation_id,
            self.title,
            self.publisher,
            self.publication_year,
        )

    class Meta:
        db_table = 'citations'
