"""create user tokens table

Revision ID: 6fa635c96e61
Revises: d691f0fe61e3
Create Date: 2023-06-15 19:46:40.096374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fa635c96e61'
down_revision = 'd691f0fe61e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user_tokens',
        sa.Column('id', sa.VARCHAR(255), primary_key=True),
        sa.Column('user_id', sa.VARCHAR(255), nullable=False),
        sa.Column('token', sa.VARCHAR(255), nullable=False),
        sa.Column('active', sa.BOOLEAN, nullable=False),
        sa.Column('valid_time', sa.INTEGER, nullable=False),
        sa.Column('created_at', sa.DATETIME, default='now')
    )

    op.create_index('user_id_token_active_idx', 'user_tokens', ['user_id', 'token', 'active'])


def downgrade() -> None:
    op.drop_index('user_id_token_active_idx', 'user_tokens')
    op.drop_table('user_tokens')
