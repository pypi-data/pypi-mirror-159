from django.db import models


class Directive(models.Model):
    directive_id = models.AutoField(db_column='directiveid', primary_key=True)
    directive_type = models.ForeignKey(
        'DirectiveType', db_column='directivetypecv', on_delete=models.CASCADE
    )
    directive_description = models.CharField(
        db_column='directivedescription', max_length=500
    )

    def __repr__(self):
        return "<Directive('%s', '%s', '%s')>" % (
            self.directive_id,
            self.directive_type_id,
            self.directive_description,
        )

    class Meta:
        db_table = 'directives'


class ActionDirective(models.Model):
    bridge_id = models.IntegerField(db_column='bridgeid', primary_key=True)
    action = models.ForeignKey(
        'Action',
        related_name='+',
        db_column='actionid',
        on_delete=models.CASCADE,
    )
    directive = models.ForeignKey(
        'Directive',
        related_name='+',
        db_column='directiveid',
        on_delete=models.CASCADE,
    )

    def __repr__(self):
        return (
            "<ActionDirective('%s', Action['%s', '%s'], Directive['%s', '%s'])>"
            % (
                self.bridge_id,
                self.action_id,
                self.action,
                self.directive_id,
                self.directive,
            )
        )

    class Meta:
        db_table = 'actiondirectives'


class SpecimenBatchPosition(models.Model):
    feature_action = models.OneToOneField(
        'FeatureAction',
        db_column='featureactionid',
        on_delete=models.CASCADE,
        primary_key=True,
    )
    batch_position_number = models.IntegerField(
        db_column='batchpositionnumber'
    )
    batch_position_label = models.CharField(
        db_column='batchpositionlabel', blank=True, max_length=255
    )

    def __repr__(self):
        return "<SpecimenBatchPosition('%s', '%s', '%s')>" % (
            self.feature_action_id,
            self.batch_position_label,
            self.batch_position_number,
        )

    class Meta:
        db_table = 'specimenbatchpostions'
