from lowcode_cli.common.constant.filetype import TypeDefaultValueMap


def get_field_names(schema: dict):
    fields = schema['properties']['fields']['properties']
    return fields.keys()


def get_field_default_value(schema: dict):
    fields = schema['properties']['fields']['properties']
    items = {}
    for key, value in fields.items():
        _type = value.get('type')
        default = value.get('default', TypeDefaultValueMap.get(_type))
        if isinstance(default, str):
            default = f'"{default}"'
        elif _type == 'multi-select':
            default = []
        else:
            default = 'null'

        items[key] = default

    return items


def get_searchable_fields(schema: dict):
    fields = schema['properties']['fields']['properties']
    items = {}
    for key, value in fields.items():
        if value.get('searchable') is True:
            items[key] = value
    return items


def get_filterable_fields(schema: dict):
    fields = schema['properties']['fields']['properties']
    items = {}
    for key, value in fields.items():
        if value.get('filterable') is True:
            items[key] = value
    return items


def image_field_exists(schema: dict):
    fields = schema['properties']['fields']['properties']
    values = fields.values()
    return len([item for item in values if item['type'] == 'image'])
