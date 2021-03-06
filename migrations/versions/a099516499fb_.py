"""empty message

Revision ID: a099516499fb
Revises: 47a8131da8b7
Create Date: 2020-05-03 19:48:53.137737

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a099516499fb'
down_revision = '47a8131da8b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_data', 'buy')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_data', sa.Column('buy', mysql.TEXT(), nullable=True))
    # ### end Alembic commands ###
