import click
from pathlib import Path
from lowcode_cli.conf import settings
from lowcode_cli.common.jsonschema.validators import DefaultValidatingDraft7Validator
import json
import jsonschema
import tempfile
import subprocess
from typing import Union
from lowcode_cli.common.jinja2 import loader, env
from lowcode_cli.common.constant.filetype import FileTypeEnum


def _form_handle(schema: dict) -> str:
    tpl_file = Path('vue-pure-admin') / 'form.vue.tpl'
    tpl_file = str(tpl_file)
    tpl = env.get_template(tpl_file)
    content = tpl.render(schema=schema)
    temp_file = tempfile.mktemp(suffix='.vue')
    Path(temp_file).write_text(content)
    popen = subprocess.run(['prettier', temp_file], stdout=subprocess.PIPE, text=True)
    return popen.stdout


def _table_handle(schema: dict) -> str:
    tpl_file = Path('vue-pure-admin') / 'table.vue.tpl'
    tpl_file = str(tpl_file)
    tpl = env.get_template(tpl_file)
    content = tpl.render(schema=schema)
    temp_file = tempfile.mktemp(suffix='.vue')
    Path(temp_file).write_text(content)
    popen = subprocess.run(['prettier', temp_file], stdout=subprocess.PIPE, text=True)
    return popen.stdout


def _router_handle(schema: dict, output) -> str:
    ...


def _profile_handle(schema: dict, output) -> str:
    ...


def _api_handle(schema: dict, output) -> str:
    ...


def handle(filetype: str, schema_file: Union[str, Path]):
    schema_path = Path(schema_file)
    if not schema_path.is_absolute():
        schema_path = settings.BASE_DIR / schema_path
    if not schema_path.exists():
        click.echo(click.style('Schema file does not exist.'), err=True)
        return

    schema = json.loads(schema_path.read_text())
    resolver = jsonschema.RefResolver(f'file://{schema_path.parent}', schema)
    DefaultValidatingDraft7Validator(schema, resolver).validate({})

    if filetype == FileTypeEnum.FORM_VUE.value:
        return _form_handle(schema)

    elif filetype == FileTypeEnum.TABLE_VUE.value:
        return _table_handle(schema)
