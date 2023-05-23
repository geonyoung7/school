from flask import Flask, render_template

app = Flask(__name__)

smartphones = [
    {
        'brand': 'Apple',
        'model': 'iPhone 14 pro max',
        'price': '1,750,000(128GB) 1,900,000(256GB) 2,200,000(512GB) 2,500,000(1TB)',
        'description': '17cm Super Retina XDR 디스플레이, Promotion지원, 트리플 카메라, A16 바이오닉칩',
        'image': 'iphone 14 pro max.png',
    },
    {
        'brand': 'Apple',
        'model': 'iphone 14 pro',
        'price': '1,550,000(128GB) 1,700,000(256GB) 2,000,000(512GB)2,300,000(1TB)',
        'description': '15.5cm Super Retina XDR 디스플레이, Promotion지원, 트리플 카메라, A16 바이오닉칩',
        'image': 'iphone 14 pro.png',
    },
    {
        'brand': 'Apple',
        'model': 'iphone 14 plus',
        'price': '1,350,000(128GB) 1,500,000(256GB) 1,800,000(512GB)',
        'description': '17cm Super Retina XDR 디스플레이, 듀얼 카메라, A15 바이오닉칩 5코어 GPU',
        'image': 'iphone 14 plus.png',
    },
    {
        'brand': 'Apple',
        'model': 'iphone 14',
        'price': '1,250,000(128GB) 1,400,000(256GB) 1,700,000(512GB)',
        'description': '15.4cm Super Retina XDR 디스플레이, 듀얼 카메라, A15 바이오닉칩 5코어 GPU',
        'image': 'iphone 14.png',
    },
    {
        'brand': 'Apple',
        'model': 'iphone 13 mini',
        'price': '950,000(128GB) 1,090,000(256GB) 1,360,000(512GB)',
        'description': '13.7cm Super Retina XDR 디스플레이, 듀얼 카메라, A15 바이오닉칩 4코어 GPU',
        'image': 'iphone 13 mini.png',
    },
    {
        'brand': 'Apple',
        'model': 'iphone se',
        'price': '650,000(64GB) 730,000(128GB) 880,000(256GB)',
        'description': '11.9cm Retina HD 디스플레이, 싱글 카메라, A15 바이오닉칩 4코어 GPU',
        'image': 'iphone se.png',
    },
    {
        'brand': 'Samsung',
        'model': 'galaxy s23 ultra',
        'price': '1,599,400(256GB) 1,720,400(512GB) 1,962,400(1TB)',
        'description': '17.3cm Dynamic AMOLED 2X 디스플레이, 120hz 지원, 트리플 카메라, 퀄컴 스냅드래곤 8 Gen 2 for Galaxy칩',
        'image': 'galaxy s23 ultra.jpg',
    },
    {
        'brand': 'Samsung',
        'model': 'galaxy s23 plus',
        'price': '1,353,000(256GB) 1,474,000(512GB)',
        'description': '16.6cm Dynamic AMOLED 2X 디스플레이, 120hz 지원, 트리플 카메라, 퀄컴 스냅드래곤 8 Gen 2 for Galaxy칩',
        'image': 'galaxy s23 plus.png',
    }, 
    {
        'brand': 'Samsung',
        'model': 'galaxy s23',
        'price': '1,155,000(256GB) 1,276,000(512GB)',
        'description': '15.3cm Dynamic AMOLED 2X 디스플레이, 120hz 지원, 트리플 카메라, 퀄컴 스냅드래곤 8 Gen 2 for Galaxy칩',
        'image': 'galaxy s23.jpg',
    },
    {
        'brand': 'Samsung',
        'model': 'galaxy z flip 4',
        'price': '1,353,000(256GB) 1,474,000(512GB)',
        'description': '17cm Dynamic AMOLED 2X 디스플레이, 120hz 지원, 듀얼 카메라, 퀄컴 스냅드래곤 8+ Gen 1칩',
        'image': 'galaxy z flip 4.jpg',
    },
    {
        'brand': 'Samsung',
        'model': 'galaxy z fold 4',
        'price': '1,998,700(256GB) 2,119,700(512GB) 2,361,700(1TB)',
        'description': '19.2cm Dynamic AMOLED 2X 디스플레이, 120hz 지원, 트리플 카메라, 퀄컴 스냅드래곤 8+ Gen 1칩',
        'image': 'galaxy z fold 4.jpg',
    }    
]

@app.route('/')
def index():
    return render_template('index.html', smartphones=smartphones)

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/smartphone/<model>')
def smartphone_details(model):
    # Find the smartphone with the specified model
    selected_smartphone = next((s for s in smartphones if s['model'] == model), None)
    if selected_smartphone:
        return render_template('smartphone_details.html', smartphone=selected_smartphone)
    else:
        return 'Smartphone not found'