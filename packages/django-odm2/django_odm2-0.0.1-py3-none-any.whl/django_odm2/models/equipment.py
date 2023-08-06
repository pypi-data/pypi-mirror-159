from django.db import models

from ..querysets import (
    CalibrationActionManager,
    CalibrationReferenceEquipmentManager,
    DataLoggerFileManager,
    EquipmentManager,
    EquipmentModelQuerySet,
    EquipmentUsedManager,
    InstrumentOutputVariableManager,
    MaintenanceActionManager,
    RelatedEquipmentManager,
)
from .abstracts import ObjectRelation
from .core import Action


class DataLoggerProgramFile(models.Model):
    program_id = models.AutoField(db_column='programid', primary_key=True)
    affiliation = models.ForeignKey(
        'Affiliation',
        db_column='affiliationid',
        on_delete=models.CASCADE,
        related_name='data_logger_programs',
    )
    program_name = models.CharField(db_column='programname', max_length=255)
    program_description = models.CharField(
        db_column='programdescription', blank=True, max_length=500
    )
    program_version = models.CharField(
        db_column='programversion', blank=True, max_length=50
    )
    program_file_link = models.FileField(
        db_column='programfilelink', blank=True
    )

    def __str__(self):
        return '%s %s' % (self.program_name, self.program_version)

    def __repr__(self):
        return "<DataLoggerProgramFile('%s', '%s', '%s')>" % (
            self.program_id,
            self.program_name,
            self.program_version,
        )

    class Meta:
        db_table = 'dataloggerprogramfiles'


class DataLoggerFile(models.Model):
    data_logger_file_id = models.AutoField(
        db_column='dataloggerfileid', primary_key=True
    )
    program = models.ForeignKey(
        'DataLoggerProgramFile',
        db_column='programid',
        on_delete=models.CASCADE,
        related_name='data_logger_files',
    )
    data_logger_file_name = models.CharField(
        db_column='dataloggerfilename', max_length=255
    )
    data_logger_file_description = models.CharField(
        db_column='dataloggerfiledescription', blank=True, max_length=500
    )
    data_logger_file_link = models.FileField(
        db_column='dataloggerfilelink', blank=True
    )

    objects = DataLoggerFileManager()

    def __str__(self):
        return '%s in %s' % (self.data_logger_file_name, self.program)

    def __repr__(self):
        return (
            "<DataLoggerFile('%s', '%s', '%s', DataLoggerProgramFile[%s, %s])>"
            % (
                self.data_logger_file_id,
                self.data_logger_file_name,
                self.data_logger_file_link,
                self.program_id,
                self.program,
            )
        )

    class Meta:
        db_table = 'dataloggerfiles'


