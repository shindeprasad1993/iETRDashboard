from flask import Flask, render_template, request, jsonify
import pandas as pd
app = Flask(__name__)


@app.route("/")
def table():
    df = pd.read_csv("DMS_A_OUTAGE_REPAIR.csv")
    records = df.to_records(index=False)
    data = list(records)
    headings = list(df.columns)
    return render_template('table.html', headings=headings, data=data)

@app.route("/update",methods=["POST","GET"])
def update():
    try:
        if request.method == 'POST':
            field = request.form['field'] 
            value = request.form['value']
            editid = request.form.get('id', type=int)

            df = pd.read_csv("DMS_A_OUTAGE_REPAIR.csv")
            df.reset_index()
            idx = df.index[df['OUTAGE_NO'] == editid].tolist()

            df.loc[idx[0],field] = value

            df.to_csv("DMS_A_OUTAGE_REPAIR.csv", index=False)
            print('CSV data updated')

            records = df.to_records(index=False)
            data = list(records)
            headings = list(df.columns)
 
            success = 1
        return render_template('table.html', headings=headings, data=data)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    app.run()
