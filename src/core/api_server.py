from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from projects.projects_endpoint import router as projects_router
from business_requests.br_endpoint import router as br_router
from functional_analysis.ba_endpoint import router as ba_router
from architecture.arch_endpoint import router as arch_router


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
        self.app.include_router(ba_router, tags=["Functional Analysis"])
        self.app.include_router(ba_router, tags=["Functional Analysis"])
        self.app.include_router(arch_router, tags=["Architecture"])

    @staticmethod
    def build() -> 'ApiServer':
        server = ApiServer()
        server.__initialize()
        return server


api_server: ApiServer = ApiServer.build()