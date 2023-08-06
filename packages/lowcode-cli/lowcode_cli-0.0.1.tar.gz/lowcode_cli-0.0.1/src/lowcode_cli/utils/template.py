from lowcode_cli.common.jinja2 import env
from pathlib import Path
from typing import Union
from lowcode_cli.conf import settings
import os


def render_dir(app_name: str, template_dir: Union[str, Path], output: Union[str, Path], variables=None):
    """渲染目录"""
    if variables is None:
        variables = {}

    if 'app_name' not in variables:
        variables['app_name'] = app_name
    if 'app_label' not in variables:
        variables['app_label'] = app_name

    template_dir = Path(template_dir)
    output = Path(output) / app_name

    for root, dirs, tpl_files in os.walk(template_dir):
        rootpath = Path(root)
        for tpl_file in tpl_files:
            tpl_name = (rootpath / Path(tpl_file)).relative_to(settings.TEMPLATE_DIR)
            tpl_relpath = (rootpath / Path(tpl_file)).relative_to(template_dir)
            tpl = env.get_template(str(tpl_name))
            content = tpl.render(**variables)
            output_file = output / str(tpl_relpath).replace('.tpl', '')
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(content)
