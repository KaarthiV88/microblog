"""add columns to project

Revision ID: 0e0171e7f4c0
Revises: 8b1aacf62d17
Create Date: 2020-06-23 19:28:12.795053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e0171e7f4c0'
down_revision = '8b1aacf62d17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('completion', sa.Numeric(), nullable=True))
    op.add_column('project', sa.Column('cost', sa.Numeric(), nullable=True))
    op.add_column('project', sa.Column('hyperlinks', sa.String(), nullable=True))
    op.add_column('project', sa.Column('image_filepath', sa.String(), nullable=True))
    op.add_column('project', sa.Column('name', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'name')
    op.drop_column('project', 'image_filepath')
    op.drop_column('project', 'hyperlinks')
    op.drop_column('project', 'cost')
    op.drop_column('project', 'completion')
    # ### end Alembic commands ###
