from sqlalchemy.ext.asyncio import AsyncSession

from business_requests.br_service import br_service
from functional_analysis.functional.crew import generate_functional_analysis, FunctionalCrewConfig
from projects.projects_service import projects_service


class BusinessAnalysisService:

    async def get_functional_crew_config(self, session: AsyncSession, br_id: str):
        """
        Asynchronously retrieves the functional crew configuration for a given business requirement (BR) ID.
        This method fetches the BR version, associated project details, and the BR content. It then constructs
        the functional output path and output file paths for functional analysis.
        Args:
            session (AsyncSession): The database session used for querying data.
            br_id (str): The ID of the business requirement.
        Returns:
            FunctionalCrewConfig: An object containing the BR version, BR content, functional output path,
                                  and a dictionary of output file paths for functional analysis.
                                  Returns None if the BR or associated project is not found, or if the BR content
                                  is unavailable.
        """

        br = await br_service.get_version_by_id(session, br_id)
        if not br:
            return None

        prj = await projects_service.get_project_by_id(session, br.project_id)
        if not prj:
            return None

        br_content = await br_service.get_file_content(session, br_id)
        if not br_content:
            return None

        functional_output_path = f"{prj.project_folder}/output/br_v{br.version}/functional/"

        # Output files for functional analysis
        initial_analysis = f'{functional_output_path}/initial_analysis.md'
        domain_context = f'{functional_output_path}/domain_context.md'
        functional_specs = f'{functional_output_path}/functional_specs.md'
        
        return FunctionalCrewConfig(
            br_version=br.version,
            br_content=br_content,
            functional_output_path=functional_output_path,
            output_files={
                'initial_analysis': initial_analysis,
                'domain_context': domain_context,
                'functional_specs': functional_specs
            }
        )

    async def create_functional_analysis(self, session: AsyncSession, br_id: str):
        """
        Creates a functional analysis for the given business requirement ID (br_id).

        This method retrieves the functional crew configuration associated with the 
        provided business requirement ID. If a configuration is found, it generates 
        a functional analysis based on the retrieved configuration.

        Args:
            session (AsyncSession): The database session used to query data.
            br_id (str): The business requirement ID for which the functional analysis 
                         is to be created.

        Returns:
            None: If no configuration is found for the given business requirement ID.
            Otherwise, the functional analysis is generated and no value is returned.
        """

        config = await self.get_functional_crew_config(session, br_id)
        if not config:
            return None

        generate_functional_analysis(config)


ba_service = BusinessAnalysisService()
