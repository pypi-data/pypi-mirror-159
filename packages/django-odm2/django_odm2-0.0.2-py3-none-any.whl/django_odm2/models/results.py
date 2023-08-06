from django.db import models

from ..querysets import TimeSeriesValuesQuerySet


class ExtendedResult(models.Model):
    result = models.OneToOneField(
        'Result',
        db_column='resultid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    spatial_reference = models.ForeignKey(
        'SpatialReference',
        db_column='spatialreferenceid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return '%s' % self.result

    def __repr__(self):
        return "<%s('%s', '%s', SpatialReference['%s', '%s'])>" % (
            self.__class__.__name__,
            self.result_id,
            self.result,
            self.spatial_reference_id,
            self.spatial_reference,
        )

    class Meta:
        abstract = True


class ResultValue(models.Model):
    value_id = models.BigAutoField(db_column='valueid', primary_key=True)
    value_datetime = models.DateTimeField(db_column='valuedatetime')
    value_datetime_utc_offset = models.IntegerField(
        db_column='valuedatetimeutcoffset'
    )

    def __str__(self):
        return '%s %s' % (self.value_datetime, self.data_value)

    def __repr__(self):
        return "<%s('%s', '%s', Result['%s', '%s'], '%s')>" % (
            self.__class__.__name__,
            self.value_id,
            self.value_datetime,
            self.result_id,
            self.result,
            self.data_value,
        )

    class Meta:
        abstract = True


class ResultValueAnnotation(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    annotation = models.ForeignKey(
        'Annotation', db_column='annotationid', on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s %s' % (self.value_datetime, self.data_value)

    def __repr__(self):
        return "<%s('%s', Annotation['%s', '%s'], ResultValue['%s', '%s')>" % (
            self.__class__.__name__,
            self.bridge_id,
            self.annotation_id,
            self.annotation,
            self.value_id,
            self.value,
        )

    class Meta:
        abstract = True


class AggregatedComponent(models.Model):
    aggregation_statistic = models.ForeignKey(
        'AggregationStatistic',
        db_column='aggregationstatisticcv',
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class TimeAggregationComponent(models.Model):
    time_aggregation_interval = models.FloatField(
        db_column='timeaggregationinterval'
    )
    time_aggregation_interval_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='timeaggregationintervalunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class XOffsetComponent(models.Model):
    x_location = models.FloatField(db_column='xlocation')
    x_location_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='xlocationunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class YOffsetComponent(models.Model):
    y_location = models.FloatField(db_column='ylocation')
    y_location_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='ylocationunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class ZOffsetComponent(models.Model):
    z_location = models.FloatField(db_column='zlocation')
    z_location_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='zlocationunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class XIntendedComponent(models.Model):
    intended_x_spacing = models.FloatField(db_column='intendedxspacing')
    intended_x_spacing_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='intendedxspacingunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class YIntendedComponent(models.Model):
    intended_y_spacing = models.FloatField(
        db_column='intendedyspacing', blank=True, null=True
    )
    intended_y_spacing_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='intendedyspacingunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class ZIntendedComponent(models.Model):
    intended_z_spacing = models.FloatField(
        db_column='intendedzspacing', blank=True, null=True
    )
    intended_z_spacing_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='intendedzspacingunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class TimeIntendedComponent(models.Model):
    intended_time_spacing = models.FloatField(
        db_column='intendedtimespacing', blank=True, null=True
    )
    intended_time_spacing_unit = models.ForeignKey(
        'Unit',
        related_name='+',
        db_column='intendedtimespacingunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True


class QualityControlComponent(models.Model):
    censor_code = models.ForeignKey(
        'CensorCode', db_column='censorcodecv', on_delete=models.CASCADE
    )
    quality_code = models.ForeignKey(
        'QualityCode', db_column='qualitycodecv', on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class PointCoverageResult(
    ExtendedResult,
    AggregatedComponent,
    ZOffsetComponent,
    XIntendedComponent,
    YIntendedComponent,
    TimeAggregationComponent,
):
    class Meta:
        db_table = 'pointcoverageresults'


class ProfileResult(
    ExtendedResult,
    AggregatedComponent,
    XOffsetComponent,
    YOffsetComponent,
    ZIntendedComponent,
    TimeIntendedComponent,
):
    class Meta:
        db_table = 'profileresults'


class CategoricalResult(
    ExtendedResult, XOffsetComponent, YOffsetComponent, ZOffsetComponent
):
    quality_code = models.ForeignKey(
        'QualityCode', db_column='qualitycodecv', on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'categoricalresults'


class TransectResult(
    ExtendedResult,
    AggregatedComponent,
    ZOffsetComponent,
    TimeIntendedComponent,
):
    intended_transect_spacing = models.FloatField(
        db_column='intendedtransectspacing'
    )
    intended_transect_spacing_unit = models.ForeignKey(
        'Unit',
        db_column='intendedtransectspacingunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'transectresults'


class SpectraResult(
    ExtendedResult,
    AggregatedComponent,
    XOffsetComponent,
    YOffsetComponent,
    ZOffsetComponent,
):
    intended_wavelength_spacing = models.FloatField(
        db_column='intendedwavelengthspacing'
    )
    intended_wavelength_spacing_unit = models.ForeignKey(
        'Unit',
        db_column='intendedwavelengthspacingunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'spectraresults'


class TimeSeriesResult(
    ExtendedResult,
    AggregatedComponent,
    XOffsetComponent,
    YOffsetComponent,
    ZOffsetComponent,
    TimeIntendedComponent,
):
    class Meta:
        db_table = 'timeseriesresults'


class SectionResult(
    ExtendedResult,
    AggregatedComponent,
    YOffsetComponent,
    XIntendedComponent,
    ZIntendedComponent,
    TimeIntendedComponent,
):
    class Meta:
        db_table = 'sectionresults'


class TrajectoryResult(
    ExtendedResult, AggregatedComponent, TimeIntendedComponent
):
    intended_trajectory_spacing = models.FloatField(
        db_column='intendedtrajectoryspacing'
    )
    intended_trajectory_spacing_unit = models.ForeignKey(
        'Unit',
        db_column='intendedtrajectoryspacingunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        db_table = 'trajectoryresults'


class MeasurementResult(
    ExtendedResult,
    AggregatedComponent,
    XOffsetComponent,
    YOffsetComponent,
    ZOffsetComponent,
    TimeAggregationComponent,
    QualityControlComponent,
):
    class Meta:
        db_table = 'measurementresults'


class CategoricalResultValue(ResultValue):
    result = models.ForeignKey(
        'CategoricalResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.CharField(db_column='datavalue', max_length=255)
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_categorical_values',
        through='CategoricalResultValueAnnotation',
    )

    class Meta:
        db_table = 'categoricalresultvalues'


class MeasurementResultValue(ResultValue):
    result = models.ForeignKey(
        'MeasurementResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.FloatField(db_column='datavalue')
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_measurement_values',
        through='MeasurementResultValueAnnotation',
    )

    class Meta:
        db_table = 'measurementresultvalues'


class PointCoverageResultValue(
    ResultValue, XOffsetComponent, YOffsetComponent, QualityControlComponent
):
    result = models.ForeignKey(
        'PointCoverageResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.BigIntegerField(db_column='datavalue')
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_point_coverage_values',
        through='PointCoverageResultValueAnnotation',
    )

    class Meta:
        db_table = 'pointcoverageresultvalues'


class ProfileResultValue(
    ResultValue,
    ZOffsetComponent,
    QualityControlComponent,
    TimeAggregationComponent,
):
    result = models.ForeignKey(
        'ProfileResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.FloatField(db_column='datavalue')
    z_aggregation_interval = models.FloatField(
        db_column='zaggregationinterval'
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_profile_values',
        through='ProfileResultValueAnnotation',
    )

    class Meta:
        db_table = 'profileresultvalues'


class SectionResultValue(
    ResultValue,
    AggregatedComponent,
    XOffsetComponent,
    ZOffsetComponent,
    QualityControlComponent,
    TimeAggregationComponent,
):
    result = models.ForeignKey(
        'SectionResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.FloatField(db_column='datavalue')
    x_aggregation_interval = models.FloatField(
        db_column='xaggregationinterval'
    )
    z_aggregation_interval = models.FloatField(
        db_column='zaggregationinterval'
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_section_values',
        through='SectionResultValueAnnotation',
    )

    class Meta:
        db_table = 'sectionresultvalues'


class SpectraResultValue(
    ResultValue, QualityControlComponent, TimeAggregationComponent
):
    result = models.ForeignKey(
        'SpectraResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.FloatField(db_column='datavalue')
    excitation_wavelength = models.FloatField(db_column='excitationwavelength')
    emission_wavelength = models.FloatField(db_column='emissionwavelength')
    wavelength_unit = models.ForeignKey(
        'Unit', db_column='wavelengthunitsid', on_delete=models.CASCADE
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_spectra_values',
        through='SpectraResultValueAnnotation',
    )

    class Meta:
        db_table = 'spectraresultvalues'


class TimeSeriesResultValue(
    ResultValue, QualityControlComponent, TimeAggregationComponent
):
    result = models.ForeignKey(
        'TimeSeriesResult',
        related_name='values',
        db_column='resultid',
        on_delete=models.CASCADE,
    )
    data_value = models.FloatField(db_column='datavalue')
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_time_series_values',
        through='TimeSeriesResultValueAnnotation',
    )

    objects = TimeSeriesValuesQuerySet.as_manager()

    class Meta:
        db_table = 'timeseriesresultvalues'
        ordering = ('value_datetime',)


class TrajectoryResultValue(
    ResultValue,
    XOffsetComponent,
    YOffsetComponent,
    ZOffsetComponent,
    QualityControlComponent,
    TimeAggregationComponent,
):
    result = models.ForeignKey(
        'TrajectoryResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.FloatField(db_column='datavalue')
    trajectory_distance = models.FloatField(db_column='trajectorydistance')
    trajectory_distance_aggregation_interval = models.FloatField(
        db_column='trajectorydistanceaggregationinterval'
    )
    trajectory_distance_unit = models.ForeignKey(
        'Unit', db_column='trajectorydistanceunitsid', on_delete=models.CASCADE
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_Trajectory_values',
        through='TrajectoryResultValueAnnotation',
    )

    class Meta:
        db_table = 'trajectoryresultvalues'


class TransectResultValue(
    ResultValue,
    AggregatedComponent,
    XOffsetComponent,
    YOffsetComponent,
    QualityControlComponent,
    TimeAggregationComponent,
):
    result = models.ForeignKey(
        'TransectResult', db_column='resultid', on_delete=models.CASCADE
    )
    data_value = models.FloatField(db_column='datavalue')
    transect_distance = models.FloatField(db_column='transectdistance')
    transect_distance_aggregation_interval = models.FloatField(
        db_column='transectdistanceaggregationinterval'
    )
    transect_distance_unit = models.ForeignKey(
        'Unit', db_column='transectdistanceunitsid', on_delete=models.CASCADE
    )
    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_transect_values',
        through='TransectResultValueAnnotation',
    )

    class Meta:
        db_table = 'transectresultvalues'


class MeasurementResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'MeasurementResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'measurementresultvalueannotations'


class CategoricalResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'CategoricalResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'categoricalresultvalueannotations'


class PointCoverageResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'PointCoverageResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'pointcoverageresultvalueannotations'


class ProfileResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'ProfileResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'profileresultvalueannotations'


class SectionResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'SectionResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'sectionresultvalueannotations'


class SpectraResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'SpectraResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'spectraresultvalueannotations'


class TimeSeriesResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'TimeSeriesResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'timeseriesresultvalueannotations'


class TrajectoryResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'TrajectoryResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'trajectoryresultvalueannotations'


class TransectResultValueAnnotation(ResultValueAnnotation):
    value = models.ForeignKey(
        'TransectResultValue',
        related_name='+',
        db_column='valueid',
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = 'transectresultvalueannotations'
