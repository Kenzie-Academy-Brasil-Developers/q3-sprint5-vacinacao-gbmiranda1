"""criando tabela vaccine_cards

Revision ID: 1fb13d909272
Revises: 
Create Date: 2022-04-20 02:07:34.751179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fb13d909272'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vaccine_cards',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('first_shot_date', sa.DateTime(), nullable=True),
    sa.Column('second_shot_date', sa.DateTime(), nullable=True),
    sa.Column('vaccine_name', sa.String(), nullable=False),
    sa.Column('health_unit_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vaccine_cards')
    # ### end Alembic commands ###