# 引入函示庫
import pymysql

# 與DB建立連線 #IP #username #password #datebasename
db = pymysql.connect('localhost', 'root', '', 'db_test')

# 用ursor()來建立操作用的物件
cursor = db.cursor()

# SQL操作語法
# SELECT "欄位名" FROM "表格名";
sql = '''SELECT * FROM `student_info`'''

# 使用try: & except: 來抓取錯誤訊息
try:
    # 執行SQL語法
    cursor.execute(sql)
    # 使用fetchall()來抓資料庫回傳資料
    results = cursor.fetchall()
    # 將欄位用變數裝起來
    for row in results:
        Name = row[0]
        ID = row[1]
        Mail = row[2]
        # 顯示結果
        print('姓名：' + Name + ' 學號：' + ID + ' 信箱：' + Mail)
    print('執行成功')
except:
    # 如果發生錯誤則返回上一步
    db.rollback()
    print('發生錯誤')

# 關閉連線，避免佔用資源
db.close()
