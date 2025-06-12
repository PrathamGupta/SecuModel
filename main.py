#!/usr/bin/env python3
from src.models.component import Component, ComponentType
from src.engines.threat_engine import ThreatEngine

def main():
    print("SecuModel - Automated Threat Detection")
    print("=" * 45)
    
    # Create threat engine
    engine = ThreatEngine()
    
    # Create components
    components = [
        Component(id="web_01", type=ComponentType.PROCESS, name="Web Server"),
        Component(id="db_01", type=ComponentType.DATASTORE, name="User Database"),
        Component(id="api_01", type=ComponentType.PROCESS, name="API Gateway")
    ]
    
    # Analyze each component
    for component in components:
        threats = engine.analyze_component(component)
        component.threats = threats
        
        print(f"\n{component.name} ({component.type.value})")
        if threats:
            print(" Threats detected:")
            for threat in threats:
                print(f"    • {threat.title} [{threat.severity.value}]")
        else:
            print("No threats detected")
    
    total_threats = sum(len(c.threats) for c in components)
    print(f"\nAnalysis complete: {total_threats} threats identified across {len(components)} components")

if __name__ == "__main__":
    main()

