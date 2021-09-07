"""create table: task_status

Revision ID: e56d8ac700e9
Revises: 9030aff8bcab
Create Date: 2021-09-05 01:30:37.270478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e56d8ac700e9'
down_revision = '9030aff8bcab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=32), nullable=False),
    sa.Column('color', sa.String(length=16), nullable=False),
    sa.Column('is_complete', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_task_status_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_task_status'))
    )
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_task_status_id_task_status'), 'task_status', ['status_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('task', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_task_status_id_task_status'), type_='foreignkey')
        batch_op.drop_column('status_id')

    op.drop_table('task_status')
    # ### end Alembic commands ###