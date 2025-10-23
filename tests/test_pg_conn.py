import psycopg2

try:
    conn = psycopg2.connect(
        dbname="ragdb",
        user="postgres",
        password="Madinah017#",
        host="localhost",
        port=5432
    )
    print("Koneksi ke PostgreSQL BERHASIL")
    conn.close()
except Exception as e:
    print("Koneksi GAGAL:", e)
