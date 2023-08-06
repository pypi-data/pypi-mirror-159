from django.db import models

from .abstracts import ExternalIdentifierBridge


class ExternalIdentifierSystem(models.Model):
    external_identifier_system_id = models.AutoField(
        db_column='externalidentifiersystemid', primary_key=True
    )
    external_identifier_system_name = models.CharField(
        db_column='externalidentifiersystemname', max_length=255
    )
    identifier_system_organization = models.ForeignKey(
        'Organization',
        db_column='identifiersystemorganizationid',
        on_delete=models.CASCADE,
    )
    external_identifier_system_description = models.CharField(
        db_column='externalidentifiersystemdescription',
        blank=True,
        max_length=500,
    )
    external_identifier_system_url = models.CharField(
        db_column='externalidentifiersystemurl', blank=True, max_length=255
    )

    def __repr__(self):
        return (
            "<ExternalIdentifierSystem('%s', '%s', Organization['%s', '%s'])>"
            % (
                self.external_identifier_system_id,
                self.external_identifier_system_name,
                self.identifier_system_organization_id,
                self.identifier_system_organization,
            )
        )

    class Meta:
        db_table = 'externalidentifiersystems'


class CitationExternalIdentifier(ExternalIdentifierBridge):
    citation = models.ForeignKey(
        'Citation', db_column='citationid', on_delete=models.CASCADE
    )
    citation_external_identifier = models.CharField(
        db_column='citationexternalidentifier', max_length=255
    )
    citation_external_identifier_uri = models.CharField(
        db_column='citationexternalidentifieruri', blank=True, max_length=255
    )

    def __repr__(self):
        return (
            "<CitationExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], Citation['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.citation_id,
                self.citation,
            )
        )

    class Meta:
        db_table = 'citationexternalidentifiers'


class MethodExternalIdentifier(ExternalIdentifierBridge):
    method = models.ForeignKey(
        'Method', db_column='methodid', on_delete=models.CASCADE
    )
    method_external_identifier = models.CharField(
        db_column='methodexternalidentifier', max_length=255
    )
    method_external_identifier_uri = models.CharField(
        db_column='methodexternalidentifieruri', blank=True, max_length=255
    )

    def __repr__(self):
        return (
            "<MethodExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], Method['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.method_id,
                self.method,
            )
        )

    class Meta:
        db_table = 'methodexternalidentifiers'


class PersonExternalIdentifier(ExternalIdentifierBridge):
    person = models.ForeignKey(
        'People', db_column='personid', on_delete=models.CASCADE
    )
    person_external_identifier = models.CharField(
        db_column='personexternalidentifier', max_length=255
    )
    person_external_identifier_uri = models.CharField(
        db_column='personexternalidentifieruri', blank=True, max_length=255
    )

    def __repr__(self):
        return (
            "<PersonExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], Person['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.person_id,
                self.person,
            )
        )

    class Meta:
        db_table = 'personexternalidentifiers'


class ReferenceMaterialExternalIdentifier(ExternalIdentifierBridge):
    reference_material = models.ForeignKey(
        'ReferenceMaterial',
        db_column='referencematerialid',
        on_delete=models.CASCADE,
    )
    reference_material_external_identifier = models.CharField(
        db_column='referencematerialexternalidentifier', max_length=255
    )
    reference_material_external_identifier_uri = models.CharField(
        db_column='referencematerialexternalidentifieruri',
        blank=True,
        max_length=255,
    )

    def __repr__(self):
        return (
            "<ReferenceMaterialExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], ReferenceMaterial['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.reference_material_id,
                self.reference_material,
            )
        )

    class Meta:
        db_table = 'referencematerialexternalidentifiers'


class SamplingFeatureExternalIdentifier(ExternalIdentifierBridge):
    sampling_feature = models.ForeignKey(
        'SamplingFeature',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
    )
    sampling_feature_external_identifier = models.CharField(
        db_column='samplingfeatureexternalidentifier', max_length=255
    )
    sampling_feature_external_identifier_uri = models.CharField(
        db_column='samplingfeatureexternalidentifieruri',
        blank=True,
        max_length=255,
    )

    def __repr__(self):
        return (
            "<SamplingFeatureExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], SamplingFeature['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.sampling_feature_id,
                self.sampling_feature,
            )
        )

    class Meta:
        db_table = 'samplingfeatureexternalidentifiers'


class SpatialReferenceExternalIdentifier(ExternalIdentifierBridge):
    spatial_reference = models.ForeignKey(
        'SpatialReference',
        db_column='spatialreferenceid',
        on_delete=models.CASCADE,
    )
    spatial_reference_external_identifier = models.CharField(
        db_column='spatialreferenceexternalidentifier', max_length=255
    )
    spatial_reference_external_identifier_uri = models.CharField(
        db_column='spatialreferenceexternalidentifieruri',
        blank=True,
        max_length=255,
    )

    def __repr__(self):
        return (
            "<SpatialReferenceExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], SpatialReference['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.spatial_reference_id,
                self.spatial_reference,
            )
        )

    class Meta:
        db_table = 'spatialreferenceexternalidentifiers'


class TaxonomicClassifierExternalIdentifier(ExternalIdentifierBridge):
    taxonomic_classifier = models.ForeignKey(
        'TaxonomicClassifier',
        db_column='taxonomicclassifierid',
        on_delete=models.CASCADE,
    )
    taxonomic_classifier_external_identifier = models.CharField(
        db_column='taxonomicclassifierexternalidentifier', max_length=255
    )
    taxonomic_classifier_external_identifier_uri = models.CharField(
        db_column='taxonomicclassifierexternalidentifieruri',
        blank=True,
        max_length=255,
    )

    def __repr__(self):
        return (
            "<TaxonomicClassifierExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], TaxonomicClassifier['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.taxonomic_classifier_id,
                self.taxonomic_classifier,
            )
        )

    class Meta:
        db_table = 'taxonomicclassifierexternalidentifiers'


class VariableExternalIdentifier(ExternalIdentifierBridge):
    variable = models.ForeignKey(
        'Variable', db_column='variableid', on_delete=models.CASCADE
    )
    variable_external_identifier = models.CharField(
        db_column='variableexternalidentifer', max_length=255
    )
    variable_external_identifier_uri = models.CharField(
        db_column='variableexternalidentifieruri', blank=True, max_length=255
    )

    def __repr__(self):
        return (
            "<VariableExternalIdentifier('%s', '%s', ExternalIdentifierSystem['%s', '%s'], Variable['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.variable_id,
                self.variable,
            )
        )

    class Meta:
        db_table = 'variableexternalidentifiers'
