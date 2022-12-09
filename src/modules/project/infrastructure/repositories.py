
import uuid
from sqlalchemy import create_engine, text
from src.modules.project.domain.repositories import ProjectRepository, ProjectOwnerRepository
from src.modules.project.domain.value_objects import ProjectId, ProjectOwnerId
from src.modules.project.domain.entities import Project

engine = create_engine('mysql://organizer-auth:password@organizer-auth-db/organizer_auth')
connection = engine.connect()


class MysqlProjectRepository(ProjectRepository):
    """User repository implementation"""
    def get_all(self):
        raw_result = connection.execute(text('select * from projects'))
        result = []

        for row in raw_result:
            pi = ProjectId.from_string(row[0])
            pn = row[1]
            poi = ProjectOwnerId.from_string(row[0])

            project = Project(pi, pn, poi)
            print(project)

        return result
