
import array

from sqlalchemy import create_engine, text
from src.modules.project.domain.repositories import ProjectRepository, ProjectOwnerRepository
from src.modules.project.domain.entities import Project
from src.modules.project.domain.value_objects import ProjectId
from src.modules.project.application.dtos import ProjectDTO

engine = create_engine('mysql://organizer-auth:password@organizer-auth-db/organizer_auth')
connection = engine.connect()


class MysqlProjectRepository(ProjectRepository):
    _TABLE_NAME = 'projects'

    """Project repository implementation"""
    def get_all(self) -> array:
        raw_result = connection.execute(
            text(
                f'select * from {self._TABLE_NAME}'
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
                f'insert into {self._TABLE_NAME} (id, name, created_at) values (:id, :name, NOW())'
            ),
            {
                'id': str(project.get_id().value),
                'name': project.get_name()
            }
        )

    def delete(self, project_id: ProjectId) -> None:
        connection.execute(
            text(
                f'delete from {self._TABLE_NAME} where id = :id'
            ),
            {
                'id': str(project_id.value)
            }
        )

    def update(self, project_id: ProjectId, project_name: str) -> None:
        connection.execute(
            text(
                f'update {self._TABLE_NAME} set name = :name where id = :id'
            ),
            {
                'name': project_name,
                'id': str(project_id.value)
            }
        )
