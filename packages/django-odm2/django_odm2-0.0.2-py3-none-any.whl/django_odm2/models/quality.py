from django.db import models


class DataSetResult(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    data_set = models.ForeignKey(
        'DataSet',
        related_name='+',
        db_column='datasetid',
        on_delete=models.CASCADE,
    )
    result = models.ForeignKey(
        'Result',
        related_name='+',
        db_column='resultid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<DataSetResult('%s', Result['%s', '%s'], DataSet['%s', '%s'])>"
            % (
                self.bridge_id,
                self.result_id,
                self.result,
                self.data_set_id,
                self.data_set,
            )
        )

    class Meta:
        db_table = 'datasetsresults'


class DataQuality(models.Model):
    data_quality_id = models.AutoField(
        db_column='dataqualityid', primary_key=True
    )
    data_quality_type = models.ForeignKey(
        'DataQualityType',
        db_column='dataqualitytypecv',
        on_delete=models.CASCADE,
    )
    data_quality_code = models.CharField(
        db_column='dataqualitycode', max_length=255
    )
    data_quality_value = models.FloatField(
        db_column='dataqualityvalue', blank=True, null=True
    )
    data_quality_value_unit = models.ForeignKey(
        'Unit',
        db_column='dataqualityvalueunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    data_quality_description = models.CharField(
        db_column='dataqualitydescription', blank=True, max_length=500
    )
    data_quality_link = models.CharField(
        db_column='dataqualitylink', blank=True, max_length=255
    )

    def __repr__(self):
        return "<DataQuality('%s', '%s', '%s', '%s')>" % (
            self.data_quality_id,
            self.data_quality_type_id,
            self.data_quality_code,
            self.data_quality_value,
        )

    class Meta:
        db_table = 'dataquality'


class ReferenceMaterial(models.Model):
    reference_material_id = models.AutoField(
        db_column='referencematerialid', primary_key=True
    )
    reference_material_medium = models.ForeignKey(
        'Medium',
        db_column='referencematerialmediumcv',
        on_delete=models.CASCADE,
    )
    reference_material_organization = models.ForeignKey(
        'Organization',
        db_column='referencematerialorganizationid',
        on_delete=models.CASCADE,
    )
    reference_material_code = models.CharField(
        db_column='referencematerialcode', max_length=50
    )
    reference_material_lot_code = models.CharField(
        db_column='referencemateriallotcode', blank=True, max_length=255
    )
    reference_material_purchase_date = models.DateTimeField(
        db_column='referencematerialpurchasedate', blank=True, null=True
    )
    reference_material_expiration_date = models.DateTimeField(
        db_column='referencematerialexpirationdate', blank=True, null=True
    )
    reference_material_certificate_link = models.FileField(
        db_column='referencematerialcertificatelink', blank=True
    )  # TODO: is it a link or a file link?  BOTH
    sampling_feature = models.ForeignKey(
        'SamplingFeature',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    external_identifiers = models.ManyToManyField(
        'ExternalIdentifierSystem',
        related_name='reference_materials',
        through='ReferenceMaterialExternalIdentifier',
    )

    def __repr__(self):
        return (
            "<ReferenceMaterial('%s', '%s', '%s', Organization['%s', '%s'])>"
            % (
                self.reference_material_id,
                self.reference_material_code,
                self.reference_material_purchase_date,
                self.reference_material_organization_id,
                self.reference_material_organization,
            )
        )

    class Meta:
        db_table = 'referencematerials'


class CalibrationStandard(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    action = models.ForeignKey(
        'CalibrationAction',
        related_name='+',
        db_column='actionid',
        on_delete=models.CASCADE,
    )
    reference_material = models.ForeignKey(
        'ReferenceMaterial',
        related_name='+',
        db_column='calibration_standards',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<CalibrationStandard('%s', CalibrationAction['%s', '%s'], ReferenceMaterial['%s', '%s'])>"
            % (
                self.bridge_id,
                self.action_id,
                self.action,
                self.reference_material_id,
                self.reference_material,
            )
        )

    class Meta:
        db_table = 'calibrationstandards'


class ReferenceMaterialValue(models.Model):
    reference_material_value_id = models.AutoField(
        db_column='referencematerialvalueid', primary_key=True
    )
    reference_material = models.ForeignKey(
        'ReferenceMaterial',
        related_name='referencematerialvalue',
        db_column='referencematerialid',
        on_delete=models.CASCADE,
    )
    reference_material_value = models.FloatField(
        db_column='referencematerialvalue'
    )
    reference_material_accuracy = models.FloatField(
        db_column='referencematerialaccuracy', blank=True, null=True
    )
    variable = models.ForeignKey(
        'Variable', db_column='variableid', on_delete=models.CASCADE
    )
    unit = models.ForeignKey(
        'Unit', db_column='unitsid', on_delete=models.CASCADE
    )
    citation = models.ForeignKey(
        'Citation',
        db_column='citationid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __repr__(self):
        return (
            "<ReferenceMaterialValue('%s', ReferenceMaterial['%s', '%s'], '%s')>"
            % (
                self.reference_material_value_id,
                self.reference_material_id,
                self.reference_material,
                self.reference_material_value,
            )
        )

    class Meta:
        db_table = 'referencematerialvalues'


class ResultNormalizationValue(models.Model):
    result = models.OneToOneField(
        'Result',
        db_column='resultid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    normalized_by_reference_material_value = models.ForeignKey(
        'ReferenceMaterialValue',
        db_column='normalizedbyreferencematerialvalueid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<ResultNormalizationValue('%s', '%s', ReferenceMaterialValue['%s', '%s'])>"
            % (
                self.result_id,
                self.result,
                self.normalized_by_reference_material_value_id,
                self.normalized_by_reference_material_value,
            )
        )

    class Meta:
        db_table = 'resultnormalizationvalues'


class ResultDataQuality(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    result = models.ForeignKey(
        'Result',
        related_name='+',
        db_column='resultid',
        on_delete=models.CASCADE,
    )
    data_quality = models.ForeignKey(
        'DataQuality',
        related_name='+',
        db_column='dataqualityid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<ResultDataQuality('%s', Result['%s', '%s'], DataQuality['%s', '%s'])>"
            % (
                self.bridge_id,
                self.result_id,
                self.result,
                self.data_quality_id,
                self.data_quality,
            )
        )

    class Meta:
        db_table = 'resultsdataquality'
