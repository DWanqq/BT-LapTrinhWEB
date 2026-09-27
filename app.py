from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_FORM = '''
<!DOCTYPE html>
<html>
<head>
    <title>Web Login Demo</title>
    <style>
        body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: #f0f2f5; }
        .login-card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: center; width: 300px; }
        input { width: 90%; padding: 10px; margin: 8px 0; border: 1px solid #ccc; border-radius: 4px; }
        button { width: 95%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        .msg { margin-top: 15px; color: green; font-weight: bold; }
        .error { color: red; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>Web Login</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Đăng nhập</button>
        </form>
        {% if message %}
            <p class="msg {{ 'error' if is_error else '' }}">{{ message }}</p>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    is_error = False
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == 'admin' and pwd == '123456':
            msg = 'Đăng nhập thành công!'
        else:
            msg = 'Sai tài khoản hoặc mật khẩu!'
            is_error = True
    return render_template_string(HTML_FORM, message=msg, is_error=is_error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
