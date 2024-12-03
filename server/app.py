from flask_cors import CORS
from web import create_app

app = create_app()
# 允许跨域请求
CORS(app, supports_credentials=True)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=8089)