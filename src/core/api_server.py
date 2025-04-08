from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.projects.projects_endpoint import router as projects_router
from src.business_requests.br_endpoint import router as br_router


class ApiServer:

    def __init__(self):
        self.app = None

    def __initialize(self):
        self.app = FastAPI()
        
        # Configure CORS middleware
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allows all origins
            allow_credentials=True,
            allow_methods=["*"],  # Allows all methods
            allow_headers=["*"],  # Allows all headers
        )
        
        self.app.include_router(projects_router, tags=["Projects"])
        self.app.include_router(br_router, tags=["Business Requests"])

    @staticmethod
    def build() -> 'ApiServer':
        server = ApiServer()
        server.__initialize()
        return server


api_server: ApiServer = ApiServer.build()