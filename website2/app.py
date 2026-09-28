from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head><title>Website 2 - Dashboard</title></head>
<body style="font-family:Arial; padding:40px; background:#f4f6f9;">
    <div style="background:white; padding:20px; border-radius:8px; border:1px solid #ddd;">
        <h1>WEBSITE 2: TRANG QUẢN TRỊ / BÁO CÁO</h1>
        <p><strong>Sinh viên thực hiện:</strong> Trần Đình Quang - K235480106057</p>
        <p><strong>Hệ thống:</strong> Chạy mô hình Multi-container qua Nginx Reverse Proxy.</p>
        <hr>
        <a href="/"><- Quay lại Website 1</a>
    </div>
</body>
</html>
'''

@app.route('/')
def dashboard():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)