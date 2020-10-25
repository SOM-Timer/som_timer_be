"""empty message

Revision ID: f27b8369934e
Revises: 
Create Date: 2020-10-25 13:28:03.446322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f27b8369934e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('category', sa.Enum('Movement', 'Meditation', 'Somatic', name='exercise_category'), server_default='Somatic', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('timers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('work_interval', sa.String(), nullable=True),
    sa.Column('rest_interval', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timers')
    op.drop_table('exercises')
    # ### end Alembic commands ###
