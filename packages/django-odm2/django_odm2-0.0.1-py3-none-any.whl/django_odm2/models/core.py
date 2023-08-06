import uuid

from django.db import models

from ..querysets import (
    ActionByQuerySet,
    ActionQuerySet,
    AffiliationQuerySet,
    FeatureActionQuerySet,
    OrganizationQuerySet,
    RelatedActionManager,
    ResultManager,
)
from .abstracts import ObjectRelation, ODM2Model


class People(ODM2Model):
    person_id = models.AutoField(db_column='personid', primary_key=True)
    person_first_name = models.CharField(
        db_column='personfirstname', max_length=255
    )
    person_middle_name = models.CharField(
        db_column='personmiddlename', blank=True, max_length=255
    )
    person_last_name = models.CharField(
        db_column='personlastname', max_length=255
    )

    citations = models.ManyToManyField(
        'Citation', related_name='cited_authors', through='AuthorList'
    )
    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='people',
        through='PersonExternalIdentifier',
    )

    def __str__(self):
        return f'{self.person_first_name} {self.person_last_name}'

    def __repr__(self):
        return f"<Person('{self.person_id}', '{self.person_first_name}', '{self.person_last_name}')>"

    class Meta:
        db_table = 'people'
        ordering = ['person_first_name', 'person_last_name']


class Organization(ODM2Model):
    organization_id = models.AutoField(
        db_column='organizationid', primary_key=True
    )
    organization_type = models.ForeignKey(
        'OrganizationType',
        db_column='organizationtypecv',
        on_delete=models.CASCADE,
    )
    organization_code = models.CharField(
        db_column='organizationcode', max_length=50, unique=True
    )
    organization_name = models.CharField(
        db_column='organizationname', max_length=255
    )
    organization_description = models.CharField(
        db_column='organizationdescription', blank=True, max_length=500
    )
    organization_link = models.CharField(
        db_column='organizationlink', blank=True, max_length=255
    )
    parent_organization = models.ForeignKey(
        'self',
        db_column='parentorganizationid',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    people = models.ManyToManyField('People', through='Affiliation')

    objects = OrganizationQuerySet.as_manager()

    def __str__(self):
        return self.organization_code

    def __repr__(self):
        return f"<Organization('{self.organization_id}', '{self.organization_type_id}', '{self.organization_code}', '{self.organization_name}')>"

    class Meta:
        db_table = 'organizations'
        ordering = ['organization_code']


class Affiliation(ODM2Model):
    affiliation_id = models.AutoField(
        db_column='affiliationid', primary_key=True
    )
    person = models.ForeignKey(
        'People',
        related_name='affiliations',
        db_column='personid',
        on_delete=models.CASCADE,
    )
    organization = models.ForeignKey(
        'Organization',
        related_name='affiliations',
        db_column='organizationid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    is_primary_organization_contact = models.BooleanField(
        db_column='isprimaryorganizationcontact', default=None, null=True
    )
    affiliation_start_date = models.DateField(db_column='affiliationstartdate')
    affiliation_end_date = models.DateField(
        db_column='affiliationenddate', blank=True, null=True
    )
    primary_phone = models.CharField(
        db_column='primaryphone', blank=True, max_length=50
    )
    primary_email = models.CharField(db_column='primaryemail', max_length=255)
    primary_address = models.CharField(
        db_column='primaryaddress', blank=True, max_length=255
    )
    person_link = models.CharField(
        db_column='personlink', blank=True, max_length=255
    )

    objects = AffiliationQuerySet.as_manager()

    @property
    def role_status(self):
        return (
            'Primary contact'
            if self.is_primary_organization_contact
            else 'Secondary contact'
        )

    def __str__(self):
        return f'{self.person} - {self.organization}'

    def __repr__(self):
        return (
            "<Affiliation('%s', Person['%s', '%s'], Organization['%s', '%s'], '%s', '%s', '%s')>"
            % (
                self.affiliation_id,
                self.person_id,
                self.person,
                self.organization_id,
                self.organization,
                self.role_status,
                self.primary_email,
                self.primary_address,
            )
        )

    class Meta:
        db_table = 'affiliations'
        ordering = ['person__person_first_name', 'person__person_last_name']


class Method(ODM2Model):
    method_id = models.AutoField(db_column='methodid', primary_key=True)
    method_type = models.ForeignKey(
        'MethodType', db_column='methodtypecv', on_delete=models.CASCADE
    )
    method_code = models.CharField(db_column='methodcode', max_length=50)
    method_name = models.CharField(db_column='methodname', max_length=255)
    method_description = models.CharField(
        db_column='methoddescription', blank=True, max_length=500
    )
    method_link = models.CharField(
        db_column='methodlink', blank=True, max_length=255
    )
    organization = models.ForeignKey(
        'Organization',
        db_column='organizationid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_methods',
        through='MethodAnnotation',
    )
    extension_property_values = models.ManyToManyField(
        'ExtensionProperty',
        related_name='methods',
        through='MethodExtensionPropertyValue',
    )
    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='methods',
        through='MethodExternalIdentifier',
    )

    def __str__(self):
        return f'{self.method_name} ({self.method_type_id})'

    def __repr__(self):
        return "<Method('%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.method_id,
            self.method_type_id,
            self.method_code,
            self.method_name,
            self.method_description,
            self.method_link,
        )

    class Meta:
        db_table = 'methods'


