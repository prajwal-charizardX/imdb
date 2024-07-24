from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load the Excel file to get the sheet names
    file_path = 'IMDB-Movie-Database.xlsx'
    xls = pd.ExcelFile(file_path)
    sheet_names = xls.sheet_names
    return render_template('index.html', sheet_names=sheet_names)

@app.route('/scrape', methods=['POST'])
def scrape():
    file_path = 'IMDB-Movie-Database.xlsx'
    sheet_name = request.form.get('sheet_name')
    search_value = request.form.get('search_value')

    df = pd.read_excel(file_path, sheet_name=sheet_name)

    if search_value:
        df = df[df.apply(lambda row: row.astype(str).str.contains(search_value, case=False).any(), axis=1)]

    html_table = df.to_html(classes='table table-striped table-dark', index=False)
    
    return render_template('data.html', table=html_table, sheet_name=sheet_name, search_value=search_value)

if __name__ == '__main__':
    app.run(debug=True)
