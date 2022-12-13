
import array
import datetime
import time

from sqlalchemy import create_engine, text
from src.modules.project.domain.repositories import ProjectRepository, ProjectOwnerRepository
from src.modules.project.domain.entities import Project
from src.modules.project.application.dtos import ProjectDTO

engine = create_engine('mysql://organizer-auth:password@organizer-auth-db/organizer_auth')
connection = engine.connect()


class MysqlProjectRepository(ProjectRepository):
    """Project repository implementation"""
    def get_all(self) -> array:
        raw_result = connection.execute(
            text(
                'select * from projects'
            )
        )

        result = []

        for row in raw_result:
            project = ProjectDTO(row[0], row[1], row[2])
            result.append(project)

        return result

    def store(self, project: Project) -> None:
        connection.execute(
            text(
                'insert into projects (id, name, created_at) values (:id, :name, NOW())'
            ),
            {
                'id': str(project.get_id().value),
                'name': project.get_name()
            }
        )
