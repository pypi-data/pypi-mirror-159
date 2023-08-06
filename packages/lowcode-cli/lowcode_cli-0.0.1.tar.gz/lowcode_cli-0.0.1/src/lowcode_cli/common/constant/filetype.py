from enum import Enum
from datetime import datetime
from lowcode_cli.conf import settings


class FileTypeEnum(Enum):
    FORM_VUE = 'form.vue'
    TABLE_VUE = 'table.vue'


TypeDefaultValueMap = {
    'string': '',
    'number': 0,
    'date': datetime.now().date().strftime(settings.DATETIME_FORMAT),
    'datetime': datetime.now().strftime(settings.DATETIME_FORMAT),
    'array': [],
    'object': {}
}
