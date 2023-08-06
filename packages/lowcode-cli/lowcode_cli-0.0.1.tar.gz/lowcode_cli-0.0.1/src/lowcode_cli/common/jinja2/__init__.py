from jinja2 import FileSystemLoader, Environment
from lowcode_cli.conf import settings
from lowcode_cli.common.jinja2 import filters
from lowcode_cli.common.jinja2 import handles

loader = FileSystemLoader(settings.TEMPLATE_DIR)
env = Environment(loader=loader, trim_blocks=True)

env.variable_start_string = '{[ '
env.variable_end_string = ' ]}'

env.filters['camel_case_filter'] = filters.camel_case_filter
env.filters['static_props_dict_to_props'] = filters.static_props_dict_to_props
env.filters['dynamic_props_dict_to_props'] = filters.dynamic_props_dict_to_props
env.filters['search_placeholder'] = filters.search_placeholder
env.globals['get_field_names'] = handles.get_field_names
env.globals['get_field_default_value'] = handles.get_field_default_value
env.globals['get_searchable_fields'] = handles.get_searchable_fields
env.globals['get_filterable_fields'] = handles.get_filterable_fields
env.globals['image_field_exists'] = handles.image_field_exists

env.add_extension('jinja2.ext.loopcontrols')
