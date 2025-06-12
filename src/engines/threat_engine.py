from typing import List
from ..models.component import Component, ComponentType
from ..models.threat import Threat, ThreatCategory, Severity, ThreatStatus

class ThreatEngine:
    def __init__(self):
        self.rules = []
    
    def analyze_component(self, component: Component) -> List[Threat]:
        """Basic threat analysis for a component"""
        threats = []
        
        # Simple rule: Web servers are vulnerable to injection attacks
        if component.type == ComponentType.PROCESS and 'web' in component.name.lower():
            threats.append(Threat(
                id=f"injection_{component.id}",
                title="Injection Attack",
                description=f"Web component {component.name} may be vulnerable to injection attacks",
                category=ThreatCategory.T,
                severity=Severity.HIGH,
                affected_elements=[component.id]
            ))
        
        # Simple rule: Data stores need access controls
        if component.type == ComponentType.DATASTORE:
            threats.append(Threat(
                id=f"access_control_{component.id}",
                title="Unauthorized Data Access",
                description=f"Data store {component.name} may allow unauthorized access",
                category=ThreatCategory.I,
                severity=Severity.MEDIUM,
                affected_elements=[component.id]
            ))
        
        return threats

