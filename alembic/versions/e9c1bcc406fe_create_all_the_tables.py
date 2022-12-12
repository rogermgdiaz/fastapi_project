"""Create All The tables

Revision ID: e9c1bcc406fe
Revises: a10eed937dec
Create Date: 2022-12-12 15:26:00.745918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9c1bcc406fe'
down_revision = 'a10eed937dec'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
        sa.Column('id',sa.Integer(),nullable=False),
        sa.Column('email',sa.String(),nullable=False),
        sa.Column('password',sa.Integer(),nullable=False),
        sa.Column('created_at',sa.Integer(),nullable=False))

def downgrade():
    op.drop_table('users')