class Action(ODM2Model):
    action_id = models.AutoField(db_column='actionid', primary_key=True)
    action_type = models.ForeignKey(
        'ActionType', db_column='actiontypecv', on_delete=models.CASCADE
    )
    method = models.ForeignKey(
        'Method', db_column='methodid', on_delete=models.CASCADE
    )
    begin_datetime = models.DateTimeField(db_column='begindatetime')
    begin_datetime_utc_offset = models.IntegerField(
        db_column='begindatetimeutcoffset'
    )
    end_datetime = models.DateTimeField(
        db_column='enddatetime', blank=True, null=True
    )
    end_datetime_utc_offset = models.IntegerField(
        db_column='enddatetimeutcoffset', blank=True, null=True
    )
    action_description = models.TextField(
        db_column='actiondescription', blank=True
    )
    action_file_link = models.FileField(db_column='actionfilelink', blank=True)

    people = models.ManyToManyField(
        'Affiliation', related_name='actions', through='ActionBy'
    )
    equipment_used = models.ManyToManyField(
        'Equipment', related_name='actions', through='EquipmentUsed'
    )
    directives = models.ManyToManyField(
        'Directive', related_name='actions', through='ActionDirective'
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_actions',
        through='ActionAnnotation',
    )
    extension_property_values = models.ManyToManyField(
        'ExtensionProperty',
        related_name='actions',
        through='ActionExtensionPropertyValue',
    )

    objects = ActionQuerySet.as_manager()

    def __str__(self):
        return '{date} {offset} {type}'.format(
            date=self.begin_datetime,
            offset=self.begin_datetime_utc_offset,
            type=self.action_type_id,
        )

    def __repr__(self):
        return "<Action('%s', '%s', '%s')>" % (
            self.action_id,
            self.action_type_id,
            self.begin_datetime,
        )

    class Meta:
        db_table = 'actions'


