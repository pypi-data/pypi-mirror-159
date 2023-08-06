from octodns.record import Record, ValuesMixin
from octodns.equality import EqualityTupleMixin


class _Route53AliasValue(EqualityTupleMixin):
    @classmethod
    def validate(cls, data, _type):
        if not isinstance(data, (list, tuple)):
            data = (data,)
        reasons = []
        for value in data:
            if 'type' not in value:
                reasons.append('missing type')
            if Route53AliasRecord.is_service_alias(value.get('name') or ''):
                if not value.get('hosted-zone-id'):
                    reasons.append('service alias without hosted-zone-id')
            else:
                if value.get('hosted-zone-id'):
                    reasons.append('hosted-zone-id on a non-service value')

        return reasons

    @classmethod
    def process(cls, values):
        return [_Route53AliasValue(v) for v in values]

    def __init__(self, value):
        self.name = value.get('name') or ''
        self._type = value['type']
        self.evaluate_target_health = value.get('evaluate-target-health', False)
        self.hosted_zone_id = value.get('hosted-zone-id')

    @property
    def data(self):
        return {
            'hosted-zone-id': self.hosted_zone_id,
            'evaluate-target-health': self.evaluate_target_health,
            'name': self.name,
            'type': self._type,
        }

    def __hash__(self):
        return hash((self._type, self.name, self.hosted_zone_id))

    def _equality_tuple(self):
        return (self._type, self.name, self.hosted_zone_id)

    def __repr__(self):
        return f'"{self.name}" {self._type} {self.hosted_zone_id or ""}'


class Route53AliasRecord(ValuesMixin, Record):
    _type = 'Route53Provider/ALIAS'
    _value_type = _Route53AliasValue

    # Since Route53's alias type reuses the same keys for different types of
    # records with nothing to definitively indicate whether it's a service or
    # same-zone symlink we need to guess which based on the fqdn. We can't do
    # an `endswith` due to cases where there are country specific endings on
    # the fqdn, e.g. `.cn`. No clue if this will work for gov-cloud etc. If you
    # encounter a case where a service isn't correctly being detected please
    # open a PR adding it's fqdn bit to the list here or an issue if that
    # doesn't make sense.
    # https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values-alias-common.html#rrsets-values-alias-common-target
    SERVICE_FQDNS = (
        'amazonaws.com.',
        'cloudfront.net.',
        'elasticbeanstalk.com.',
    )

    @classmethod
    def is_service_alias(cls, name):
        for service_fqdn in cls.SERVICE_FQDNS:
            if service_fqdn in name:
                return True
        return False


Record.register_type(Route53AliasRecord)
