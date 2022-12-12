"""create content column to posts table

Revision ID: a10eed937dec
Revises: e4b0643031c2
Create Date: 2022-12-12 14:56:16.279439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a10eed937dec'
down_revision = 'e4b0643031c2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('title', sa.String(),nullable=False))
    op.add_column('posts',sa.Column('content', sa.String(),nullable=False))

def downgrade() -> None:
    op.drop_column('posts','title')
    op.drop_column('posts','content')