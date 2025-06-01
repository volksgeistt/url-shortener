from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import json
import os
from datetime import datetime
from urllib.parse import urlparse
import tempfile

app = Flask(__name__)
CORS(app)

# Use /tmp directory for file storage in serverless environment
DATA_FILE = '/tmp/url_data.json'

def load_url_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except:
            return {'urls': [], 'count': 0}
    return {'urls': [], 'count': 0}

def save_url_data(data):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def normalize_url(url):
    url = url.strip()
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    return url

def shorten_url(url):
    try:
        api_url = f"https://tinyurl.com/api-create.php?url={url}"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            short_url = response.text.strip()
            if short_url.startswith('http') and 'tinyurl.com' in short_url:
                return short_url
        return None
    except:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    try:
        data = request.get_json()
        
        if not data or 'url' not in data:
            return jsonify({'error': 'URL is required'}), 400
        
        original_url = data['url'].strip()
        if not original_url:
            return jsonify({'error': 'URL cannot be empty'}), 400
        
        normalized_url = normalize_url(original_url)
        if not is_valid_url(normalized_url):
            return jsonify({'error': 'Please enter a valid URL'}), 400
        
        short_url = shorten_url(normalized_url)
        if not short_url:
            return jsonify({'error': 'Failed to shorten URL'}), 500
        
        url_data = load_url_data()
        url_entry = {
            'original': normalized_url,
            'shortened': short_url,
            'created_at': datetime.now().isoformat()
        }
        url_data['urls'].append(url_entry)
        url_data['count'] += 1
        save_url_data(url_data)
        
        return jsonify({
            'short_url': short_url,
            'original_url': normalized_url,
            'total_count': url_data['count']
        })
        
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

@app.route('/stats', methods=['GET'])
def get_stats():
    url_data = load_url_data()
    return jsonify({'total_count': url_data['count']})

# Vercel requires this for serverless functions
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# Export the app for Vercel
app = app