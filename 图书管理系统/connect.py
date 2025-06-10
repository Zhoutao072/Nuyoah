import pymysql

def connect():
    try:
        conn = pymysql.connect(
            host='localhost',       # 数据库主机地址
            user='root',            # 数据库用户名
            password='root',        # 数据库密码
            database='library',     # 要连接的数据库名称
            port=1888               # 数据库端口号（根据你的实际情况修改）
        )
        cursor = conn.cursor()
        print("Connected to MySQL successfully!")  # 打印成功信息
        return cursor, conn
    except Exception as e:
        print(f"Error connecting to MySQL: {e}")  # 捕获并打印错误信息
        return None, None