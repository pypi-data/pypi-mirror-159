from .abstracts import ControlledVocabulary


class ActionType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_actiontype'


class AggregationStatistic(ControlledVocabulary):
    class Meta:
        db_table = 'cv_aggregationstatistic'


class AnnotationType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_annotationtype'


class CensorCode(ControlledVocabulary):
    class Meta:
        db_table = 'cv_censorcode'


class DataQualityType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_dataqualitytype'


class DataSetType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_datasettype'


class DeploymentType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_deploymenttype'


class DirectiveType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_directivetype'


class ElevationDatum(ControlledVocabulary):
    class Meta:
        db_table = 'cv_elevationdatum'
        ordering = ['name']


class EquipmentType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_equipmenttype'


class Medium(ControlledVocabulary):
    class Meta:
        db_table = 'cv_medium'
        ordering = ['name']


class MethodType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_methodtype'
        ordering = ['name']


class OrganizationType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_organizationtype'
        ordering = ['name']


class PropertyDataType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_propertydatatype'


class QualityCode(ControlledVocabulary):
    class Meta:
        db_table = 'cv_qualitycode'


class ResultType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_resulttype'


class RelationshipType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_relationshiptype'


class SamplingFeatureGeoType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_samplingfeaturegeotype'


class SamplingFeatureType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_samplingfeaturetype'


class SpatialOffsetType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_spatialoffsettype'


class Speciation(ControlledVocabulary):
    class Meta:
        db_table = 'cv_speciation'


class SpecimenType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_specimentype'


class SiteType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_sitetype'
        ordering = ['name']


class Status(ControlledVocabulary):
    class Meta:
        db_table = 'cv_status'


class TaxonomicClassifierType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_taxonomicclassifiertype'


class UnitsType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_unitstype'
        ordering = ['name']


class VariableName(ControlledVocabulary):
    class Meta:
        db_table = 'cv_variablename'
        ordering = ['name']


class VariableType(ControlledVocabulary):
    class Meta:
        db_table = 'cv_variabletype'
        ordering = ['name']


class ReferenceMaterialMedium(ControlledVocabulary):
    class Meta:
        db_table = 'cv_referencematerialmedium'
