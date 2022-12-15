"""create user table

Revision ID: d691f0fe61e3
Revises: 799f820f728e
Create Date: 2022-12-15 08:21:52.385789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd691f0fe61e3'
down_revision = '799f820f728e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.VARCHAR(255), primary_key=True),
        sa.Column('login', sa.VARCHAR(255), nullable=False),
        sa.Column('email', sa.VARCHAR(255), nullable=False),
        sa.Column('password', sa.VARCHAR(255), nullable=False),
        sa.Column('salt', sa.VARCHAR(255), nullable=False),
        sa.Column('status', sa.Enum('active', 'disabled', 'banned')),
        sa.Column('created_at', sa.DATETIME(), default='now')
    )


def downgrade() -> None:
    op.drop_table('users')
