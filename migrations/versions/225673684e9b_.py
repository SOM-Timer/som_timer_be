"""empty message

Revision ID: 225673684e9b
Revises: 018af8a22d84
Create Date: 2020-11-25 19:35:17.237266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '225673684e9b'
down_revision = '018af8a22d84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uid', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'uid')
    # ### end Alembic commands ###
