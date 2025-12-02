from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# konfigurasi database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="your_mysql_password",
  database="db_nilai or your_db_name"
)

# fungsi untuk mendapatkan data mahasiswa dari database
def get_data():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()
    cursor.close()
    return data

# halaman utama
@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

# halaman untuk menambahkan data mahasiswa
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nim = request.form['NIM']
        nama = request.form['Nama']
        kelas = request.form['Kelas']
        fc = request.form['Fundamental_Cloud']
        db = request.form['Db']
        py = request.form['Py']
        linux = request.form['Linux']
        cursor = mydb.cursor()
        sql = "INSERT INTO mahasiswa (NIM, Nama, Kelas, Fundamental_Cloud, Db, Py, Linux) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (nim, nama, kelas, fc, db, py, linux)
        cursor.execute(sql, val)
        mydb.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('add.html')

# halaman untuk mengedit data mahasiswa
@app.route('/edit/<string:nim>', methods=['GET', 'POST'])
def edit(nim):
    cursor = mydb.cursor()
    if request.method == 'POST':
        nama = request.form['Nama']
        kelas = request.form['Kelas']
        fc = request.form['Fundamental_Cloud']
        db = request.form['Db']
        py = request.form['Py']
        linux = request.form['Linux']
        sql = "UPDATE mahasiswa SET Nama=%s, Kelas=%s, Fundamental_Cloud=%s, Db=%s, Py=%s, Linux=%s WHERE NIM=%s"
        val = (nama, kelas, fc, db, py, linux, nim)
        cursor.execute(sql, val)
        mydb.commit()
        cursor.close()
        return redirect(url_for('index'))
    else:
        sql = "SELECT * FROM mahasiswa WHERE NIM=%s"
        val = (nim,)
        cursor.execute(sql, val)
        data = cursor.fetchone()
        cursor.close()
        return render_template('edit.html', data=data)
    

# proses delete data mahasiswa
@app.route('/delete/<string:nim>', methods=['GET', 'POST'])
def delete(nim):
    cursor = mydb.cursor()
    sql = "DELETE FROM mahasiswa WHERE NIM=%s"
    val = (nim,)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
