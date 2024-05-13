from flask import Flask, request, g
from sqlalchemy import create_engine
# from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy import create_engine, ForeignKey
from models import db
from repository import Teams, Challenges, Rounds    
from service import AuthService, ChallengeService
import logging

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_dir, 'data')
os.makedirs(data_path, exist_ok=True)
database_path = 'sqlite:///'+ os.path.join(project_dir, 'data', 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = data_path

# db = SQLAlchemy(app)

SQL_ENGINE = create_engine(database_path, echo=True)
db.Base.metadata.create_all(SQL_ENGINE)
teams = Teams(SQL_ENGINE)
auth_service = AuthService(logging, teams)
rounds = Rounds(SQL_ENGINE)
challenges = Challenges(SQL_ENGINE)
challenge_service = ChallengeService(logging, challenges, rounds)
@app.before_request
def load_blueprint():
    g.teams = teams
    g.auth_service = auth_service
    g.data_path = data_path
    g.challenge_service = challenge_service
from controller import auth_bp, challenge_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(challenge_bp, url_prefix="/challenge")

if __name__ == "__main__":
    app.run(debug=True)
