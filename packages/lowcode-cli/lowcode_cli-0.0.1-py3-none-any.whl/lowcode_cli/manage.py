import click
from pathlib import Path
from lowcode_cli.common.constant.filetype import FileTypeEnum
from lowcode_cli.core.commands import makemigrations as makemigrations_commands
from lowcode_cli.core.commands import startapp
from lowcode_cli import utils

FILETYPE_CHOICES = [item.value for item in FileTypeEnum] + ['all']


def get_default_version_dir():
    return Path.home() / '.lowcode' / utils.make_uuid_string()


@click.group()
def cli():
    ...


@click.command()
@click.option('--file_type', '-ft', '--file-type', required=True, type=click.Choice(FILETYPE_CHOICES),
              help='Select the file type of generated code.')
@click.option('--version', '-v', default=get_default_version_dir(), type=str, help='Select the migration version.')
@click.option('--schema_file', '-sf', '--schema-file', required=True, type=str, help='Select the jsonschema file path.')
@click.option('--raw/--no-raw', default=False, type=bool, help='Output raw data.')
def makemigrations(file_type: str, schema_file: str, version: str = None, raw: bool = False):
    if not version:
        version = utils.make_uuid_string()
    content = makemigrations_commands.handle(file_type, schema_file)
    if raw:
        click.echo(content)
    else:
        output = Path.cwd() / version / file_type
        if not output.parent.exists():
            output.parent.mkdir(parents=True)
        output.write_text(content)


@click.command()
@click.option('--app_name', type=str, help='App name')
@click.option('--app_label', type=str, help='App label')
@click.option('--output', default=Path.cwd(), type=str, help='App label')
def startapp(app_name: str, app_label: str, output: str = Path.cwd()):
    startapp.handel(app_name, app_label)


cli.add_command(makemigrations)
cli.add_command(startapp)

if __name__ == '__main__':
    cli()
