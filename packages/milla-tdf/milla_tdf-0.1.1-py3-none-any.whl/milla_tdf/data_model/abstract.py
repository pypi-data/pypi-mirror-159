from dataclasses import dataclass,field
from typing import Optional

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class AbstractDataModel:
    pass

@dataclass_json
@dataclass
class AbstractMetaData:
    pass
