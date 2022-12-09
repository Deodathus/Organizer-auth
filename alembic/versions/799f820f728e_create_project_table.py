"""create project table

Revision ID: 799f820f728e
Revises: 
Create Date: 2022-12-09 14:56:30.052390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '799f820f728e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'projects',
        sa.Column('id', sa.VARCHAR(255), primary_key=True),
        sa.Column('name', sa.VARCHAR(255), nullable=False),
        sa.Column('created_at', sa.DATETIME(), default='now')
    )


def downgrade() -> None:
    op.drop_table('projects')
