import os
import psycopg2
import time

print("🔍 Tentando conectar no banco...")

for i in range(10):
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            connect_timeout=5
        )
        print("✅ Conectado com sucesso!")
        conn.close()
        break
    except Exception as e:
        print(f"⏳ Tentativa {i+1}/10 falhou...")
        time.sleep(3)
else:
    print("❌ Não foi possível conectar ao banco")
