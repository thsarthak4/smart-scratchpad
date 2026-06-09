from flask import Flask, render_template, request, jsonify
import re
import json
import os

# -------------------------------------------------------------------------
# FORCE PATH RESOLUTION FOR LOCAL AND VERCEL RUNTIMES
# -------------------------------------------------------------------------
# This looks at the exact absolute path of this index.py file on your Windows machine,
# moves up one directory level, and explicitly binds the templates folder.
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
template_dir = os.path.join(parent_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

def analyze_payload(text):
    text = text.strip()
    if not text:
        return {"type": "empty", "message": "No data detected."}
    
    # 1. Check for valid JSON
    if text.startswith('{') or text.startswith('['):
        try:
            parsed_json = json.loads(text)
            return {
                "type": "json",
                "message": "Valid structural JSON parsed successfully.",
                "data": parsed_json
            }
        except ValueError:
            return {
                "type": "malformed_json",
                "message": "Malformed JSON Detected. Check for missing brackets, trailing commas, or quotes.",
                "raw": text
            }

    # 2. Check for Python Stack Trace / Error Logs
    if "Traceback (most recent call last)" in text or re.search(r"File \".*\", line \d+", text):
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        error_summary = lines[-1] if lines else "Unknown Execution Exception"
        locations = re.findall(r"File \"(.*)\", line (\d+)", text)
        file_info = f"Error located in {locations[-1][0]} on line {locations[-1][1]}" if locations else "Unknown execution path"
        
        return {
            "type": "error_log",
            "summary": error_summary,
            "location": file_info,
            "raw": text
        }

    # 3. Check for raw links list
    urls = re.findall(r'https?://[^\s]+', text)
    if len(urls) >= 1:
        return {
            "type": "links",
            "message": f"Harvested {len(urls)} live URL endpoints.",
            "links": urls
        }

    # 4. Fallback to general narrative plaintext
    word_count = len(text.split())
    char_count = len(text)
    reading_time = max(1, round(word_count / 200))
    
    return {
        "type": "text",
        "message": "Plaintext / Narrative Body",
        "stats": {
            "words": word_count,
            "characters": char_count,
            "est_reading_time_min": reading_time
        }
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if not request.is_json:
        return jsonify({"error": "Payload must be application/json"}), 400
        
    data = request.get_json()
    input_text = data.get('text', '')
    analysis_result = analyze_payload(input_text)
    return jsonify(analysis_result)

# Expose app safely for Vercel
app = app