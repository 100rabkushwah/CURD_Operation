from django.shortcuts import render, HttpResponse
from .import DB_connection

def student(request):
    return render(request,"student_data.html")



def show_data(request):
    db, cmd = DB_connection.connection()
    q = "select student_roll, student_name from student_detail"
    cmd.execute(q)
    data = cmd.fetchall()
    db.commit()
    print(data)
    return render(request,"show_student_data.html",{'datas':data})



def creat_row(request):
    db, cmd = DB_connection.connection()
    name = request.GET['name']
    roll = request.GET['rollno']
    q = "insert into student_detail (student_roll, student_name)value({0},'{1}')".format(roll,name)
    print(name,roll)
    cmd.execute(q)
    db.commit()
    db.close()
    return show_data(request)


def delete_row(request):
    db, cmd = DB_connection.connection()
    try:
        sid = request.GET['id']
        q = "delete from student_detail where student_roll = {0}".format(sid)
        cmd.execute(q)
        db.commit()
        db.close()
        print(sid)
        return show_data(request)
    except Exception as e:
        return render(request,"show_student_data.html",{'message':'Successfully failed'})



def edit_row(request):
    db, cmd = DB_connection.connection()
    try:
        sid = request.GET['id']
        q = "select * from student_detail where student_roll = {0}".format(sid)
        cmd.execute(q)
        row=cmd.fetchone()
        db.commit()
        db.close()
        print(sid)
        return render(request,"edit_delete.html",{'row':row})
    except Exception as e:
        print("Error:",e)
        return render(request,"edit_delete.html",{'row':[]})

def update_row(request):
    db, cmd = DB_connection.connection()
    try:

        sid = request.GET['roll']
        name = request.GET['name']
        q = "update student_detail set student_name='{}' where student_roll={}".format(name,sid)
        cmd.execute(q)
        db.commit()
        db.close()
        return show_data(request)
    except Exception as e:
        print("Error:",e)
        return show_data(request)









