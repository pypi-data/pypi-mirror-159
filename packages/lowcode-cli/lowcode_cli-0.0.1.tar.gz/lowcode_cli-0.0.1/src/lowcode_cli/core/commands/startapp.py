from lowcode_cli.utils import template
from lowcode_cli.conf import settings


def handel(app_name: str, app_label: str, output: str = settings.BASE_DIR):
    template_dir = settings.TEMPLATE_DIR / "app"
    variables = {"app_name": app_name, "app_label": app_label}
    template.render_dir(
        app_name=app_name, template_dir=template_dir, output=output, variables=variables
    )
