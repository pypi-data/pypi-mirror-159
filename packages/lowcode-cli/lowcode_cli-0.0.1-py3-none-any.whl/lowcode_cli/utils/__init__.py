import uuid


def make_uuid_string():
    return str(uuid.uuid4()).replace('-', '')[:8]
