# 引入函示庫
import pymysql

# 與DB建立連線 #IP #username #password #datebasename
db = pymysql.connect('localhost', 'root', '', 'db_test')

# 用ursor()來建立操作用的物件
cursor = db.cursor()

# SQL操作語法
# INSERT INTO '表格名' ('欄位1', '欄位2', ...)
# VALUES ('值1', '值2', ...);
table_name = 'student_info'
name = '小高'
stu_id = 'N001'
mail = 'N001@nknu'
sql = '''INSERT INTO `''' + table_name + '''` (`Name`, `ID`, `MailAddress`) 
        VALUES (\'''' + name + '''\', \'''' + stu_id + '''\', \'''' + mail + '''\')'''

# 使用try: & except: 來抓取錯誤訊息
try:
    # 執行SQL語法
    cursor.execute(sql)
    # 確認執行
    db.commit()
    print('執行成功')
except:
    # 如果發生錯誤則返回上一步
    db.rollback()
    print('發生錯誤')

# 關閉連線，避免佔用資源
db.close()
