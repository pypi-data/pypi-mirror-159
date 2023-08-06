from django.db import models

from .abstracts import ObjectRelation


class SpatialReference(models.Model):
    spatial_reference_id = models.AutoField(
        db_column='spatialreferenceid', primary_key=True
    )
    srs_code = models.CharField(db_column='srscode', blank=True, max_length=50)
    srs_name = models.CharField(db_column='srsname', max_length=255)
    srs_description = models.CharField(
        db_column='srsdescription', blank=True, max_length=500
    )
    srs_link = models.CharField(
        db_column='srslink', blank=True, max_length=255
    )

    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='spatial_references',
        through='SpatialReferenceExternalIdentifier',
    )

    def __repr__(self):
        return "<SpatialReference('%s', '%s', '%s')>" % (
            self.spatial_reference_id,
            self.srs_code,
            self.srs_name,
        )

    class Meta:
        db_table = 'spatialreferences'


class Specimen(models.Model):
    sampling_feature = models.OneToOneField(
        'SamplingFeature',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    specimen_type = models.ForeignKey(
        'SpecimenType', db_column='specimentypecv', on_delete=models.CASCADE
    )
    specimen_medium = models.ForeignKey(
        'Medium', db_column='specimenmediumcv', on_delete=models.CASCADE
    )
    is_field_specimen = models.BooleanField(
        db_column='isfieldspecimen', default=None
    )

    def __repr__(self):
        return "<SpatialReference('%s', '%s', '%s')>" % (
            self.spatial_reference_id,
            self.srs_code,
            self.srs_name,
        )

    class Meta:
        db_table = 'specimens'


class SpatialOffset(models.Model):
    spatial_offset_id = models.AutoField(
        db_column='spatialoffsetid', primary_key=True
    )
    spatial_offset_type = models.ForeignKey(
        'SpatialOffsetType',
        db_column='spatialoffsettypecv',
        on_delete=models.CASCADE,
    )
    offset_1_value = models.FloatField(db_column='offset1value')
    offset_1_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='offset1unitid',
        on_delete=models.CASCADE,
    )
    offset_2_value = models.FloatField(
        db_column='offset2value', blank=True, null=True
    )
    offset_2_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='offset2unitid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    offset_3_value = models.FloatField(
        db_column='offset3value', blank=True, null=True
    )
    offset_3_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='offset3unitid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __repr__(self):
        return "<SpatialOffset('%s', '%s', '%s')>" % (
            self.spatial_offset_id,
            self.spatial_offset_type_id,
            self.srs_name,
        )

    class Meta:
        db_table = 'spatialoffsets'


class Site(models.Model):
    sampling_feature = models.OneToOneField(
        'SamplingFeature',
        related_name='site',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    site_type = models.ForeignKey(
        'SiteType', db_column='sitetypecv', on_delete=models.CASCADE
    )
    latitude = models.FloatField(db_column='latitude')
    longitude = models.FloatField(db_column='longitude')
    spatial_reference = models.ForeignKey(
        'SpatialReference',
        db_column='spatialreferenceid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return "<Site('%s', '%s', '%s', '%s')>" % (
            self.sampling_feature_id,
            self.site_type_id,
            self.latitude,
            self.longitude,
        )

    class Meta:
        db_table = 'sites'


class RelatedFeature(ObjectRelation):
    sampling_feature = models.ForeignKey(
        'SamplingFeature',
        related_name='related_features_sampling_feature',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
    )
    related_feature = models.ForeignKey(
        'SamplingFeature',
        related_name='related_features_related_feature',
        db_column='relatedfeatureid',
        on_delete=models.CASCADE,
    )
    spatial_offset = models.ForeignKey(
        'SpatialOffset',
        db_column='spatialoffsetid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __repr__(self):
        return (
            "<RelatedFeature('%s', SamplingFeature['%s', '%s'], '%s', SamplingFeature['%s', '%s'])>"
            % (
                self.relation_id,
                self.sampling_feature_id,
                self.sampling_feature,
                self.relationship_type_id,
                self.related_feature_id,
                self.related_feature,
            )
        )

    class Meta:
        db_table = 'relatedfeatures'


class SpecimenTaxonomicClassifier(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    sampling_feature = models.ForeignKey(
        'Specimen',
        related_name='taxonomic_classifiers',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
    )
    taxonomic_classifier = models.ForeignKey(
        'TaxonomicClassifier',
        db_column='taxonomicclassifierid',
        on_delete=models.CASCADE,
    )
    citation = models.ForeignKey(
        'Citation',
        related_name='specimen_taxonomic_classifiers',
        db_column='citationid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __repr__(self):
        return (
            "<SpecimenTaxonomicClassifier('%s', SamplingFeature['%s', '%s'], TaxonomicClassifier['%s', '%s'])>"
            % (
                self.bridge_id,
                self.sampling_feature_id,
                self.sampling_feature,
                self.taxonomic_classifier_id,
                self.taxonomic_classifier,
            )
        )

    class Meta:
        db_table = 'specimentaxonomicclassifiers'
