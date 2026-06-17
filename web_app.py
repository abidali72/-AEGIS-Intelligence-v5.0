from flask import Flask, render_template_string, Response, jsonify
import cv2
import threading
from detector import SmokingDetector
from database import Database
import time

app = Flask(__name__)

# Initialize Detector and Database
detector = SmokingDetector()
db = Database()
cap = cv2.VideoCapture(0)

# Global variables for diagnostics
current_diagnostic = "Initializing..."
current_motion = False
current_height = "--"
current_alert = ""

def generate_frames():
    global current_diagnostic, current_motion, current_height, current_alert
    
    if not cap.isOpened():
        # Fallback to other cameras if 0 fails
        for i in [1, 2]:
            cap.open(i)
            if cap.isOpened():
                break

    while True:
        success, frame = cap.read()
        if not success:
            time.sleep(0.1)
            continue
            
        detections, people, motion_detected = detector.detect(frame)
        event, diagnostic, mouth_zone = detector.get_contextual_event(detections, people, motion_detected)
        
        current_diagnostic = diagnostic
        current_motion = motion_detected
        if people:
            avg_h = sum(p["estimated_height"] for p in people) / len(people)
            current_height = f"{avg_h:.2f}m"
            
        if event and event["category"] == "SMOKING":
            current_alert = f"🚨 SECURITY ALERT: SMOKING ({event['product']})"
        else:
            current_alert = ""
            
        display_frame = detector.draw_detections(frame.copy(), detections, people, mouth_zone)
        
        ret, buffer = cv2.imencode('.jpg', display_frame)
        frame_bytes = buffer.tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AEGIS Intelligence Web Dashboard</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 20px; display: flex; flex-direction: column; align-items: center; }
            h1 { color: #38bdf8; font-weight: 300; letter-spacing: 1px; margin-bottom: 5px; }
            .subtitle { color: #94a3b8; font-size: 14px; margin-bottom: 25px; }
            .container { display: flex; flex-direction: row; gap: 24px; width: 100%; max-width: 1200px; }
            .video-feed { flex: 2; border: 1px solid #334155; border-radius: 12px; overflow: hidden; background-color: #000; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5); }
            .video-feed img { width: 100%; height: auto; display: block; }
            .sidebar { flex: 1; display: flex; flex-direction: column; gap: 16px; }
            .panel { background-color: rgba(30, 41, 59, 0.7); backdrop-filter: blur(10px); padding: 20px; border-radius: 12px; border: 1px solid #334155; }
            .panel h3 { margin-top: 0; font-size: 12px; font-weight: 600; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; border-bottom: 1px solid #334155; padding-bottom: 8px; margin-bottom: 12px; }
            .value { font-size: 20px; font-weight: 500; color: #4ade80; }
            .alert-box { color: #ef4444; font-size: 22px; font-weight: bold; text-align: center; height: 35px; text-transform: uppercase; letter-spacing: 2px; }
        </style>
    </head>
    <body>
        <h1>🛡️ AEGIS Web Command Center</h1>
        <div class="subtitle">v5.0 Biometric & Security Platform</div>
        <div class="alert-box" id="alert-box"></div>
        <div class="container">
            <div class="video-feed">
                <img src="/video_feed" alt="AEGIS Video Feed">
            </div>
            <div class="sidebar">
                <div class="panel">
                    <h3>Analytics Engine</h3>
                    <div class="value" id="diag-value">Initializing...</div>
                </div>
                <div class="panel">
                    <h3>Motion Status</h3>
                    <div class="value" id="motion-value" style="color: #94a3b8;">Idle</div>
                </div>
                <div class="panel">
                    <h3>Estimated Target Height</h3>
                    <div class="value" id="height-value">--</div>
                </div>
            </div>
        </div>
        <script>
            function updateStats() {
                fetch('/stats')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('diag-value').innerText = data.diagnostic;
                        const motionEl = document.getElementById('motion-value');
                        motionEl.innerText = data.motion ? 'DETECTED' : 'Idle';
                        motionEl.style.color = data.motion ? '#ef4444' : '#94a3b8';
                        document.getElementById('height-value').innerText = data.height;
                        
                        const alertEl = document.getElementById('alert-box');
                        alertEl.innerText = data.alert;
                    })
                    .catch(e => console.log(e));
            }
            setInterval(updateStats, 1000);
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stats')
def stats():
    return jsonify({
        "diagnostic": current_diagnostic,
        "motion": current_motion,
        "height": current_height,
        "alert": current_alert
    })

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
