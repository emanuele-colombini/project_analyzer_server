from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_solution_architect():
    solution_architect = Agent(
        role="Solution Architect",
        goal="Design comprehensive architectural solutions based on functional requirements",
        backstory="""
        You are a seasoned solution architect with over 20 years of experience designing 
        enterprise-grade systems. You have expertise in both monolithic and microservice 
        architectures across various industries. You excel at analyzing business and 
        functional requirements to recommend the most appropriate architectural approach.
        You understand the trade-offs between different architectural styles and can justify 
        your decisions with clear reasoning.
        """,
        allow_delegation=True,
        verbose=True,
        llm=global_llm
    )
    return solution_architect


def create_architecture_approach_task(
        agent: Agent,
        output_file_path: str
):
    architecture_approach_task = Task(
        description="""
        Review the business request, initial analysis, domain context, and functional specifications 
        to determine the most appropriate architectural approach (monolithic vs microservices).

        Your assessment should include:
        1. Architectural Decision - Whether a monolithic or microservice architecture is recommended
        2. Decision Rationale - Detailed explanation of why this approach is best for this situation
        3. Key Drivers - Business or technical factors that influenced the decision
        4. Trade-offs - Advantages and disadvantages of the chosen approach for this specific case
        5. Future Considerations - How the architecture might evolve over time

        Use specific examples from the provided inputs to support your decision.
        Format your response in professional markdown structure.
        
        ---

        Business request: 
        {business_request}
        
        ---
        
        Initial analysis: 
        {initial_analysis}
        
        ---
        
        Domain context: 
        {domain_context}
        
        ---
        
        Functional specifications: 
        {functional_specs}
        """,
        expected_output="A detailed architectural approach recommendation with justification",
        output_file=output_file_path,
        agent=agent
    )
    return architecture_approach_task


def create_design_core_components_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    design_core_components_task = Task(
        description="""
        Based on the architectural approach and functional specifications, design the core 
        components of the solution.

        If a monolithic approach was selected:
        1. Design the modular components within the monolith
        2. Define component responsibilities and boundaries
        3. Describe internal communication patterns
        4. Identify shared services and utilities

        If a microservice approach was selected:
        1. Identify each microservice and its responsibility
        2. Define service boundaries and data ownership
        3. Determine appropriate sizing of services
        4. Address data consistency challenges

        For either approach, include:
        - Component/service naming
        - Primary functions
        - Data managed by each component
        - Dependencies between components

        Create a logical diagram description of the components and their relationships.
        Format your response in professional markdown structure.
        
        ---
        
        Functional specifications: 
        {functional_specs}
        """,
        expected_output="Detailed component design aligned with the architectural approach",
        output_file=output_file_path,
        context=context,
        agent=agent
    )
    return design_core_components_task


def create_final_architecture_document_task(agent: Agent, output_file_path: str, context: List[Task]):
    return Task(
        description="""
        Compile a comprehensive architecture document that integrates all previous analyses and designs.

        Your architecture document should include:
        1. Executive Summary - Brief overview of the architectural solution
        2. Architectural Vision - Goals and principles guiding the design
        3. Solution Overview - High-level description of the complete solution
            - Include whether it's monolithic or microservice-based and why
        4. Detailed Architecture
            - For monolithic: Component breakdown, responsibilities, and interactions
            - For microservices: Service definitions, boundaries, and communications
        5. Integration Architecture - How components/services communicate
        6. Infrastructure Architecture - Deployment model and environments
        7. Security Architecture - Security controls and considerations
        8. Quality Attributes - How the architecture addresses performance, scalability, reliability
        9. Implementation Roadmap - Phased approach to building the solution
        10. Architecture Decision Records - Key decisions and their rationale

        Create a cohesive document that tells the complete architectural story.
        Format your document using professional markdown structure with clear sections and subsections.
        
        To create the document, use the following inputs:
    
        
        Business request: {business_request}
        Functional specifications: {functional_specs}
        
        """,
        expected_output="Comprehensive architectural solution document",
        output_file=output_file_path,
        context=context,
        agent=agent
    )