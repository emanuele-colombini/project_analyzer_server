from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_infrastructure_specialist():
    infrastructure_specialist = Agent(
        role="Infrastructure Specialist",
        goal="Define the optimal infrastructure to support architectural solutions",
        backstory="""
        You are an infrastructure expert with deep knowledge of cloud platforms, on-premises 
        solutions, and hybrid environments. You understand scaling requirements, high availability 
        patterns, disaster recovery strategies, and security best practices. You can recommend 
        the right infrastructure components to support various architectural designs while 
        considering performance, reliability, and cost.
        """,
        allow_delegation=True,
        verbose=True,
        llm=global_llm
    )
    return infrastructure_specialist


def create_infrastructure_recommendations_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    infrastructure_recommendations_task = Task(
        description="""
        Propose the optimal infrastructure to support the architectural solution and its components.

        Your infrastructure recommendations should include:
        1. Deployment Environment - Cloud, on-premises, or hybrid with specific platforms
        2. Compute Resources - Server types, containerization, serverless options
        3. Storage Solutions - Databases, file storage, caching mechanisms
        4. Network Configuration - API gateways, load balancers, service mesh
        5. Scaling Strategy - Horizontal vs vertical, auto-scaling policies
        6. Monitoring & Observability - Logging, metrics, tracing approaches
        7. Disaster Recovery - Backup strategies, recovery point/time objectives

        Consider performance, reliability, cost, and operational complexity in your recommendations.
        Format your response in professional markdown structure.
        """,
        expected_output="Detailed infrastructure recommendations aligned with the architecture",
        output_file=output_file_path,
        context=context,
        agent=agent
    )
    return infrastructure_recommendations_task
