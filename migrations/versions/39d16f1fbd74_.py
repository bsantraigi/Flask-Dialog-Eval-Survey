"""empty message

Revision ID: 39d16f1fbd74
Revises: 
Create Date: 2023-02-03 10:36:00.130737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39d16f1fbd74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('annotator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_token', sa.String(length=6), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_token')
    )
    op.create_table('dialog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dialog_context', sa.String(length=200), nullable=False),
    sa.Column('response_a_model', sa.String(length=100), nullable=False),
    sa.Column('response_a', sa.String(length=100), nullable=False),
    sa.Column('response_b_model', sa.String(length=100), nullable=False),
    sa.Column('response_b', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dialog_id', sa.Integer(), nullable=False),
    sa.Column('annotator_id', sa.Integer(), nullable=False),
    sa.Column('coherence_a', sa.String(length=10), nullable=False),
    sa.Column('coherence_b', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['annotator_id'], ['annotator.id'], ),
    sa.ForeignKeyConstraint(['dialog_id'], ['dialog.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rating')
    op.drop_table('dialog')
    op.drop_table('annotator')
    # ### end Alembic commands ###
