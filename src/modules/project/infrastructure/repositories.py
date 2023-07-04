
import array

from sqlalchemy import create_engine, text
from src.modules.project.domain.repositories import ProjectRepository, ProjectWebhookRepository
from src.modules.project.domain.entities import Project, ProjectWebhook
from src.modules.project.domain.value_objects import ProjectId, ProjectWebhookType, ProjectWebhookId, ProjectWebhookUrl
from src.modules.project.application.dtos import ProjectDTO

engine = create_engine('mysql://organizer-auth:password@organizer-auth-db/organizer_auth')
connection = engine.connect()


class MysqlProjectRepository(ProjectRepository):
    """Project repository implementation"""
    _TABLE_NAME = 'projects'

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

    def exists_by_id(self, project_id: ProjectId) -> bool:
        result = connection.execute(
            text(
                f'select count(*) as count from {self._TABLE_NAME} where id = :project_id'
            ),
            {
                'project_id': project_id.value
            }
        ).fetchone()

        return result.count > 0


class MysqlProjectWebhookRepository(ProjectWebhookRepository):
    _TABLE_NAME = 'project_webhooks'

    def store(self, webhook: ProjectWebhook) -> None:
        connection.execute(
            text(
                f'insert into {self._TABLE_NAME} (id, project_id, type, url, active) '
                f'values (:id, :project_id, :type, :url, :active)'
            ),
            {
                'id': webhook.get_id().value,
                'project_id': webhook.get_project_id().value,
                'type': webhook.get_type().name,
                'url': webhook.get_url().get_value(),
                'active': webhook.get_active()
            }
        )

    def get_by_project_id_and_type(self, project_id: ProjectId, webhook_type: ProjectWebhookType) -> ProjectWebhook:
        raw_data = connection.execute(
            text(
                f'select id, project_id, type, url, active from {self._TABLE_NAME} '
                f'where project_id = :project_id and type = :type'
            ),
            {
                'project_id': project_id.value,
                'type': webhook_type.name
            }
        ).fetchone()

        return ProjectWebhook.reproduce(
            ProjectWebhookId.from_string(raw_data.id),
            ProjectId.from_string(raw_data.project_id),
            ProjectWebhookType[raw_data.type],
            ProjectWebhookUrl(raw_data.url),
            raw_data.active
        )
