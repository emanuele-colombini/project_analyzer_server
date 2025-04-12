from typing import List

from crewai import Agent, Task

from llms import global_llm


def create_domain_expert():
    domain_expert = Agent(
        role="Domain Expert",
        goal="Provide industry context and domain-specific insights",
        backstory="""
        You have deep expertise across multiple business domains including finance, healthcare, 
        retail, manufacturing, and technology. You understand industry standards, compliance 
        requirements, and best practices that help ensure functional specifications are 
        realistic and aligned with industry norms.
        """,
        allow_delegation=True,
        verbose=True,
        max_iter=10,
        llm=global_llm
    )
    return domain_expert


def create_domain_context_task(
        agent: Agent,
        output_file_path: str,
        context: List[Task]
):
    domain_context_task = Task(
        description="""
        Review the business request and provide industry-specific context that would be relevant 
        for creating functional specifications.

        Your domain context should include:
        1. Industry Standards - Relevant frameworks, methodologies, or best practices
        2. Regulatory Considerations - Any compliance issues that might impact the solution
        3. Common Challenges - Typical pitfalls or obstacles in this domain
        4. Integration Points - Standard systems that typically connect in this context
        5. Success Metrics - How solutions of this type are typically measured

        Format your response in markdown.
        
        ---
        
        Business request: 
        {business_request}
        """,
        expected_output="Domain-specific context and considerations",
        output_file=output_file_path,
        context=context,
        agent=agent
    )

    return domain_context_task
