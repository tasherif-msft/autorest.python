from .base_schema import BaseSchema
from typing import Any, Dict
from ..common.utils import get_enum_name


class EnumValue:
    def __init__(self, name, value, **kwargs):
        self.name = name
        self.value = value
        self.description = kwargs.pop('description', None)

    @classmethod
    def from_yaml(cls, yaml_data):
        name = get_enum_name(yaml_data['language']['default']['name'])
        return cls(
            name=name,
            value=yaml_data['value'],
            description=yaml_data['language']['default'].get('description')
        )

class EnumSchema(BaseSchema):
    def __init__(self, yaml_data, name, description, enum_type, values, **kwargs):
        super(EnumSchema, self).__init__(yaml_data, name, **kwargs)
        self.description = description
        self.enum_type = enum_type
        self.values = values

    def __eq__(self, other):
        return isinstance(other, EnumSchema) and other.name == self.name

    def __hash__(self):
        return hash(self.name)

    def get_serialization_type(self):
        return 'str'

    def get_doc_string_type(self, namespace):
        return "str or ~{}.models.{}".format(namespace, self.enum_type)

    @classmethod
    def _get_enum_values(cls, yaml_data):
        values = []
        for enum in yaml_data:
            values.append(EnumValue.from_yaml(enum))
        return values

    @classmethod
    def from_yaml(cls, name: str, yaml_data: Dict[str, str], **kwargs: Any) -> "EnumType":
        enum_type = yaml_data['language']['default']['name']
        values = cls._get_enum_values(yaml_data['choices'])

        return cls(
            yaml_data=yaml_data,
            name=get_enum_name(name),
            description=yaml_data['language']['default']['description'],
            enum_type=enum_type,
            values=values
        )
