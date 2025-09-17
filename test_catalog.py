from kedro.io import DataCatalog
from kedro.config import ConfigLoader
from pathlib import Path

conf_paths = [Path.cwd() / "conf"]
conf_loader = ConfigLoader(conf_paths)

catalog = DataCatalog.from_config(conf_loader.get("base/catalog*"))

print(list(catalog.datasets.keys()))
