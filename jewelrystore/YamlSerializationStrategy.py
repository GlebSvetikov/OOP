import yaml
from typing import List, Any, TextIO
from .AbstractSerializationStrategy import AbstractSerializationStrategy

class YamlSerializationStrategy(AbstractSerializationStrategy):
    def read_data(self, file: TextIO) -> List[dict]:
        """Read data from YAML file."""
        return yaml.safe_load(file) or []

    def write_data(self, file: TextIO, data: List[dict]) -> None:
        """Write data to YAML file."""
        yaml.dump(data, file, default_flow_style=False)