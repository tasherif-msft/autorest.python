# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import List
from jinja2 import Environment
from .model_base_serializer import ModelBaseSerializer
from ..models import ObjectSchema, CodeModel


class ModelGenericSerializer(ModelBaseSerializer):

    def __init__(self, code_model: CodeModel, env: Environment) -> None:
        super(ModelGenericSerializer, self).__init__(
            code_model=code_model, env=env, is_python_3_file=False
        )

    @staticmethod
    def init_line(model: ObjectSchema) -> List[str]:
        return []

    @staticmethod
    def init_args(model: ObjectSchema) -> List[str]:
        init_args = []
        init_args.append(f"super({model.name}, self).__init__(**kwargs)")

        for prop in ModelGenericSerializer.get_properties_to_initialize(model):
            if prop.readonly:
                init_args.append(f"self.{prop.name} = None")
            elif prop.is_discriminator:
                discriminator_value = f"'{model.discriminator_value}'" if model.discriminator_value else None
                if not discriminator_value:
                    typing = "Optional[str]"
                else:
                    typing = "str"
                init_args.append(f"self.{prop.name} = {discriminator_value}  # type: {typing}")
            elif not prop.constant:
                if prop.required and not prop.schema.default_value:
                    init_args.append(f"self.{prop.name} = kwargs['{prop.name}']")
                else:
                    default = prop.schema.default_value_declaration
                    init_args.append(f"self.{prop.name} = kwargs.get('{prop.name}', {default})")
        return init_args
