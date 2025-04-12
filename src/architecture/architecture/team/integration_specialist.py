from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_integration_specialist():
    integration_specialist = Agent(
        role="Integration Specialist",
        goal="Design robust integration patterns for system components",
        backstory="""
        You are an integration expert with extensive experience in designing communication 
        patterns between system components. You have deep knowledge of API design, messaging 
        patterns, event-driven architectures, and data synchronization strategies. You understand 
        how to create resilient and scalable integration solutions that maintain system integrity 
        while allowing for flexibility and future growth.
        """,
        allow_delegation=True,
        verbose=True,
        llm=global_llm
    )
    return integration_specialist


def create_design_integration_patterns_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    design_integration_patterns_task = Task(
        description="""
        Design the integration patterns for communication between system components based on 
        the architectural approach and component design.
        
        Your integration design should address:
        1. Communication Patterns - Synchronous vs asynchronous, request/response vs event-driven
        2. API Design - REST, GraphQL, gRPC, or other approaches as appropriate
        3. Message Exchange - Formats, protocols, and standards
        4. Event Management - Event structure, routing, and handling
        5. Error Handling - Retry policies, circuit breakers, fallback mechanisms
        6. Data Consistency - Strategies for maintaining consistency across components
        
        Provide specific recommendations for each integration point identified in the component design.
        Format your response in professional markdown structure.
        """,
        expected_output="Comprehensive integration pattern design",
        output_file=output_file_path,
        context=context,
        agent=agent
    )
    return design_integration_patterns_task
