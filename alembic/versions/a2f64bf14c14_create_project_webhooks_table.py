"""create project_webhooks table

Revision ID: a2f64bf14c14
Revises: 6fa635c96e61
Create Date: 2023-07-04 17:03:21.601005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f64bf14c14'
down_revision = '6fa635c96e61'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'project_webhooks',
        sa.Column('id', sa.VARCHAR(255), primary_key=True),
        sa.Column('project_id', sa.VARCHAR(255), nullable=False),
        sa.Column('type', sa.VARCHAR(255), nullable=False),
        sa.Column('url', sa.VARCHAR(255), nullable=False),
        sa.Column('active', sa.Boolean, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('project_webhooks')
