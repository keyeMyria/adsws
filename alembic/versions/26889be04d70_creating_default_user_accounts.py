"""creating default user accounts

Revision ID: 26889be04d70
Revises: 33d84dc97ea1
Create Date: 2014-09-10 00:08:49.335000

"""

# revision identifiers, used by Alembic.
revision = '26889be04d70'
down_revision = '33d84dc97ea1'

from alembic import op
import sqlalchemy as sa
from werkzeug.security import gen_salt
from adsws.factory import create_app
def upgrade():
    

        anonymous = User.query.get(0)