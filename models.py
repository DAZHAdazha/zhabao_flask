from exts import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'  # 表名
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)  # autoincrement为自增
    username = db.Column(db.String(16), unique=True, nullable=False)  # nullable=False 不能为空
    age = db.Column(db.Integer)
    phone = db.Column(db.String(11))
    password = db.Column(db.Text)
    # content = db.Column(db.Text) # text类型为无限长度的字符串

    def __init__(self, *args, **kwargs):
        username = kwargs.get('username')
        phone = kwargs.get('phone')
        password = kwargs.get('password')
        age = kwargs.get('age')
        self.phone = phone
        self.age = age
        self.username = username
        # 加密密码，注意需要导入
        self.password = generate_password_hash(password)

    # 检查密码函数
    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

    def __repr__(self):
        return '<id:%d username:%s age:%d phone:%s password:%s >' % (self.id, self.username, self.age, self.phone, self.password)

class User_Data(db.Model):
    __tablename__ = 'user_data'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    cart = db.Column(db.Text)
    # 第一参数为要关联的表的模型的名字,作为正向引用，backref表示反向引用，以后可以通过User.user_datas反向引用来通过user对象查找
    # 对应User_data表的数据
    user = db.relationship('User', backref=db.backref("user_datas"))

    def __repr__(self):
        return '<id:%d username:%s cart:%s buy:%s >' % (self.id, self.username, self.cart)


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(32), unique=True)
    price = db.Column(db.Float, nullable=False)
    seller = db.Column(db.String(32))
    img_path = db.Column(db.String(64))
    product_path = db.Column(db.String(64))
    seller_path = db.Column(db.String(64))

    def __repr__(self):
        return '<id:%d price:%f seller:%s img_path:%s product_path:%s seller_path:%s>' % (self.id, self.price, self.seller, self.img_path, self.product_path, self.seller_path)


def database_init():
    product1 = Product(name='BlackWidow', price=799, seller='Razer Store', img_path="../static/img/keyboard1.jpg", product_path='../HTML/keyboard1.html', seller_path='../HTML/razer.html')
    product2 = Product(name='Logitech G813', price=1100, seller='Logi Store', img_path="../static/img/keyboard2.jpg", product_path='../HTML/keyboard2.html', seller_path='../HTML/logitech.html')
    product3 = Product(name='Apex 7', price=500, seller='SteelSeries', img_path="../static/img/keyboard3.jpg", product_path='../HTML/keyboard3.html', seller_path='../HTML/steelseries.html')
    product4 = Product(name='Zowie BenQ', price=800, seller='Zowie Store', img_path="../static/img/keyboard4.jpg", product_path='../HTML/keyboard4.html', seller_path='../HTML/zowie.html')
    product5 = Product(name='Corsair K70', price=1990, seller='Corsair Store', img_path="../static/img/keyboard5.jpg", product_path='../HTML/keyboard5.html', seller_path='../HTML/corsair.html')
    product6 = Product(name='Huntsman', price=1349, seller='Razer Store', img_path="../static/img/keyboard6.jpg", product_path='../HTML/keyboard6.html', seller_path='../HTML/razer.html')
    product7 = Product(name='DeathAdder', price=250, seller='Razer Store', img_path="../static/img/mouse1.jpg", product_path='../HTML/mouse1.html', seller_path='../HTML/razer.html')
    product8 = Product(name='Logitech G502', price=350, seller='Logi Store', img_path="../static/img/mouse2.jpg", product_path='../HTML/mouse2.html', seller_path='../HTML/logitech.html')
    product9 = Product(name='Zowie S2', price=530, seller='Zowie Stor', img_path="../static/img/mouse3.jpg", product_path='../HTML/mouse3.html', seller_path='../HTML/zowie.html' )
    product10 = Product(name='Rival 600', price=180, seller='SteelSeries', img_path="../static/img/mouse4.jpg", product_path='../HTML/mouse4.html', seller_path='../HTML/steelseries.html')
    product11 = Product(name='Razer Mamba', price=500, seller='Razer Store', img_path="../static/img/mouse5.jpg", product_path='../HTML/mouse5.html', seller_path='../HTML/razer.html')
    product12 = Product(name='Logitech G903', price=979, seller='Logi Store', img_path="../static/img/mouse6.jpg", product_path='../HTML/mouse6.html', seller_path='../HTML/logitech.html')
    product13 = Product(name='Razer Nari', price=230, seller='Razer Store', img_path="../static/img/headphone1.jpg", product_path='../HTML/headphone1.html', seller_path='../HTML/razer.html')
    product14 = Product(name='Hammer', price=430, seller='Zowie Store', img_path="../static/img/headphone2.jpg", product_path='../HTML/headphone2.html', seller_path='../HTML/zowie.html')
    product15 = Product(name='Logitech H340', price=330, seller='Logi Store', img_path="../static/img/headphone3.jpg", product_path='../HTML/headphone3.html', seller_path='../HTML/logitech.html')
    product16 = Product(name='Bose NC700', price=2000, seller='Bose Store', img_path="../static/img/headphone4.jpg", product_path='../HTML/headphone4.html', seller_path='../HTML/bose.html')
    product17 = Product(name='Solo Wireless', price=1990, seller='Beats Store', img_path="../static/img/headphone5.jpg", product_path='../HTML/headphone5.html', seller_path='../HTML/beats.html')
    product18 = Product(name='Bose QC35', price=2550, seller='Bose Store', img_path="../static/img/headphone6.jpg", product_path='../HTML/headphone6.html', seller_path='../HTML/bose.html')
    product19 = Product(name='iphone XR', price=5500, seller='Apple Store', img_path="../static/img/phone1.jpg", product_path='../HTML/phone1.html', seller_path='../HTML/apple.html')
    product20 = Product(name='Mate 30 Pro', price=5400, seller='Huawei Store', img_path="../static/img/phone2.jpg", product_path='../HTML/phone2.html', seller_path='../HTML/huawei.html')
    product21 = Product(name='Meizu 16Xs', price=2290, seller='Meizu Store', img_path="../static/img/phone3.jpg", product_path='../HTML/phone3.html', seller_path='../HTML/meizu.html')
    product22 = Product(name='Galaxy S10', price=7500, seller='Samsung Store', img_path="../static/img/phone4.jpg", product_path='../HTML/phone4.html', seller_path='../HTML/samsung.html')
    product23 = Product(name='vivo NEX 3', price=5599, seller='vivo Store', img_path="../static/img/phone5.jpg", product_path='../HTML/phone5.html', seller_path='../HTML/vivo.html')
    product24 = Product(name='iphone 8 plus', price=4999, seller='Apple Store', img_path="../static/img/phone6.jpg", product_path='../HTML/phone6.html', seller_path='../HTML/apple.html')
    db.session.add_all([product1, product2, product3, product4, product5, product6, product7,
                       product8, product9, product10, product11, product12, product13, product14,
                       product15, product16, product17, product18, product19, product20, product21,
                       product22, product23, product24])
    db.session.commit()