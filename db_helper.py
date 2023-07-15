import mysql.connector

def get_db_cursor():
    db= mysql.connector.connect(
        user='root',
        password='swayam',
        host='localhost',
        database='atliq_college_db'
    )
    cursor= db.cursor()
    return db,cursor

def close_db_connection(db,cursor):
    cursor.close()
    db.close()

def get_marks(params):
    db, cursor = get_db_cursor()
    cursor.callproc('get_marks', [params.get('student_name', ''), params.get('semester', ''), params.get('operation', '')])
    result = None
    for res in cursor.stored_results():
        result = float(res.fetchone()[0])  # Fetch the first column of the first row
    close_db_connection(db, cursor)
    return result


def get_fees(params):
    db, cursor = get_db_cursor()
    cursor.callproc('get_fees', [params.get('student_name', ''), params.get('semester', ''), params.get('fees_type', '')])
    result = None
    for res in cursor.stored_results():
        result = float(res.fetchone()[0])  # Fetch the first column of the first row
    close_db_connection(db, cursor)
    return result


if __name__ == "__main__":
    print(get_marks({
        'semester': 4,
        'operation': 'avg'
    }))

    print(get_fees({
        'student_name': "Peter Pandey",
        'semester': 1,
        'fees_type': 'paid'
    }))