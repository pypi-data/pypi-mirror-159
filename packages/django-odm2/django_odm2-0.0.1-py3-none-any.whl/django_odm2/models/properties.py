from django.db import models

from .abstracts import ExtensionPropertyBridge


class ExtensionProperty(models.Model):
    property_id = models.AutoField(db_column='propertyid', primary_key=True)
    property_name = models.CharField(db_column='propertyname', max_length=255)
    property_description = models.CharField(
        db_column='propertydescription', blank=True, max_length=500
    )
    property_data_type = models.ForeignKey(
        'PropertyDataType',
        db_column='propertydatatypecv',
        on_delete=models.CASCADE,
    )
    property_units = models.ForeignKey(
        'Unit',
        db_column='propertyunitsid',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __repr__(self):
        return "<ExtensionProperty('%s', '%s', '%s')>" % (
            self.property_id,
            self.property_name,
            self.property_data_type_id,
        )

    class Meta:
        db_table = 'extensionproperties'


class ActionExtensionPropertyValue(ExtensionPropertyBridge):
    action = models.ForeignKey(
        'Action', db_column='actionid', on_delete=models.CASCADE
    )

    def __repr__(self):
        return (
            "<ActionExtensionPropertyValue('%s', '%s', ExtensionProperty['%s', '%s'], Action['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.action_id,
                self.action,
            )
        )

    class Meta:
        db_table = 'actionextensionpropertyvalues'


class CitationExtensionPropertyValue(ExtensionPropertyBridge):
    citation = models.ForeignKey(
        'Citation', db_column='citationid', on_delete=models.CASCADE
    )

    def __repr__(self):
        return (
            "<CitationExtensionPropertyValue('%s', '%s', ExtensionProperty['%s', '%s'], Citation['%s', '%s'])>"
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
        db_table = 'citationextensionpropertyvalues'


class MethodExtensionPropertyValue(ExtensionPropertyBridge):
    method = models.ForeignKey(
        'Method', db_column='methodid', on_delete=models.CASCADE
    )

    def __repr__(self):
        return (
            "<MethodExtensionPropertyValue('%s', '%s', ExtensionProperty['%s', '%s'], Method['%s', '%s'])>"
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
        db_table = 'methodextensionpropertyvalues'


class ResultExtensionPropertyValue(ExtensionPropertyBridge):
    result = models.ForeignKey(
        'Result', db_column='resultid', on_delete=models.CASCADE
    )

    def __repr__(self):
        return (
            "<ResultExtensionPropertyValue('%s', '%s', ExtensionProperty['%s', '%s'], Result['%s', '%s'])>"
            % (
                self.bridge_id,
                self.property_value,
                self.property_id,
                self.property,
                self.result_id,
                self.result,
            )
        )

    class Meta:
        db_table = 'resultextensionpropertyvalues'


class SamplingFeatureExtensionPropertyValue(ExtensionPropertyBridge):
    sampling_feature = models.ForeignKey(
        'SamplingFeature',
        db_column='samplingfeatureid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<SamplingFeatureExtensionPropertyValue('%s', '%s', ExtensionProperty['%s', '%s'], SamplingFeature['%s', '%s'])>"
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
        db_table = 'samplingfeatureextensionpropertyvalues'


class VariableExtensionPropertyValue(ExtensionPropertyBridge):
    variable = models.ForeignKey(
        'Variable', db_column='variableid', on_delete=models.CASCADE
    )

    def __repr__(self):
        return (
            "<VariableExtensionPropertyValue('%s', '%s', ExtensionProperty['%s', '%s'], Variable['%s', '%s'])>"
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
        db_table = 'variableextensionpropertyvalues'
