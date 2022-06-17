from flask import Flask,redirect,url_for,request,render_template

import pandas as pd


app=Flask(__name__)

@app.route('/newbill',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['nm']
        price=request.form['price']
        dict1={'item':[user],'price':[price]}
        df=pd.read_csv(r"items.csv",index_col=0)
        ind = df.tail(1).index
        df.loc[ind[0] + 1] = [user,price]
        print(df)
        df.to_csv('/Users/rekha/Documents/items.csv')
        return (render_template('user.html', name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success',name=user))
if __name__=='__main__':
    app.run(debug=True)
