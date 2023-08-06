from convert_case import camel_case


def camel_case_filter(value: str):
    value = value.replace('-', '_')
    return camel_case(value)


def static_props_dict_to_props(props: dict = None) -> str:
    if not props:
        return ''
    items = []
    for key, value in props.items():
        if isinstance(value, bool):
            if value is False:
                continue
            else:
                items.append(key)
        else:
            items.append(f'{key}="{value}"')

    return ' '.join(items)


def dynamic_props_dict_to_props(props: dict = None) -> str:
    if not props:
        return ''
    prop_array = [f':{key}="{value}"' for key, value in props.items()]
    return ' '.join(prop_array)


def search_placeholder(searchable_fields: dict):
    items = []
    for key, value in searchable_fields.items():
        items.append(value.get('label', key))

    return '/'.join(items)
