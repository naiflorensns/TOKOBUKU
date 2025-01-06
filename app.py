import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nai16dor06',  
            database='TokoBuku'
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def create_buku(connection, judul, penulis, penerbit, tahun_terbit, harga, stok):
    """Insert a new book into the Buku table."""
    cursor = connection.cursor()
    query = """
    INSERT INTO Buku (judul, penulis, penerbit, tahun_terbit, harga, stok)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (judul, penulis, penerbit, tahun_terbit, harga, stok))
    connection.commit()
    print("Buku added successfully")

def get_all_buku(connection):
    """Fetch all books from the Buku table."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Buku")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def main():
    connection = create_connection()
    
    # Menambahkan buku baru
    create_buku(connection, 'Belajar Python', 'John Doe', 'Penerbit A', 2023, 150000, 10)
    
    # Menampilkan semua buku
    print("Daftar Buku:")
    get_all_buku(connection)

    if connection:
        connection.close()

if __name__ == "__main__":
    main()