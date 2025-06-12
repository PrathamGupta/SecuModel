from dataclasses import dataclass, field
from typing import List, Optional
from enum import Enum

class ThreatCategory(Enum):
    S = 'S'  # Spoofing
    T = 'T'  # Tampering
    R = 'R'  # Repudiation
    I = 'I'  # Information Disclosure
    D = 'D'  # Denial of Service
    E = 'E'  # Elevation of Privilege

class Severity(Enum):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'

class ThreatStatus(Enum):
    IDENTIFIED = 'IDENTIFIED'
    MITIGATED = 'MITIGATED'
    ACCEPTED = 'ACCEPTED'

@dataclass
class Threat:
    id: str
    title: str
    description: str
    category: ThreatCategory
    severity: Severity
    status: ThreatStatus = ThreatStatus.IDENTIFIED
    affected_elements: List[str] = field(default_factory=list)

