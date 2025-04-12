from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_business_analyst():
    business_analyst = Agent(
        role="Business Analyst",
        goal="Transform business requests into comprehensive functional specifications",
        backstory="""
        You are a senior business analyst with 15 years of experience across various industries.
        You excel at understanding business needs and transforming them into clear, structured 
        functional specifications. You are methodical, thorough, and have a knack for asking 
        the right questions to uncover hidden requirements.
        """,
        allow_delegation=True,
        verbose=True,
        llm=global_llm,
        tools=[]
    )
    return business_analyst


def create_initial_analysis_task(
        agent: Agent,
        output_file_path: str
):
    functional_analysis_task = Task(
        description="""
        Analyze the given business request thoroughly. Extract and organize the key information 
        into a structured analysis_crew.

        Your analysis_crew should include:
        1. Executive Summary - Brief overview of what is being requested
        2. Business Objectives - The core goals the solution aims to achieve
        3. Stakeholders - Key groups affected by or interested in the solution
        4. Current State Analysis - Assessment of how things work currently
        5. Constraints and Assumptions - Any limitations or prerequisites
        6. Questions for Clarification - Any information that seems missing

        Format your response in a clean, professional structure using markdown.

        ---
        
        Business request: 
        {business_request}
        """,
        expected_output="A comprehensive analysis_crew of the business request",
        output_file=output_file_path,
        agent=agent
    )

    return functional_analysis_task


def create_functional_specs_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    functional_specs_task = Task(
        description="""
        Based on the business request analysis_crew and domain context, develop a comprehensive 
        functional specification document.

        Your functional specification should include:
        1. Purpose and Scope - Clear boundaries of what the solution will and won't do
        2. Functional Requirements - Detailed description of features and capabilities
           - Each requirement should be specific, measurable, and testable
           - Organize by logical modules or components
           - Include user roles and permissions
        3. Data Requirements - What information will be stored and processed
        4. Interface Requirements - How the system will interact with users and other systems
        5. Non-Functional Requirements - Performance, security, usability, etc.
        6. Assumptions and Constraints
        7. Acceptance Criteria - How to determine if requirements are met

        Format your specification using professional markdown structure with clear headings and numbered requirements.
        
        ---
        
        Business request: 
        {business_request}
        """,
        expected_output="A comprehensive functional specification document.",
        output_file=output_file_path,
        context=context,
        agent=agent
    )
    return functional_specs_task
