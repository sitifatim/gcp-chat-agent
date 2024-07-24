from flask import jsonify, render_template, request, Blueprint
from app.services.gcp_chat import detect_intent
import uuid
from . import app_routes

@app_routes.route('/')
def index():
    return render_template('chatroom.html')

@app_routes.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    session_id = request.json.get('session_id', str(uuid.uuid4()))
    
    bot_response = detect_intent(session_id, user_message)
    
    return jsonify({
        'response': bot_response,
        'session_id': session_id
    })