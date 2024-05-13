from sqlalchemy.orm import scoped_session, sessionmaker

from utils import managed_session
from models import db
import os

class Submissions:
    def __init__(self, sql_engine):
        self.sql_engine = sql_engine
        self.session_factory = scoped_session(sessionmaker(bind=self.sql_engine))
    