"""empty message

Revision ID: f6f229271809
Revises: 4a855fbde8fa
Create Date: 2020-11-01 16:07:31.255049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6f229271809'
down_revision = '4a855fbde8fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rest_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('init_mood', sa.Integer(), nullable=True),
    sa.Column('end_mood', sa.Integer(), nullable=True),
    sa.Column('timer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['timer_id'], ['timers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('work_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('init_mood', sa.Integer(), nullable=True),
    sa.Column('end_mood', sa.Integer(), nullable=True),
    sa.Column('timer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['timer_id'], ['timers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work_sessions')
    op.drop_table('rest_sessions')
    # ### end Alembic commands ###