import pymysql

try:
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234',
        database='Careers',
        connect_timeout=5
    )
    print("✅ Connected successfully!")
    with conn.cursor() as cursor:
        cursor.execute("SELECT DATABASE();")
        print("📂 Current DB:", cursor.fetchone())
except Exception as e:
    print("❌ Connection failed:", e)
