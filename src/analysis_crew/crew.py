from crewai import Crew, Process

from pydantic import BaseModel

from analysis_crew.team.business_analyst import (
    create_business_analyst,
    create_functional_analysis_task,
    create_functional_analysis_final_task
)
from analysis_crew.team.product_owner import (
    create_product_owner,
    create_functional_analysis_review_task,
    create_architectural_assessment_review_task,
    create_technical_analysis_review_task,
)
from analysis_crew.team.software_architect import (
    create_software_architect,
    create_architectural_assessment_task,
    create_technical_analysis_task,
    create_architectural_assessment_final_task,
    create_technical_analysis_final_task
)
from llms import ollama__memory_embedder


class AnalysisModel(BaseModel):
    functional_analysis: str
    technical_analysis: str
    architectural_assessment: str


def _create_analysis_crew(
        output_file_path: str
) -> Crew:

    # Agents
    business_analyst = create_business_analyst()
    software_architect = create_software_architect()
    product_owner = create_product_owner()

    # Task
    functional_analysis_task = create_functional_analysis_task(
        agent=business_analyst,
        output_file_path=f'{output_file_path}__functional_analysis.md'
    )
    architectural_assessment_task = create_architectural_assessment_task(
        agent=software_architect,
        output_file_path=f'{output_file_path}__architectural_assessment.md',
        context=[functional_analysis_task]
    )
    technical_analysis_task = create_technical_analysis_task(
        agent=software_architect,
        output_file_path=f'{output_file_path}__technical_analysis.md',
        context=[functional_analysis_task, architectural_assessment_task]
    )
    product_owner__functional_analysis_review_task = create_functional_analysis_review_task(
        agent=product_owner,
        output_file_path=f'{output_file_path}__functional_analysis_review.md',
        context=[functional_analysis_task]
    )
    product_owner__architectural_assessment_review_task = create_architectural_assessment_review_task(
        agent=product_owner,
        output_file_path=f'{output_file_path}__architectural_assessment_review.md',
        context=[architectural_assessment_task]
    )
    product_owner__technical_analysis_review_task = create_technical_analysis_review_task(
        agent=product_owner,
        output_file_path=f'{output_file_path}__technical_analysis_review.md',
        context=[technical_analysis_task]
    )
    functional_analysis_final_task = create_functional_analysis_final_task(
        agent=business_analyst,
        output_file_path=f'{output_file_path}__functional_analysis_final.md',
        context=[functional_analysis_task, product_owner__functional_analysis_review_task]
    )
    architectural_assessment_final_task = create_architectural_assessment_final_task(
        agent=software_architect,
        output_file_path=f'{output_file_path}__architectural_assessment_final.md',
        context=[architectural_assessment_task, product_owner__architectural_assessment_review_task]
    )
    technical_analysis_final_task = create_technical_analysis_final_task(
        agent=software_architect,
        output_file_path=f'{output_file_path}__technical_analysis_final.md',
        context=[technical_analysis_task, product_owner__technical_analysis_review_task]
    )

    # Crew
    crew = Crew(
        agents=[
            product_owner,
            business_analyst,
            software_architect
        ],
        tasks=[
            functional_analysis_task,
            architectural_assessment_task,
            technical_analysis_task,
            product_owner__functional_analysis_review_task,
            product_owner__architectural_assessment_review_task,
            product_owner__technical_analysis_review_task,
            functional_analysis_final_task,
            architectural_assessment_final_task,
            technical_analysis_final_task
        ],
        verbose=True,
        memory=True,
        embedder=ollama__memory_embedder,
        process=Process.sequential,
        # process=Process.hierarchical,
        # manager_llm=llm,
        # planning=True,
        # planning_llm=llm
    )
    return crew


def generate_analysis(br_content: str, output_file_path: str):

    crew = _create_analysis_crew(output_file_path)

    # Run the crew
    crew.kickoff(inputs={
        "requirements": br_content
    })

    return AnalysisModel(
        functional_analysis='',
        architectural_assessment='',
        technical_analysis=''
    )