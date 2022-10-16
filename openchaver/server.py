def server():
    import time
    from .db import get_configuration_db

    configdb = get_configuration_db()
    if configdb.is_configured:
        time.sleep(60)
        return
    
    from flask import Flask, jsonify, request
    from marshmallow import Schema, fields
    from .const import LOCAL_SERVER_PORT
    from .api import api    

    app = Flask(__name__)

    class ConfigureRequest(Schema):
        device_id = fields.UUID(required=True)
    
    @app.route('/configure', methods=['POST'])
    def configure():
        data = request.get_json()
        
        errors = ConfigureRequest().validate(data)
        if errors:
            return jsonify(errors), 400
        
        device_id = data['device_id']

        # Check if device exists
        status = api(f'devices/{device_id}/register_device/')
        if not status:
            return jsonify({'error': 'Device does not exist'}), 400
        else:
            success = configdb.save_device_id(data['device_id'])
            if success:
                return jsonify({'success': True})
            else:
                return jsonify({"error": "Current device already configured."}), 400

    app.run(port=LOCAL_SERVER_PORT)