class ActionBy(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    action = models.ForeignKey(
        'Action',
        related_name='action_by',
        db_column='actionid',
        on_delete=models.CASCADE,
    )
    affiliation = models.ForeignKey(
        'Affiliation', db_column='affiliationid', on_delete=models.CASCADE
    )
    is_action_lead = models.BooleanField(
        db_column='isactionlead', default=None
    )
    role_description = models.CharField(
        db_column='roledescription', blank=True, max_length=255
    )

    objects = ActionByQuerySet.as_manager()

    def __str__(self):
        return '%s by %s' % (self.action, self.affiliation)

    def __repr__(self):
        return (
            "<ActionBy('%s', Action['%s', '%s'], Affiliation['%s', '%s'])>"
            % (
                self.bridge_id,
                self.action_id,
                self.action,
                self.affiliation_id,
                self.affiliation,
            )
        )

    class Meta:
        db_table = 'actionby'


class SamplingFeature(models.Model):
    sampling_feature_id = models.AutoField(
        db_column='samplingfeatureid', primary_key=True
    )
    sampling_feature_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_column='samplingfeatureuuid'
    )
    sampling_feature_type = models.ForeignKey(
        'SamplingFeatureType',
        db_column='samplingfeaturetypecv',
        on_delete=models.CASCADE,
    )
    sampling_feature_code = models.CharField(
        db_column='samplingfeaturecode', max_length=50, unique=True
    )
    sampling_feature_name = models.CharField(
        db_column='samplingfeaturename', blank=True, max_length=255
    )
    sampling_feature_description = models.CharField(
        db_column='samplingfeaturedescription', blank=True, max_length=500
    )
    sampling_feature_geo_type = models.ForeignKey(
        'SamplingFeatureGeoType',
        db_column='samplingfeaturegeotypecv',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    elevation_m = models.FloatField(
        db_column='elevation_m', blank=True, null=True
    )
    elevation_datum = models.ForeignKey(
        'ElevationDatum',
        db_column='elevationdatumcv',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    feature_geometry = models.BinaryField(
        db_column='featuregeometry', blank=True, null=True
    )

    actions = models.ManyToManyField(
        'Action', related_name='sampling_features', through='FeatureAction'
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_sampling_features',
        through='SamplingFeatureAnnotation',
    )
    extension_property_values = models.ManyToManyField(
        'ExtensionProperty',
        related_name='sampling_features',
        through='SamplingFeatureExtensionPropertyValue',
    )
    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='sampling_features',
        through='SamplingFeatureExternalIdentifier',
    )

    @property
    def latest_updated_result(self):
        return (
            self.feature_actions.with_results()
            .filter(results__value_count__gt=0)
            .latest('results__result_datetime')
            .results.first()
        )

    def __str__(self):
        return '%s %s' % (
            self.sampling_feature_code,
            self.sampling_feature_name,
        )

    def __repr__(self):
        return "<SamplingFeature('%s', '%s', '%s', '%s', '%s')>" % (
            self.sampling_feature_id,
            self.sampling_feature_type_id,
            self.sampling_feature_code,
            self.sampling_feature_name,
            self.elevation_m,
        )

    class Meta:
        db_table = 'samplingfeatures'


class FeatureAction(models.Model):
    feature_action_id = models.AutoField(
        db_column='featureactionid', primary_key=True
    )
    sampling_feature = models.ForeignKey(
        'SamplingFeature',
        related_name='feature_actions',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
    )
    action = models.ForeignKey(
        'Action',
        related_name='feature_actions',
        db_column='actionid',
        on_delete=models.CASCADE,
    )

    objects = FeatureActionQuerySet.as_manager()

    def __str__(self):
        return '%s on %s' % (self.action.action_type_id, self.sampling_feature)

    def __repr__(self):
        return (
            "<FeatureAction('%s', Action['%s', '%s'], SamplingFeature['%s', '%s'])>"
            % (
                self.feature_action_id,
                self.action_id,
                self.action,
                self.sampling_feature_id,
                self.sampling_feature,
            )
        )

    class Meta:
        db_table = 'featureactions'


class DataSet(models.Model):
    data_set_id = models.AutoField(db_column='datasetid', primary_key=True)
    data_set_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_column='datasetuuid'
    )
    data_set_type = models.ForeignKey(
        'DataSetType', db_column='datasettypecv', on_delete=models.CASCADE
    )
    data_set_code = models.CharField(db_column='datasetcode', max_length=50)
    data_set_title = models.CharField(db_column='datasettitle', max_length=255)
    data_set_abstract = models.CharField(
        db_column='datasetabstract', max_length=500
    )

    citations = models.ManyToManyField(
        'Citation', related_name='cited_data_sets', through='DataSetCitation'
    )

    def __str__(self):
        return '%s %s' % (self.data_set_code, self.data_set_title)

    def __repr__(self):
        return "<DataSet('%s', '%s', '%s', '%s')>" % (
            self.data_set_id,
            self.data_set_type_id,
            self.data_set_code,
            self.data_set_title,
        )

    class Meta:
        db_table = 'datasets'


