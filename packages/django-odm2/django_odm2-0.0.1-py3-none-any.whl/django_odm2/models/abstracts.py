from django.db import models

from ..querysets import ODM2QuerySet


class ODM2Model(models.Model):
    objects = ODM2QuerySet.as_manager()

    class Meta:
        abstract = True


class ControlledVocabulary(ODM2Model):
    term = models.CharField(db_column='term', max_length=255)
    name = models.CharField(db_column='name', primary_key=True, max_length=255)
    definition = models.TextField(db_column='definition', blank=True)
    category = models.CharField(
        db_column='category', blank=True, max_length=255
    )
    source_vocabulary_uri = models.CharField(
        db_column='sourcevocabularyuri', blank=True, max_length=255
    )

    def __str__(self):
        return '%s' % self.name

    def __repr__(self):
        return "<%s('%s', '%s', '%s', '%s')>" % (
            self.__class__.__name__,
            self.term,
            self.name,
            self.definition,
            self.category,
        )

    class Meta:
        abstract = True


class AnnotationBridge(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    annotation = models.ForeignKey(
        'Annotation', db_column='annotationid', on_delete=models.CASCADE
    )

    def __str__(self):
        return '%s' % self.annotation

    class Meta:
        abstract = True


class ExtensionPropertyBridge(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    property = models.ForeignKey(
        'ExtensionProperty', db_column='propertyid', on_delete=models.CASCADE
    )
    property_value = models.CharField(
        db_column='propertyvalue', max_length=255
    )

    def __str__(self):
        return '%s' % self.property_value

    class Meta:
        abstract = True


class ExternalIdentifierBridge(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    external_identifier_system = models.ForeignKey(
        'ExternalIdentifierSystem',
        db_column='externalidentifiersystemid',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '%s' % self.external_identifier_system

    class Meta:
        abstract = True


class ObjectRelation(models.Model):
    relation_id = models.AutoField(db_column='relationid', primary_key=True)
    relationship_type = models.ForeignKey(
        'RelationshipType',
        db_column='relationshiptypecv',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return '%s' % self.relationship_type_id

    class Meta:
        abstract = True
