from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import mysql.connector as mydb

conn = mydb.Connect(
    host='localhost',
    port='3306',
    user='root',
    password='pong0530',
    database='visualization'
)
cur = conn.cursor()

def signup(request):
    return render(request, 'signup.html')

def complete(request):
    if request.method == 'POST':
        u_id = str(request.POST.get('user_id'))
        ps = str(request.POST.get('password'))
        df = pd.DataFrame({
            'user_name': [u_id],
            'password': [ps]
        })
        print(df)
        df2 = df
        df2['authority'] = 1
        df3 = "'"+df2['user_name'].iloc[-1]+"'"
        df4 = "'"+df2['password'].iloc[-1]+"'"
        df5 = df2['authority'].iloc[-1]
        cur.execute("INSERT INTO li_id (user_name)"
                    f" VALUES ({df3})")
        conn.commit()
        cur.execute("INSERT INTO li_ps (password)"
                    f" VALUES ({df4})")
        conn.commit()
        cur.execute("INSERT INTO li_auth (authority)"
                    f" VALUES ({df5})")
        conn.commit()
        return render(request, 'complete.html')
    else:
        return render(request, 'complete.html')