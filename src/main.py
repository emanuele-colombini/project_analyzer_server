from dotenv import load_dotenv

load_dotenv()

import asyncio
import uvicorn

from core.api_server import api_server
from core.database_manager import database_manager


async def setup():
    await database_manager.setup_entities()


async def main():
    # Core setup
    await setup()

    # Server app
    config = uvicorn.Config(
        api_server.app,
        host="0.0.0.0",
        port=8000,
        loop="asyncio"
    )
    server = uvicorn.Server(config)

    await server.serve()

    # Leggi i requisiti dal file markdown
    # requirements_path = os.path.join(os.path.dirname(__file__), 'input/requirements.md')
    # requirements = read_markdown(requirements_path)
    
    # if not requirements:
    #     print("Impossibile procedere senza requisiti. Verifica che il file requirements.md esista.")
    #     return
    
    # Inizializza l'agente e genera gli epic
    # analysis_crew = AnalysisCrew()
    # analysis_crew.generate_analysis(requirements)

    # functional = read_analysis()

    # design_crew = DesignCrew()
    # design_crew.generate_design(
    #     architectural_assessment=functional.architecture_assessment,
    #     functional_analysis=functional.functional_analysis,
    #     technical_analysis=functional.technical_analysis
    # )

    # functional = read_analysis()
    # epic_crew = EpicCrew()
    # result = epic_crew.generate_epic(functional)

    # BR Evaluator
    # br_evaluator_crew = create_br_evaluator_crew()
    # br_evaluator_crew.kickoff(inputs={"business_request": requirements})

    # responses_path = os.path.join(os.path.dirname(__file__), 'input/responses.md')
    # responses = read_markdown(responses_path)

    # BR Complete
    # br_integrator_crew = create_br_integrator_crew()
    # br_integrator_crew.kickoff(inputs={"business_request": requirements, "client_responses": responses})

    # br_complete_path = os.path.join(os.path.dirname(__file__), 'output/br_complete.md')
    # br_complete = read_markdown(br_complete_path)

    # Functional Analysis
    # functional_analysis_crew = create_functional_analysis_crew()
    # functional_analysis_crew.kickoff(inputs={"business_requirements": br_complete})
    pass


if __name__ == "__main__":
    asyncio.run(main())
