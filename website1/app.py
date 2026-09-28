from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Website 1 - Login</title>
    <style>
        body { font-family: Arial; text-align: center; padding-top: 50px; background: #f9f9f9; }
        .box { display: inline-block; background: white; border: 1px solid #ccc; padding: 25px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        input { padding: 8px; margin: 5px; width: 200px; }
        button { padding: 8px 15px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
        button:hover { background: #218838; }
        #result { margin-top: 15px; font-weight: bold; color: #155724; background: #d4edda; padding: 10px; border-radius: 4px; display: none; }
    </style>
</head>
<body>
    <div class="box">
        <h2>WEBSITE 1: FORM ĐĂNG NHẬP</h2>
        <input type="text" id="user" placeholder="Username (nhập admin)"><br>
        <input type="password" id="pass" placeholder="Password"><br><br>
        <button type="button" onclick="login()">Đăng nhập</button>
        <div id="result"></div>
        <hr style="margin-top:20px;">
        <p><a href="/dashboard/">-> Chuyển sang Website 2 (Dashboard)</a></p>
    </div>

    <script>
        function login() {
            var user = document.getElementById('user').value;
            var res = document.getElementById('result');
            if(user.trim() === '') {
                alert('Vui lòng nhập Username!');
            } else {
                res.style.display = 'block';
                res.innerHTML = '✅ Đăng nhập thành công!<br>Xin chào: ' + user + '<br>Sinh viên: Trần Đình Quang - K235480106057';
            }
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)