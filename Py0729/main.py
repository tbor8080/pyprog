import os, sys, datetime,sqlite3
from flask import Flask, render_template, request, redirect
from modules.search import *

############################################################
############################################################
# FrameWork: Flask
# Virtual Enveiroment > python -m venv [virtual directory]
# Install > pip install flask
############################################################
# Global Variable
############################################################
port=50000
debug=True

db_name='./database/ledger.db'
############################################ Global Variable

app=Flask(__name__)

page_title='Pythonと基本情報処理科'

@app.route('/')
def index():
    flag='index'
    items=[]
    conn=sqlite3.connect(db_name)
    cursor=conn.cursor()
    
    sql='SELECT * from COMPANY_DOCUMENT_LIST;'
    cursor.execute(sql)
    items=cursor.fetchall()
    
    sql='SELECT NAME FROM sqlite_master WHERE TYPE=\'table\';'
    cursor.execute(sql)
    table=cursor.fetchall()[1:]
    
    conn.close()

    # print(table)
    
    return render_template(
    'main.html',
    items=items, page_title=page_title, flag=flag)

@app.route('/create', methods=["POST"])
def create():
    return '@Route CREATE Table'

@app.route('/insert', methods=["POST"])
def insert():

    tbl='COMPANY_DOCUMENT_LIST'
    document_num, comp_id, category, document_name, company_deploy, from_save_date, disposal_date, remark=0, 1, request.form["category"], request.form["document_name"],request.form["company_deploy"], request.form["from_save_date"], request.form["disposal_date"], request.form["remark"]
    
    conn=sqlite3.connect(db_name)
    count=conn.cursor()
    sql=f'SELECT MAX(document_num) from {tbl};'
    count.execute(sql)
    for r in count:
        document_num=r[0]+1

    # SQL Insert
    sql=f'INSERT INTO {tbl} VALUES (?,?,?,?,?,?,?,?);'
    cursor=conn.cursor()
    cursor.execute(sql, (document_num, comp_id, category, document_name, company_deploy, from_save_date, disposal_date, remark))
    conn.commit()
    conn.close()
    return redirect('/')


@app.route('/update', methods=["POST"])
def update():
    return 'Route @UPDATE'

@app.route('/delete', methods=["POST"])
def delete():
    tbl='COMPANY_DOCUMENT_LIST'
    document_num=request.form['document_num']
    sql=f'DELETE FROM {tbl} WHERE document_num=?;'

    conn=sqlite3.connect(db_name)
    deletes=conn.cursor()
    deletes.execute(sql, (document_num,))
    
    conn.commit()
    conn.close()

    return redirect('/')

@app.route('/search', methods=["POST"])
def search():
    flag='search'
    tbl='COMPANY_DOCUMENT_LIST'
    forms=sanitize(request.form)
    word=forms['search_word']
    word=f'%{word}%'
    print(word)
    sql=f'SELECT * from {tbl} WHERE document_name LIKE ? OR company_deploy LIKE ? OR category LIKE ?;'
    
    conn=sqlite3.connect(db_name)
    cursor=conn.cursor()
    cursor.execute(sql, (word, word, word))

    items=cursor.fetchall()
    print(items)
    return render_template(
    'main.html',
    items=items, page_title=page_title, flag=flag)


if __name__=='__main__':
    app.run(port=port, debug=debug)
