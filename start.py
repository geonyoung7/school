from flask import Flask, render_template

app = Flask(__name__)

smartphones = [
    {
        '제조사': 'Apple',
        '모델': 'iPhone 14 128GB',
        '가격': '1,250,000',
        '세부정보': 'A15 Bionic 칩 탑재, 듀얼 카메라, 최대 26시간 배터리',
    },
    {
        '제조사': 'Samsung',
        '모댈': 'Galaxy S23 256GB',
        '가격': '1,155,000',
        '세부정보': '',
    },
]

@app.route('/')
def index():
    return render_template('index.html', smartphones=smartphones)

if __name__ == '__main__':
    app.run(debug=True)
