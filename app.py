from flask import Flask, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    # Load the Excel file
    file_path = '/mnt/data/IMDB-Movie-Database.xlsx'
    df = pd.read_excel(file_path)

    # Save the DataFrame as HTML
    html_table = df.to_html(classes='table table-striped', index=False)
    
    return render_template('data.html', table=html_table)

if __name__ == '__main__':
    app.run(debug=True)
