from crewai import Crew, Process

from pydantic import BaseModel

from src.teams.business_analyst import (
    create_business_analyst,
    create_functional_analysis_task,
    create_functional_analysis_review_task
)
from src.teams.product_owner import (
    create_product_owner,
    create_product_owner__functional_analysis_review_task,
    create_product_owner__architectural_assessment_review_task,
    create_product_owner__technical_analysis_review_task
)
from src.teams.software_architect import (
    create_software_architect,
    create_architectural_assessment_task,
    create_technical_analysis_task,
    create_architectural_assessment_review_task,
    create_technical_analysis_review_task
)
from src.llms import ollama__memory_embedder


class AnalysisModel(BaseModel):
    functional_analysis: str
    technical_analysis: str
    architecture_assessment: str


class AnalysisCrew:
    def __init__(self):
        pass

    def generate_analysis(self, requirements):

        # Agents
        business_analyst = create_business_analyst()
        software_architect = create_software_architect()
        product_owner = create_product_owner()

        # Task
        functional_analysis_task = create_functional_analysis_task(
            business_analyst
        )
        architectural_assessment_task = create_architectural_assessment_task(
            software_architect,
            functional_analysis_task
        )
        technical_analysis_task = create_technical_analysis_task(
            software_architect,
            functional_analysis_task,
            architectural_assessment_task
        )
        product_owner__functional_analysis_review_task = create_product_owner__functional_analysis_review_task(
            product_owner,
            functional_analysis_task
        )
        product_owner__architectural_assessment_review_task = create_product_owner__architectural_assessment_review_task(
            product_owner,
            architectural_assessment_task
        )
        product_owner__technical_analysis_review_task = create_product_owner__technical_analysis_review_task(
            product_owner,
            technical_analysis_task
        )
        functional_analysis_review_task = create_functional_analysis_review_task(
            business_analyst,
            functional_analysis_task,
            product_owner__functional_analysis_review_task
        )
        architectural_assessment_review_task = create_architectural_assessment_review_task(
            software_architect,
            architectural_assessment_task,
            product_owner__architectural_assessment_review_task
        )
        technical_analysis_review_task = create_technical_analysis_review_task(
            software_architect,
            technical_analysis_task,
            product_owner__technical_analysis_review_task
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
                functional_analysis_review_task,
                architectural_assessment_review_task,
                technical_analysis_review_task
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

        # Run the crew
        crew.kickoff(inputs={"requirements": requirements})

        # Read the output files
        # functional_analysis_path = 'output/functional_analysis.md'
        # architectural_assessment_path = 'output/architectural_assessment.md'
        # technical_analysis_path = 'output/technical_analysis.md'

        # Read functional analysis content
        # with open(functional_analysis_path, 'r', encoding='utf-8') as f:
        #     functional_analysis_content = f.read()

        # Read architectural_assessment
        # with open(architectural_assessment_path, 'r', encoding='utf-8') as f:
        #     architectural_assessment = f.read()

        # Read technical analysis content
        # with open(technical_analysis_path, 'r', encoding='utf-8') as f:
        #     technical_analysis_content = f.read()

        # Create and return the AnalysisModel
        # result = AnalysisModel(
        #     functional_analysis=functional_analysis_content,
        #     technical_analysis=technical_analysis_content,
        #     architectural_assessment=architectural_assessment
        # )

        # return result

    def read_analysis(self):
        try:
            # Read the output files
            functional_analysis_path = 'output/functional_analysis_reviewed.md'
            technical_analysis_path = 'output/technical_analysis_reviewed.md'
            architecture_assessment_path = 'output/architectural_assessment_reviewed.md'

            # Read functional analysis content
            with open(functional_analysis_path, 'r', encoding='utf-8') as f:
                functional_analysis_content = f.read()

            # Read technical analysis content
            with open(technical_analysis_path, 'r', encoding='utf-8') as f:
                technical_analysis_content = f.read()

            # Read architecture analysis content
            with open(architecture_assessment_path, 'r', encoding='utf-8') as f:
                architecture_assessment_content = f.read()

            # Create and return the AnalysisModel
            result = AnalysisModel(
                functional_analysis=functional_analysis_content,
                technical_analysis=technical_analysis_content,
                architecture_assessment=architecture_assessment_content
            )

            return result
        except FileNotFoundError as fef:
            print(f"Errore: Il file {fef.filename} non è stato trovato.")
            return None
        except Exception as e:
            print(f"Errore durante la lettura del file: {e}")
            return None