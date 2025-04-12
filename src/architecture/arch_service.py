from sqlalchemy.ext.asyncio import AsyncSession

from architecture.architecture.crew import generate_architecture_analysis, ArchitectureCrewConfig
from business_requests.br_service import br_service
from functional_analysis.ba_service import ba_service
from projects.projects_service import projects_service


class ArchitectureService:

    async def get_architecture_crew_config(self, session: AsyncSession, br_id: str):

        br = await br_service.get_version_by_id(session, br_id)
        if not br:
            return None

        prj = await projects_service.get_project_by_id(session, br.project_id)
        if not prj:
            return None

        br_content = await br_service.get_file_content(session, br_id)
        if not br_content:
            return None

        architecture_output_path = f"{prj.project_folder}/output/br_v{br.version}/architecture/"

        # Output files for architecture analysis
        architecture_approach = f'{architecture_output_path}/architecture_approach.md'
        core_components = f'{architecture_output_path}/core_components.md'
        integration_pattern = f'{architecture_output_path}/integration_pattern.md'
        infrastructure_recommendations = f'{architecture_output_path}/infrastructure_recommendations.md'
        security_architecture = f'{architecture_output_path}/security_architecture.md'
        architecture_document = f'{architecture_output_path}/architecture_document.md'

        return ArchitectureCrewConfig(
            br_version=br.version,
            br_content=br_content,
            architecture_output_path=architecture_output_path,
            output_files={
                'architecture_approach': architecture_approach,
                'core_components': core_components,
                'integration_pattern': integration_pattern,
                'infrastructure_recommendations': infrastructure_recommendations,
                'security_architecture': security_architecture,
                'architecture_document': architecture_document 
            }
        )


    async def create_architecture_analysis(self, session: AsyncSession, br_id: str):

        func_config = await ba_service.get_functional_crew_config(session, br_id)
        if not func_config:
            return None
        
        arch_config = await self.get_architecture_crew_config(session, br_id)
        if not arch_config:
            return None
        
        generate_architecture_analysis(arch_config, func_config)


arch_service = ArchitectureService()