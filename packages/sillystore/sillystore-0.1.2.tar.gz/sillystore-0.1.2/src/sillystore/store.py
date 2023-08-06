import json
import os
from datetime import datetime
from pathlib import Path

_FILESTORE_VARIABLE = "CHRIS-SILLY-SECRETMANAGER"
_DEFAULT_STORE = Path.home() / '.config' / 'sillystore.json'


class BasicStore:

    def __init__(self, file_store=None):
        if file_store:
            self.file_store = Path(file_store)
        else:
            self.file_store = Path(os.environ.get(_FILESTORE_VARIABLE, _DEFAULT_STORE))
        if self.file_store.exists():
            with self.file_store.open("r") as f:
                res = f.read()
                self.store = json.loads(res) if res else {}
        else:
            self.store = {}

    def secrets(self, tag=None):
        if tag:
            return [k for k, t, _ in self if tag in t]
        return list(self.store.keys())

    def save(self):
        with self.file_store.open("w") as f:
            res = json.dumps(self.store)
            f.write(res)

    def get_date(self):
        return datetime.utcnow().isoformat()

    def tag(self, key, to_add=None, to_remove=None):
        tags = set(self.store[key]["tags"])
        if to_add:
            tags.update(to_add)
        if to_remove:
            tags -= set(to_remove)
        self.store[key]["tags"] = list(tags)
        self.store[key]["lastupdate"] = self.get_date()

    def update_value(self, key, value):
        if not key in self.store.keys():
            self.store[key] = {"value": {}, "tags": [], "lastupdate": ""}
        self.store[key]["value"] = value
        self.store[key]["lastupdate"] = self.get_date()

    def get_value(self, key, def_value=None):
        res = self.store.get(key, None)
        if res:
            return res["value"]
        return def_value

    def __iter__(self):
        for k, v in self.store.items():
            yield k, v["tags"], v['value']

    def __delitem__(self, key):
        del self.store[key]

    def __getitem__(self, key):
        return self.store[key]["value"]

    def __setitem__(self, key, value):
        self.update_value(key, value)
        return self


def default_store():
    return BasicStore()
