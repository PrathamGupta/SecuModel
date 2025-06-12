#!/usr/bin/env python3
"""
SecuModel - Simple Threat Modeling Tool
Basic demonstration of core functionality
"""

from src.models.component import Component, ComponentType
from src.models.threat import Threat, ThreatCategory, Severity

def main():
    print("SecuModel - Threat Modeling Tool")
    print("=" * 40)
    
    # Create a simple component
    web_server = Component(
        id="web_01",
        type=ComponentType.PROCESS,
        name="Web Server",
        description="Apache web server handling user requests"
    )
    
    # Create a basic threat
    threat = Threat(
        id="threat_01",
        title="SQL Injection",
        description="Attacker may inject malicious SQL code",
        category=ThreatCategory.T,  # Tampering
        severity=Severity.HIGH,
        affected_elements=[web_server.id]
    )
    
    web_server.threats.append(threat)
    
    # Display results
    print(f"Component: {web_server.name}")
    print(f"Type: {web_server.type.value}")
    print(f"Description: {web_server.description}")
    print(f"\nIdentified Threats:")
    for threat in web_server.threats:
        print(f"  - {threat.title} ({threat.severity.value})")
        print(f"    {threat.description}")
    
    print(f"\nSecuModel basic functionality working!")

if __name__ == "__main__":
    main()

