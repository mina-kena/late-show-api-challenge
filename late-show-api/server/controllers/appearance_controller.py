from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models.appearance import Appearance
from models.episode import Episode
from models.guest import Guest
from models import db

appearance_bp = Blueprint('appearances', __name__)

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    
    if not data or 'rating' not in data or 'guest_id' not in data or 'episode_id' not in data:
        return jsonify({'error': 'rating, guest_id, and episode_id are required'}), 400
    
    if not 1 <= data['rating'] <= 5:
        return jsonify({'error': 'Rating must be between 1 and 5'}), 400
    
    guest = Guest.query.get(data['guest_id'])
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404
    
    episode = Episode.query.get(data['episode_id'])
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    
    appearance = Appearance(
        rating=data['rating'],
        guest_id=data['guest_id'],
        episode_id=data['episode_id']
    )
    
    db.session.add(appearance)
    db.session.commit()
    
    return jsonify({
        'id': appearance.id,
        'rating': appearance.rating,
        'guest_id': appearance.guest_id,
        'episode_id': appearance.episode_id
    }), 201