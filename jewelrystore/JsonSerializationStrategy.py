import json
from typing import List, Any, TextIO
from .AbstractSerializationStrategy import AbstractSerializationStrategy

class JsonSerializationStrategy(AbstractSerializationStrategy):
    def read_data(self, file: TextIO) -> List[dict]:
        """Read data from JSON file."""
        return json.load(file)

    def write_data(self, file: TextIO, data: List[dict]) -> None:
        """Write data to JSON file."""
        json.dump(data, file, indent=2)