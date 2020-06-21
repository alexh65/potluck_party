"""empty message

Revision ID: dbb5557422ce
Revises: 
Create Date: 2020-06-16 20:10:31.282200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbb5557422ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ingredient_name', sa.String(length=50), nullable=False),
    sa.Column('calories_per_serving', sa.Integer(), nullable=True),
    sa.Column('serving_amount', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('email_address', sa.String(length=50), nullable=True),
    sa.Column('user_bio', sa.String(length=225), nullable=True),
    sa.Column('profile_pic', sa.String(length=225), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_address')
    )
    op.create_table('friends',
    sa.Column('friend1_id', sa.Integer(), nullable=False),
    sa.Column('friend2_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('friend1_id < friend2_id', name='firstIdIsLessThanSecond'),
    sa.ForeignKeyConstraint(['friend1_id'], ['user_info.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['friend2_id'], ['user_info.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('friend1_id', 'friend2_id')
    )
    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.Column('recipe_desc', sa.String(length=225), nullable=True),
    sa.Column('recipe_result_pic', sa.String(length=200), nullable=True),
    sa.Column('prep_time', sa.Integer(), nullable=True),
    sa.Column('cook_time', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_login',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user_info.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('recipe_ingredient',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('amount_unit', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('recipe_id', 'ingredient_id')
    )
    op.create_table('recipe_step',
    sa.Column('recipe_id', sa.Integer(), nullable=False),
    sa.Column('step_no', sa.Integer(), nullable=False),
    sa.Column('step_desc', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('recipe_id', 'step_no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_step')
    op.drop_table('recipe_ingredient')
    op.drop_table('user_login')
    op.drop_table('recipe')
    op.drop_table('friends')
    op.drop_table('user_info')
    op.drop_table('ingredient')
    # ### end Alembic commands ###