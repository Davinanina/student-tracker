from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity


from App.controllers import *

user_views = Blueprint('user_views', __name__, template_folder='../templates')

# @user_views.route('/api/students', methods=['GET'])
# def get_students_action():
#     users = get_all_students()
#     return jsonify(users)

@user_views.route('/students', methods=['GET'])
def get_user_page():
    users = get_all_students()
    return render_template('users.html', users=users)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_action():
    data = request.json
    print(data)
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})
    # return jsonify("")


@user_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_user_action():
    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')