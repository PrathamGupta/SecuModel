from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum

class ComponentType(Enum):
    PROCESS = 'process'
    DATASTORE = 'datastore'
    EXTERNAL = 'external'
    ACTOR = 'actor'

@dataclass
class Component:
    id: str
    type: ComponentType
    name: str
    description: Optional[str] = None
    position: Optional[Dict[str, int]] = field(default_factory=dict)
    properties: Dict[str, str] = field(default_factory=dict)
    threats: List['Threat'] = field(default_factory=list)
    
    def __post_init__(self):
        if isinstance(self.type, str):
            self.type = ComponentType(self.type)

