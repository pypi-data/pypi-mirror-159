from django.db import models

from .abstracts import AnnotationBridge


class Annotation(models.Model):
    annotation_id = models.AutoField(
        db_column='annotationid', primary_key=True
    )
    annotation_type = models.ForeignKey(
        'AnnotationType',
        db_column='annotationtypecv',
        on_delete=models.CASCADE,
    )
    annotation_code = models.CharField(
        db_column='annotationcode', blank=True, max_length=50
    )
    annotation_text = models.CharField(
        db_column='annotationtext', max_length=500
    )
    annotation_datetime = models.DateTimeField(
        db_column='annotationdatetime', blank=True, null=True
    )
    annotation_utc_offset = models.IntegerField(
        db_column='annotationutcoffset', blank=True, null=True
    )
    annotation_link = models.CharField(
        db_column='annotationlink', blank=True, max_length=255
    )
    annotator = models.ForeignKey(
        'People',
        db_column='annotatorid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    citation = models.ForeignKey(
        'Citation',
        db_column='citationid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.annotation_text

    def __repr__(self):
        return "<Annotation('%s', '%s', '%s', '%s', '%s')>" % (
            self.annotation_id,
            self.annotation_type_id,
            self.annotation_datetime,
            self.annotation_code,
            self.annotation_text,
        )

    class Meta:
        db_table = 'annotations'


class ActionAnnotation(AnnotationBridge):
    action = models.ForeignKey(
        'Action',
        related_name='+',
        db_column='actionid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<ActionAnnotation('%s', Annotation['%s', '%s'], Action['%s', '%s'])>"
            % (
                self.bridge_id,
                self.annotation_id,
                self.annotation,
                self.action_id,
                self.action,
            )
        )

    class Meta:
        db_table = 'actionannotations'


class EquipmentAnnotation(AnnotationBridge):
    equipment = models.ForeignKey(
        'Equipment',
        related_name='+',
        db_column='equipmentid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<EquipmentAnnotation('%s', Annotation['%s', '%s'], Equipment['%s', '%s'])>"
            % (
                self.bridge_id,
                self.annotation_id,
                self.annotation,
                self.equipment_id,
                self.equipment,
            )
        )

    class Meta:
        db_table = 'equipmentannotations'


class MethodAnnotation(AnnotationBridge):
    method = models.ForeignKey(
        'Method',
        related_name='+',
        db_column='methodid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<MethodAnnotation('%s', Annotation['%s', '%s'], Method['%s', '%s'])>"
            % (
                self.bridge_id,
                self.annotation_id,
                self.annotation,
                self.method_id,
                self.method,
            )
        )

    class Meta:
        db_table = 'methodannotations'


class ResultAnnotation(AnnotationBridge):
    result = models.ForeignKey(
        'Result',
        related_name='dated_annotations',
        db_column='resultid',
        on_delete=models.CASCADE,
    )
    begin_datetime = models.DateTimeField(db_column='begindatetime')
    end_datetime = models.DateTimeField(db_column='enddatetime')

    def __repr__(self):
        return (
            "<ResultAnnotation('%s', Annotation['%s', '%s'], Result['%s', '%s'])>"
            % (
                self.bridge_id,
                self.annotation_id,
                self.annotation,
                self.result_id,
                self.result,
            )
        )

    class Meta:
        db_table = 'resultannotations'


class SamplingFeatureAnnotation(AnnotationBridge):
    sampling_feature = models.ForeignKey(
        'SamplingFeature',
        related_name='+',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.annotation.__str__()

    def __repr__(self):
        return (
            "<SamplingFeatureAnnotation('%s', Annotation['%s', '%s'], SamplingFeature['%s', '%s'])>"
            % (
                self.bridge_id,
                self.annotation_id,
                self.annotation,
                self.sampling_feature_id,
                self.sampling_feature,
            )
        )

    class Meta:
        db_table = 'samplingfeatureannotations'


__all__ = [
    'Annotation',
    'ActionAnnotation',
    'MethodAnnotation',
    'ResultAnnotation',
    'SamplingFeatureAnnotation',
]
