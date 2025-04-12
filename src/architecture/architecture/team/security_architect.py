from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_security_architect():
    security_architect = Agent(
        role="Security Architect",
        goal="Ensure architectural solutions incorporate robust security measures",
        backstory="""
        You are a security architect with expertise in designing secure systems from the ground up. 
        You understand security principles like defense in depth, least privilege, and secure by design. 
        You can identify security risks in architectural designs and recommend appropriate mitigations. 
        You have experience with identity management, encryption, network security, and compliance 
        requirements across various industries.
        """,
        allow_delegation=True,
        verbose=True,
        llm=global_llm
    )
    return security_architect

def create_design_security_architecture_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    design_security_architecture = Task(
        description="""
        Design a comprehensive security architecture for the solution based on the architectural 
        approach, component design, and infrastructure recommendations.
    
        Your security architecture should address:
        1. Identity and Access Management - Authentication, authorization approaches
        2. Data Protection - Encryption at rest and in transit, sensitive data handling
        3. Network Security - Segmentation, firewalls, intrusion detection
        4. API Security - Rate limiting, input validation, API gateways
        5. Security Monitoring - Audit logging, threat detection
        6. Compliance Requirements - Regulatory considerations based on domain
        7. Security Testing - Approaches to verify security controls
    
        Provide specific security measures for each component and integration point.
        Format your response in professional markdown structure.
        """,
        expected_output="Comprehensive security architecture design",
        output_file=output_file_path,
        context=context,
        agent=agent
    )
    return design_security_architecture
