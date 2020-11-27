"""empty message

Revision ID: 64281b6893a1
Revises: 6b643097f85e
Create Date: 2020-11-27 13:27:08.331242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64281b6893a1'
down_revision = '6b643097f85e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=True))
    op.drop_column('users', 'token')
    op.drop_column('users', 'uid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('uid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('token', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('users', 'email')
    # ### end Alembic commands ###