from curses import raw
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import re
import semantic_version as sv

VAULT_CURRENT_VERSION = "1.10.0"

env = Environment(loader=FileSystemLoader("templates"), autoescape=select_autoescape())

diag_data = ""

with open("Results.json") as f:
    diag_data = json.load(f)

vault_version_raw = diag_data["vault"]["vault version"]["result"]
vault_version_error = diag_data["vault"]["vault version"]["error"]

vault_version_in_spec = False
vault_version = vault_version_raw
extra_parameters = ""

vault_version_parseable = False

vault_version_search = re.search(
    r"(?P<version>v[0-9]+.[0-9]+.[0-9]+)+(?P<extra>.*)", vault_version_raw
)

try:
    vault_version = vault_version_search[1]
    extra_parameters = vault_version_search[2]
    minimum_vault_version = sv.Version(VAULT_CURRENT_VERSION)
    minimum_vault_version.minor -= 2
    vault_version_in_spec = sv.Version(vault_version[1:]) in sv.SimpleSpec(
        f">={minimum_vault_version}"
    )
except (AttributeError, TypeError):
    pass
else:
    vault_version_parseable = True

template = env.get_template("vault_version.jinja2")
rendered = template.render(
    version=vault_version,
    extra_parameters=extra_parameters,
    in_spec=vault_version_in_spec,
    error=vault_version_error,
)

print(f"{vault_version} {VAULT_CURRENT_VERSION} {vault_version_in_spec}")

with open("build/simple_page.html", "w") as f:
    f.write(rendered)
