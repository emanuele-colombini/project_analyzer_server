from projects.projects_data import ProjectModel
from business_requests.br_data import BusinessRequestModel
from business_requests.br_evaluator.crew import create_br_evaluator_crew
from utils import sanitize_folder_name


class BusinessRequestEvaluator():

    def __init__(self):
        self.evaluator_crew = None
    
    def evaluate(self, project: ProjectModel, business_request: BusinessRequestModel, content: str):

        project_name = sanitize_folder_name(project.name)

        self.evaluator_crew = create_br_evaluator_crew(project_name=project_name)

        result = self.evaluator_crew.kickoff(inputs={
            "business_request": content
        })
        return result.pydantic


br_evaluator = BusinessRequestEvaluator()