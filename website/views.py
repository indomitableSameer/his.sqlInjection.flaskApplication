from flask import Blueprint, redirect, render_template, request, flash, url_for

from website.db import opendb

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        cnx = opendb()
        employeeId = request.form.get('employeeId')
        print(employeeId)
        sqlQuery = "select id, name, msg from users where id=" + employeeId
        print(sqlQuery)
        cursor = cnx.cursor()
        cursor.execute(sqlQuery)
        records = cursor.fetchall()

        print("total=", cursor.rowcount)
        for row in records:
            print("id=", row[0])
            print("name=", row[1])
            print("msg=", row[2])
        cnx.close()
        #return redirect(url_for('views.datadisplay'))
        print(records)
        return render_template("infodisplay.html", users=records)
    return render_template("userinput.html")

@views.route('/datadisplay')
def datadisplay():
    return render_template("infodisplay.html")