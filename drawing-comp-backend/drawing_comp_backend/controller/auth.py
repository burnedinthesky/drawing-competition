from flask import url_for, jsonify, request, g, Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

# @problem_bp.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# @problem_bp.route('/<string:invalid_path>')
# def handle_unmatched(*args, **kwargs):
#     return jsonify({"error": "Api not found"}), 404


@auth_bp.route("/", methods=["POST"])
def create_team():
    data = request.get_json()  # Get the JSON payload
    # team_name = data.get("name")
    token = data.get("token")
    team_token = g.auth_service.create_team(token)

    return jsonify({"Team token": team_token})

@auth_bp.route("/<string:team_token>", methods=["GET"])
def query_team(team_token):
    team = g.auth_service.query_team(team_token)
    
    if team is None:
        return jsonify({"error": "Team not found"}), 404
    return jsonify(team)

@auth_bp.route("/<string:team_token>", methods=["PUT"])
def update_team(team_token):
    data = request.get_json()
    name = data.get("name")
    team_id = g.auth_service.update_team(team_token, name)
    if not team_id:
        return jsonify({"error": "Team not found"}), 404
    return jsonify({"Team updated": team_id})

@auth_bp.route("/all_teams", methods=["GET"])
def query_all_teams():
    teams = g.auth_service.query_all_teams()
    return jsonify(teams)