class ProcessingLevel(models.Model):
    processing_level_id = models.AutoField(
        db_column='processinglevelid', primary_key=True
    )
    processing_level_code = models.CharField(
        db_column='processinglevelcode', max_length=50
    )
    definition = models.CharField(
        db_column='definition', blank=True, max_length=500
    )
    explanation = models.CharField(
        db_column='explanation', blank=True, max_length=500
    )

    def __str__(self):
        return '%s (%s)' % (self.processing_level_code, self.definition)

    def __repr__(self):
        return "<ProcessingLevel('%s', '%s', '%s')>" % (
            self.processing_level_id,
            self.processing_level_code,
            self.definition,
        )

    class Meta:
        db_table = 'processinglevels'


class RelatedAction(ObjectRelation):
    action = models.ForeignKey(
        'Action',
        related_name='related_actions',
        db_column='actionid',
        on_delete=models.CASCADE,
    )
    related_action = models.ForeignKey(
        'Action',
        related_name='reverse_related_actions',
        db_column='relatedactionid',
        on_delete=models.CASCADE,
    )

    objects = RelatedActionManager()

    def __str__(self):
        return '(%s) %s (%s)' % (
            self.action,
            self.relationship_type_id,
            self.related_action,
        )

    def __repr__(self):
        return (
            "<RelatedAction('%s', Action['%s', '%s'], '%s', Action['%s', '%s'])>"
            % (
                self.relation_id,
                self.action_id,
                self.action,
                self.relationship_type_id,
                self.related_action_id,
                self.related_action,
            )
        )

    class Meta:
        db_table = 'relatedactions'


class TaxonomicClassifier(models.Model):
    taxonomic_classifier_id = models.AutoField(
        db_column='taxonomicclassifierid', primary_key=True
    )
    taxonomic_classifier_type = models.ForeignKey(
        'TaxonomicClassifierType',
        db_column='taxonomicclassifiertypecv',
        on_delete=models.CASCADE,
    )
    taxonomic_classifier_name = models.CharField(
        db_column='taxonomicclassifiername', max_length=255
    )
    taxonomic_classifier_common_name = models.CharField(
        db_column='taxonomicclassifiercommonname', blank=True, max_length=255
    )
    taxonomic_classifier_description = models.CharField(
        db_column='taxonomicclassifierdescription', blank=True, max_length=500
    )
    parent_taxonomic_classifier = models.ForeignKey(
        'self',
        db_column='parenttaxonomicclassifierid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='taxonomic_classifier',
        through='TaxonomicClassifierExternalIdentifier',
    )

    def __str__(self):
        return '%s (%s)' % (
            self.taxonomic_classifier_common_name,
            self.taxonomic_classifier_name,
        )

    def __repr__(self):
        return "<TaxonomicClassifier('%s', '%s', '%s', '%s')>" % (
            self.taxonomic_classifier_id,
            self.taxonomic_classifier_type_id,
            self.taxonomic_classifier_name,
            self.taxonomic_classifier_common_name,
        )

    class Meta:
        db_table = 'taxonomicclassifiers'


class Unit(models.Model):
    unit_id = models.AutoField(db_column='unitsid', primary_key=True)
    unit_type = models.ForeignKey(
        'UnitsType', db_column='unitstypecv', on_delete=models.CASCADE
    )
    unit_abbreviation = models.CharField(
        db_column='unitsabbreviation', max_length=255
    )
    unit_name = models.CharField(db_column='unitsname', max_length=255)
    unit_link = models.CharField(
        db_column='unitslink', blank=True, max_length=255
    )

    def __str__(self):
        return '%s - %s (%s)' % (
            self.unit_name,
            self.unit_abbreviation,
            self.unit_type_id,
        )

    def __repr__(self):
        return "<Unit('%s', '%s', '%s', '%s')>" % (
            self.unit_id,
            self.unit_type_id,
            self.unit_abbreviation,
            self.unit_name,
        )

    class Meta:
        db_table = 'units'
        ordering = ['unit_name', 'unit_type_id']