class DataLoggerFileColumn(models.Model):
    data_logger_file_column_id = models.AutoField(
        db_column='dataloggerfilecolumnid', primary_key=True
    )
    result = models.ForeignKey(
        'Result',
        related_name='data_logger_file_columns',
        db_column='resultid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    data_logger_file = models.ForeignKey(
        'DataLoggerFile',
        related_name='data_logger_file_columns',
        db_column='dataloggerfileid',
        on_delete=models.CASCADE,
    )
    instrument_output_variable = models.ForeignKey(
        'InstrumentOutputVariable',
        related_name='data_logger_file_columns',
        db_column='instrumentoutputvariableid',
        on_delete=models.CASCADE,
    )
    column_label = models.CharField(db_column='columnlabel', max_length=50)
    column_description = models.CharField(
        db_column='columndescription', blank=True, max_length=500
    )
    measurement_equation = models.CharField(
        db_column='measurementequation', blank=True, max_length=255
    )
    scan_interval = models.FloatField(
        db_column='scaninterval', blank=True, null=True
    )
    scan_interval_unit = models.ForeignKey(
        'Unit',
        related_name='scan_interval_data_logger_file_columns',
        db_column='scanintervalunitsid',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    recording_interval = models.FloatField(
        db_column='recordinginterval', blank=True, null=True
    )
    recording_interval_unit = models.ForeignKey(
        'Unit',
        related_name='recording_interval_data_logger_file_columns',
        db_column='recordingintervalunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    aggregation_statistic = models.ForeignKey(
        'AggregationStatistic',
        related_name='data_logger_file_columns',
        db_column='aggregationstatisticcv',
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return '%s %s' % (self.column_label, self.column_description)

    def __repr__(self):
        return "<DataLoggerFileColumn('%s', '%s', Result['%s', '%s'])>" % (
            self.data_logger_file_column_id,
            self.column_label,
            self.result_id,
            self.result,
        )

    class Meta:
        db_table = 'dataloggerfilecolumns'


class EquipmentModel(models.Model):
    equipment_model_id = models.AutoField(
        db_column='equipmentmodelid', primary_key=True
    )
    model_manufacturer = models.ForeignKey(
        'Organization',
        db_column='modelmanufacturerid',
        on_delete=models.CASCADE,
    )
    model_part_number = models.CharField(
        db_column='modelpartnumber', blank=True, max_length=50
    )
    model_name = models.CharField(db_column='modelname', max_length=255)
    model_description = models.CharField(
        db_column='modeldescription', blank=True, max_length=500
    )
    is_instrument = models.BooleanField(db_column='isinstrument', default=None)
    model_specifications_file_link = models.FileField(
        db_column='modelspecificationsfilelink', blank=True
    )
    model_link = models.CharField(
        db_column='modellink', blank=True, max_length=255
    )

    output_variables = models.ManyToManyField(
        'Variable',
        related_name='instrument_models',
        through='InstrumentOutputVariable',
    )
    output_units = models.ManyToManyField(
        'Unit',
        related_name='instrument_models',
        through='InstrumentOutputVariable',
    )

    objects = EquipmentModelQuerySet.as_manager()

    def __str__(self):
        return '%s' % self.model_name

    def __repr__(self):
        return "<EquipmentModel('%s', '%s', '%s', Organization[%s, %s])>" % (
            self.equipment_model_id,
            self.model_name,
            self.model_description,
            self.model_manufacturer_id,
            self.model_manufacturer,
        )

    class Meta:
        db_table = 'equipmentmodels'
        ordering = ['model_manufacturer', 'model_name']


class InstrumentOutputVariable(models.Model):
    instrument_output_variable_id = models.AutoField(
        db_column='instrumentoutputvariableid', primary_key=True
    )
    model = models.ForeignKey(
        'EquipmentModel',
        related_name='instrument_output_variables',
        db_column='modelid',
        on_delete=models.CASCADE,
    )
    variable = models.ForeignKey(
        'Variable',
        related_name='instrument_output_variables',
        db_column='variableid',
        on_delete=models.CASCADE,
    )
    instrument_method = models.ForeignKey(
        'Method',
        related_name='instrument_output_variables',
        db_column='instrumentmethodid',
        on_delete=models.CASCADE,
    )
    instrument_resolution = models.CharField(
        db_column='instrumentresolution', blank=True, max_length=255
    )
    instrument_accuracy = models.CharField(
        db_column='instrumentaccuracy', blank=True, max_length=255
    )
    instrument_raw_output_unit = models.ForeignKey(
        'Unit',
        related_name='instrument_output_variables',
        db_column='instrumentrawoutputunitsid',
        on_delete=models.CASCADE,
    )

    objects = InstrumentOutputVariableManager()

    def __str__(self):
        return '%s: %s measured in %s' % (
            self.model.model_manufacturer,
            self.variable.variable_code,
            self.instrument_raw_output_unit.unit_abbreviation,
        )

    def __repr__(self):
        return (
            "<InstrumentOutputVariable('%s', EquipmentModel['%s', '%s'], Variable['%s', '%s'], Unit['%s', '%s'], Method['%s', '%s'])>"
            % (
                self.instrument_output_variable_id,
                self.model_id,
                self.model,
                self.variable_id,
                self.variable,
                self.instrument_raw_output_unit_id,
                self.instrument_raw_output_unit,
                self.instrument_method_id,
                self.instrument_method,
            )
        )

    class Meta:
        db_table = 'instrumentoutputvariables'
        ordering = ['model__model_manufacturer', 'variable__variable_code']


class Equipment(models.Model):
    equipment_id = models.AutoField(db_column='equipmentid', primary_key=True)
    equipment_code = models.CharField(db_column='equipmentcode', max_length=50)
    equipment_name = models.CharField(
        db_column='equipmentname', max_length=255
    )
    equipment_type = models.ForeignKey(
        'EquipmentType', db_column='equipmenttypecv', on_delete=models.CASCADE
    )
    equipment_model = models.ForeignKey(
        'EquipmentModel',
        related_name='equipment',
        db_column='equipmentmodelid',
        on_delete=models.CASCADE,
    )
    equipment_serial_number = models.CharField(
        db_column='equipmentserialnumber', max_length=50
    )
    equipment_owner = models.ForeignKey(
        'People',
        related_name='owned_equipment',
        db_column='equipmentownerid',
        on_delete=models.CASCADE,
    )
    equipment_vendor = models.ForeignKey(
        'Organization',
        related_name='equipment',
        db_column='equipmentvendorid',
        on_delete=models.CASCADE,
    )
    equipment_purchase_date = models.DateTimeField(
        db_column='equipmentpurchasedate'
    )
    equipment_purchase_order_number = models.CharField(
        db_column='equipmentpurchaseordernumber', blank=True, max_length=50
    )
    equipment_description = models.CharField(
        db_column='equipmentdescription', blank=True, max_length=500
    )
    equipment_documentation_link = models.FileField(
        db_column='equipmentdocumentationlink', blank=True
    )

    annotations = models.ManyToManyField(
        'Annotation',
        related_name='annotated_equipment',
        through='EquipmentAnnotation',
    )
    objects = EquipmentManager()

    def __str__(self):
        return '%s %s (%s)' % (
            self.equipment_serial_number,
            self.equipment_model,
            self.equipment_type_id,
        )

    def __repr__(self):
        return (
            "<Equipment('%s', '%s', '%s', '%s', '%s', EquipmentModel['%s', '%s'], Person['%s', '%s'], Organization['%s', '%s'])>"
            % (
                self.equipment_id,
                self.equipment_code,
                self.equipment_type,
                self.equipment_serial_number,
                self.equipment_purchase_date,
                self.equipment_model_id,
                self.equipment_model,
                self.equipment_owner_id,
                self.equipment_owner,
                self.equipment_vendor_id,
                self.equipment_vendor,
            )
        )

    class Meta:
        db_table = 'equipment'


class CalibrationReferenceEquipment(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    action = models.ForeignKey(
        'CalibrationAction',
        related_name='+',
        db_column='actionid',
        on_delete=models.CASCADE,
    )
    equipment = models.ForeignKey(
        'Equipment',
        related_name='+',
        db_column='equipmentid',
        on_delete=models.CASCADE,
    )

    objects = CalibrationReferenceEquipmentManager()

    def __str__(self):
        return '%s of %s' % (self.action, self.equipment)

    def __repr__(self):
        return (
            "<CalibrationReferenceEquipment('%s', CalibrationAction['%s', '%s'], Equipment['%s', '%s'])>"
            % (
                self.bridge_id,
                self.action_id,
                self.action,
                self.equipment_id,
                self.equipment,
            )
        )

    class Meta:
        db_table = 'calibrationreferenceequipment'


class EquipmentUsed(models.Model):
    bridge_id = models.AutoField(db_column='bridgeid', primary_key=True)
    action = models.ForeignKey(
        'Action',
        related_name='+',
        db_column='actionid',
        on_delete=models.CASCADE,
    )
    equipment = models.ForeignKey(
        'Equipment',
        related_name='+',
        db_column='equipmentid',
        on_delete=models.CASCADE,
    )

    objects = EquipmentUsedManager()

    def __str__(self):
        return '%s of %s' % (self.action, self.equipment)

    def __repr__(self):
        return (
            "<EquipmentUsed('%s', Action['%s', '%s'], Equipment['%s', '%s'])>"
            % (
                self.bridge_id,
                self.action_id,
                self.action,
                self.equipment_id,
                self.equipment,
            )
        )

    class Meta:
        db_table = 'equipmentused'


class MaintenanceAction(models.Model):
    action = models.OneToOneField(
        Action,
        related_name='maintenance',
        db_column='actionid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_factory_service = models.BooleanField(
        db_column='isfactoryservice', default=None
    )
    maintenance_code = models.CharField(
        db_column='maintenancecode', blank=True, max_length=50
    )
    maintenance_reason = models.CharField(
        db_column='maintenancereason', blank=True, max_length=500
    )

    objects = MaintenanceActionManager()

    def __str__(self):
        return '%s: %s - %s' % (
            self.action,
            self.maintenance_code,
            self.maintenance_reason,
        )

    def __repr__(self):
        return "<MaintenanceAction('%s', '%s', '%s', '%s')>" % (
            self.action_id,
            self.action.begin_datetime,
            self.maintenance_code,
            self.maintenance_reason,
        )

    class Meta:
        db_table = 'maintenanceactions'


class RelatedEquipment(ObjectRelation):
    equipment = models.ForeignKey(
        'Equipment',
        related_name='related_equipment',
        db_column='equipmentid',
        on_delete=models.CASCADE,
    )
    related_equipment = models.ForeignKey(
        'Equipment',
        related_name='reverse_related_equipment',
        db_column='relatedequipmentid',
        on_delete=models.CASCADE,
    )
    relationship_start_datetime = models.DateTimeField(
        db_column='relationshipstartdatetime'
    )
    relationship_start_datetime_utc_offset = models.IntegerField(
        db_column='relationshipstartdatetimeutcoffset'
    )
    relationship_end_datetime = models.DateTimeField(
        db_column='relationshipenddatetime', blank=True, null=True
    )
    relationship_end_datetime_utc_offset = models.IntegerField(
        db_column='relationshipenddatetimeutcoffset', blank=True, null=True
    )

    objects = RelatedEquipmentManager()

    def __str__(self):
        return '%s %s %s' % (
            self.equipment,
            self.relationship_type_id,
            self.related_equipment,
        )

    def __repr__(self):
        return (
            "<RelatedEquipment('%s', Equipment['%s', '%s'], '%s', Equipment['%s', '%s'])>"
            % (
                self.relation_id,
                self.equipment_id,
                self.equipment,
                self.relationship_type_id,
                self.related_equipment_id,
                self.related_equipment,
            )
        )

    class Meta:
        db_table = 'relatedequipment'


class CalibrationAction(models.Model):
    action = models.OneToOneField(
        Action,
        related_name='calibration',
        db_column='actionid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    calibration_check_value = models.FloatField(
        db_column='calibrationcheckvalue', blank=True, null=True
    )
    instrument_output_variable = models.ForeignKey(
        'InstrumentOutputVariable',
        db_column='instrumentoutputvariableid',
        on_delete=models.CASCADE,
    )
    calibration_equation = models.CharField(
        db_column='calibrationequation', blank=True, max_length=255
    )

    calibration_standards = models.ManyToManyField(
        'ReferenceMaterial',
        related_name='calibration_actions',
        through='CalibrationStandard',
    )
    reference_equipment = models.ManyToManyField(
        'Equipment',
        related_name='calibration_reference_actions',
        through='CalibrationReferenceEquipment',
    )
    objects = CalibrationActionManager()

    def __str__(self):
        return '%s: %s' % (self.action, self.instrument_output_variable)

    def __repr__(self):
        return (
            "<CalibrationAction('%s', '%s', '%s', '%s', InstrumentOutputVariable['%s', '%s'])>"
            % (
                self.action_id,
                self.action.begin_datetime,
                self.calibration_equation,
                self.calibration_check_value,
                self.instrument_output_variable_id,
                self.instrument_output_variable,
            )
        )

    class Meta:
        db_table = 'calibrationactions'
