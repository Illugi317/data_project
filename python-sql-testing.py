import mysql.connector
from datetime import date, datetime, timedelta

cxw = mysql.connector.connect(user='helgiste_test', password='ab123', host='108.167.160.53', database='helgiste_DataProject')
cursor = cxw.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)

add_employee = ('INSERT INTO employees '
                '(first_name, last_name, hire_date, gender, birth_date) '
                'VALUES (%s, %s, %s, %s, %s)')

data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))

cursor.execute(add_employee, data_employee)

cxw.commit()
cursor.close()
cxw.close()