class Variable(models.Model):
    variable_id = models.AutoField(db_column='variableid', primary_key=True)
    variable_type = models.ForeignKey(
        'VariableType', db_column='variabletypecv', on_delete=models.CASCADE
    )
    variable_code = models.CharField(db_column='variablecode', max_length=50)
    variable_name = models.ForeignKey(
        'VariableName', db_column='variablenamecv', on_delete=models.CASCADE
    )
    variable_definition = models.CharField(
        db_column='variabledefinition', blank=True, max_length=500
    )
    speciation = models.ForeignKey(
        'Speciation',
        db_column='speciationcv',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    no_data_value = models.FloatField(db_column='nodatavalue')

    extension_property_values = models.ManyToManyField(
        'ExtensionProperty',
        related_name='variables',
        through='VariableExtensionPropertyValue',
    )
    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='variables',
        through='VariableExternalIdentifier',
    )

    def __str__(self):
        return '%s' % self.variable_code

    def __repr__(self):
        return "<Variable('%s', '%s', '%s', '%s')>" % (
            self.variable_id,
            self.variable_code,
            self.variable_name_id,
            self.variable_type_id,
        )

    class Meta:
        db_table = 'variables'
        ordering = ['variable_code']


class Result(models.Model):
    result_id = models.AutoField(db_column='resultid', primary_key=True)
    result_uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, db_column='resultuuid'
    )
    feature_action = models.ForeignKey(
        'FeatureAction',
        related_name='results',
        db_column='featureactionid',
        on_delete=models.CASCADE,
    )
    result_type = models.ForeignKey(
        'ResultType', db_column='resulttypecv', on_delete=models.CASCADE
    )
    variable = models.ForeignKey(
        'Variable', db_column='variableid', on_delete=models.CASCADE
    )
    unit = models.ForeignKey(
        'Unit', db_column='unitsid', on_delete=models.CASCADE
    )
    taxonomic_classifier = models.ForeignKey(
        'TaxonomicClassifier',
        db_column='taxonomicclassifierid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    processing_level = models.ForeignKey(
        ProcessingLevel,
        db_column='processinglevelid',
        on_delete=models.CASCADE,
    )
    result_datetime = models.DateTimeField(
        db_column='resultdatetime', blank=True, null=True
    )
    result_datetime_utc_offset = models.BigIntegerField(
        db_column='resultdatetimeutcoffset', blank=True, null=True
    )
    valid_datetime = models.DateTimeField(
        db_column='validdatetime', blank=True, null=True
    )
    valid_datetime_utc_offset = models.BigIntegerField(
        db_column='validdatetimeutcoffset', blank=True, null=True
    )
    status = models.ForeignKey(
        'Status', db_column='statuscv', blank=True, on_delete=models.CASCADE
    )
    sampled_medium = models.ForeignKey(
        'Medium', db_column='sampledmediumcv', on_delete=models.CASCADE
    )
    value_count = models.IntegerField(db_column='valuecount', default=0)

    data_sets = models.ManyToManyField(
        'DataSet', related_name='results', through='DataSetResult'
    )
    data_quality_values = models.ManyToManyField(
        'DataQuality', related_name='results', through='ResultDataQuality'
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_results',
        through='ResultAnnotation',
    )
    extension_property_values = models.ManyToManyField(
        'ExtensionProperty',
        related_name='results',
        through='ResultExtensionPropertyValue',
    )

    objects = ResultManager()

    def __str__(self):
        return '%s - %s (%s): %s %s' % (
            self.result_datetime,
            self.result_type_id,
            self.variable.variable_name_id,
            self.variable.variable_code,
            self.unit.unit_abbreviation,
        )

    def __repr__(self):
        return "<Result('%s', '%s', '%s', '%s', '%s')>" % (
            self.result_id,
            self.result_uuid,
            self.result_type_id,
            self.processing_level.processing_level_code,
            self.value_count,
        )

    class Meta:
        db_table = 'results'


__all__ = [
    'People',
    'Organization',
    'Affiliation',
    'Method',
    'Action',
    'ODM2Model',
    'ActionBy',
    'SamplingFeature',
    'FeatureAction',
    'DataSet',
    'ProcessingLevel',
    'TaxonomicClassifier',
    'Unit',
    'Variable',
    'Result',
]
