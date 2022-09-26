
from ast import Not
from asyncio.windows_events import NULL
from contextlib import nullcontext
from email.message import EmailMessage
import pyodbc
from flask import Flask,request
app = Flask(__name__)
connection=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=USER-PC;DATABASE=dbs_school;Trusted_Connection=yes;')
@app.route('/saveStudent',methods=['POST'])
def saveStudent():
    name=request.args['name']
    age=request.args['age']
    email=request.args['email']
    
    '''
    name='amrutha'
    age=25
    email='connection@gmail.com'
    '''
    cursor=connection.cursor()
    inserQuery = "INSERT INTO student (name,age,Email_id) VALUES ('"+name+"',"+str(age)+",'"+email+"')"
    print(inserQuery)
    cursor.execute(inserQuery)
    connection.commit()
    #VALUES (?, ?, ?)",(name,age,email))
    return str(cursor.rowcount)
 
    
    
@app.route('/updateStudent',methods=['PUT'])
def updateStudent():
    name=request.args['name']
    stId=request.args['id']
    age=request.args['age']
    print(request.args['age'])
    email=request.args['email']
    query="SELECT name,age,Email_id FROM student WHERE student_id=?"
    cursor=connection.cursor()
    cursor.execute(query,stId)
    existing_details=cursor.fetchone()
    print(existing_details[1])
    if name is None or not name:
        name=existing_details[0]
    if age is None or not age:
        age=existing_details[1]

    if email is None or not email:
        email=existing_details[2]
          
    #studentId=1
    #name='aisu'
    #cursor=connection.cursor()
    sql="UPDATE student SET name=?,age=?,Email_id=? WHERE student_id=?"
    #tuple1=(name,studentId)
    cursor.execute(sql,name,age,email,stId)
    print(age)
    connection.commit()
    return str(cursor.rowcount)
   
    
    
@app.route('/selectStudent')
def selectStudent():
    stId=request.args['id']
    #studentId=1
    cursor=connection.cursor()
    sel_query="SELECT * FROM student WHERE student_id = ?"
    #stId=studentId
    cursor.execute(sel_query,stId)
    #print(cursor._executed)
    return {'results': str(cursor.fetchone())}
            
    
    
@app.route('/selectAllStudent')
def selectAllStudent():
    cursor=connection.cursor()
    sel_all_query="SELECT * FROM student"
    cursor.execute(sel_all_query)
    return {'results':
            [dict(zip([column[0] for column in cursor.description], row))
             for row in cursor.fetchall()]}
    #return cursor.fetchone()
    
@app.route('/deleteStudent',methods=['DELETE'])
def deleteStudent():
    stuId=request.args['id']
    #studentId=1
    cursor=connection.cursor()
    del_query="""Delete from student where student_id = ?"""
    #stuId=studentId
    cursor.execute(del_query,stuId)
    connection.commit()
    return str(cursor.rowcount)
    
    
    
    
if __name__=='__main__':
    app.run(port=8000)
 
 
    

       

    
    

    
    
    
    
