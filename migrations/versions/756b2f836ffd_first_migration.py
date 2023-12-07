"""first migration

Revision ID: 756b2f836ffd
Revises: 
Create Date: 2023-12-07 21:18:24.713302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '756b2f836ffd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appearing_detail',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('appearing_detail', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('appearing_detail')
    )
    op.create_table('file',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('vol_num', sa.Integer(), nullable=False),
    sa.Column('file_num', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_name')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('appearing',
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('appearing_detail_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['appearing_detail_id'], ['appearing_detail.id'], ),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('file_id', 'task_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appearing')
    op.drop_table('tasks')
    op.drop_table('file')
    op.drop_table('appearing_detail')
    # ### end Alembic commands ###