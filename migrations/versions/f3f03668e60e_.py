"""empty message

Revision ID: f3f03668e60e
Revises: 
Create Date: 2023-07-28 06:08:07.090710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3f03668e60e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=42), nullable=True),
    sa.Column('category', sa.String(length=48), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=48), nullable=True),
    sa.Column('budget', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('lists')
    op.drop_table('items')
    # ### end Alembic commands ###