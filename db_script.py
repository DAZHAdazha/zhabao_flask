from flask_script import Manager

db_manager = Manager() # 此处不用加app以及if __name__ == '__main__'，因为该文件并不作为主文件运行


@db_manager.command
def init():
    print('数据库已初始化完成')


@db_manager.command
def migrate():
    print('数据库已完成迁移')