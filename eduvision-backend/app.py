import os
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_socketio import SocketIO
from flask_cors import CORS
import json
import time
import threading
from services.ai_processor import AIProcessor
from services.camera_service import CameraService
from services.analytics_service import AnalyticsService

# Setup logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-domain requests
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize services
ai_processor = AIProcessor()
camera_service = CameraService()
analytics_service = AnalyticsService()

# Global variables
active_session = None
device_status = "ready"

# Paths to frontend files
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'eduvision-frontend')

# Routes for serving frontend files
@app.route('/')
def serve_index():
    """Serve the frontend index.html"""
    return send_from_directory(frontend_dir, 'index.html')

@app.route('/views/<path:path>')
def serve_views(path):
    """Serve frontend view files"""
    return send_from_directory(os.path.join(frontend_dir, 'views'), path)

@app.route('/assets/<path:path>')
def serve_assets(path):
    """Serve frontend asset files"""
    assets_dir = os.path.join(frontend_dir, 'assets')
    # Determine subdirectory (css, js, img)
    if path.startswith('css/'):
        return send_from_directory(os.path.join(assets_dir, 'css'), path[4:])
    elif path.startswith('js/'):
        return send_from_directory(os.path.join(assets_dir, 'js'), path[3:])
    elif path.startswith('img/'):
        return send_from_directory(os.path.join(assets_dir, 'img'), path[4:])
    return send_from_directory(assets_dir, path)

# API Endpoints (keep all your existing API endpoints)
@app.route('/api/status')
def get_status():
    """Get the current status of the AI Vision system"""
    global device_status
    return jsonify({
        'status': device_status,
        'device_info': {
            'name': 'EduVision AI',
            'model': 'Jetson Nano J1010',
            'camera': 'Wide-angle 8MP',
            'ip_address': request.remote_addr
        }
    })

# ... (rest of your API endpoints remain the same)

# Run the application
if __name__ == '__main__':
    print(f"Frontend directory: {frontend_dir}")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)