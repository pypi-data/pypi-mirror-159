from django.db import models

from .abstracts import ObjectRelation


class AuthorList(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    citation = models.ForeignKey(
        'Citation', db_column='citationid', on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        'People', db_column='personid', on_delete=models.CASCADE
    )
    author_order = models.IntegerField(db_column='authororder')

    def __repr__(self):
        return (
            "<VariableExternalIdentifier('%s', Person['%s', '%s'], Citation['%s', '%s'], '%s')>"
            % (
                self.bridge_id,
                self.person_id,
                self.person,
                self.citation_id,
                self.citation,
                self.author_order,
            )
        )

    class Meta:
        db_table = 'authorlists'


class DataSetCitation(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    data_set = models.ForeignKey(
        'DataSet', db_column='datasetid', on_delete=models.CASCADE
    )
    relationship_type = models.ForeignKey(
        'RelationshipType',
        db_column='relationshiptypecv',
        on_delete=models.CASCADE,
    )
    citation = models.ForeignKey(
        'Citation', db_column='citationid', on_delete=models.CASCADE
    )

    def __repr__(self):
        return (
            "<DataSetCitation('%s', DataSet['%s', '%s'], '%s', Citation['%s', '%s'])>"
            % (
                self.bridge_id,
                self.data_set_id,
                self.data_set,
                self.relationship_type_id,
                self.citation_id,
                self.citation,
            )
        )

    class Meta:
        db_table = 'datasetcitations'


class DerivationEquation(models.Model):
    derivation_equation_id = models.AutoField(
        db_column='derivationequationid', primary_key=True
    )
    derivation_equation = models.CharField(
        db_column='derivationequation', max_length=255
    )

    def __repr__(self):
        return "<DerivationEquation('%s', '%s')>" % (
            self.derivation_equation_id,
            self.derivation_equation,
        )

    class Meta:
        db_table = 'derivationequations'


class ResultDerivationEquation(models.Model):
    result = models.OneToOneField(
        'Result',
        db_column='resultid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    derivation_equation = models.ForeignKey(
        'DerivationEquation',
        db_column='derivationequationid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<ResultDerivationEquation('%s', '%s', DerivationEquation['%s', '%s'])>"
            % (
                self.result_id,
                self.result,
                self.derivation_equation_id,
                self.derivation_equation,
            )
        )

    class Meta:
        db_table = 'resultderivationequations'


class MethodCitation(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    method = models.ForeignKey(
        'Method', db_column='methodid', on_delete=models.CASCADE
    )
    relationship_type = models.ForeignKey(
        'RelationshipType',
        db_column='relationshiptypecv',
        on_delete=models.CASCADE,
    )
    citation = models.ForeignKey(
        'Citation', db_column='citationid', on_delete=models.CASCADE
    )

    def __repr__(self):
        return (
            "<MethodCitation('%s', Method['%s', '%s'], '%s', Citation['%s', '%s'])>"
            % (
                self.bridge_id,
                self.method_id,
                self.method,
                self.relationship_type_id,
                self.citation_id,
                self.citation,
            )
        )

    class Meta:
        db_table = 'methodcitations'


class RelatedAnnotation(ObjectRelation):
    annotation = models.ForeignKey(
        'Annotation',
        related_name='related_annonation_annotation',
        db_column='annotationid',
        on_delete=models.CASCADE,
    )
    related_annotation = models.ForeignKey(
        'Annotation',
        related_name='related_annotation_related_annontation',
        db_column='relatedannotationid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<RelatedAnnotation('%s', Annotation['%s', '%s'], '%s', Annotation['%s', '%s'])>"
            % (
                self.relation_id,
                self.annotation_id,
                self.annotation,
                self.relationship_type_id,
                self.related_annotation_id,
                self.related_annotation,
            )
        )

    class Meta:
        db_table = 'relatedannotations'


class RelatedDataSet(ObjectRelation):
    data_set = models.ForeignKey(
        'DataSet',
        related_name='related_dataset_dataset',
        db_column='datasetid',
        on_delete=models.CASCADE,
    )
    related_data_set = models.ForeignKey(
        'DataSet',
        related_name='related_dataset_related_dataset',
        db_column='relateddatasetid',
        on_delete=models.CASCADE,
    )
    version_code = models.CharField(
        db_column='versioncode', blank=True, max_length=50
    )

    def __repr__(self):
        return (
            "<RelatedDataSet('%s', DataSet['%s', '%s'], '%s', DataSet['%s', '%s'], '%s')>"
            % (
                self.relation_id,
                self.data_set_id,
                self.data_set,
                self.relationship_type_id,
                self.related_data_set_id,
                self.related_data_set,
                self.version_code,
            )
        )

    class Meta:
        db_table = 'relateddatasets'


class RelatedResult(ObjectRelation):
    result = models.ForeignKey(
        'Result', db_column='resultid', on_delete=models.CASCADE
    )
    related_result = models.ForeignKey(
        'Result',
        related_name='related_result_related_result',
        db_column='relatedresultid',
        on_delete=models.CASCADE,
    )
    version_code = models.CharField(
        db_column='versioncode', blank=True, max_length=50
    )
    related_result_sequence_number = models.IntegerField(
        db_column='relatedresultsequencenumber', blank=True, null=True
    )

    def __repr__(self):
        return (
            "<RelatedResult('%s', Result['%s', '%s'], '%s', Result['%s', '%s'], '%s')>"
            % (
                self.relation_id,
                self.result_id,
                self.result,
                self.relationship_type_id,
                self.related_result_id,
                self.related_result,
                self.version_code,
            )
        )

    class Meta:
        db_table = 'relatedresults'
