from flask import Flask, render_template
import csv

app = Flask(__name__, template_folder='/Users/hb/Documents/demoWebsite/templates')

def load_data():
    data = {}
    with open('/Users/hb/Documents/demoWebsite/fixed.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            city, title, articleContent, time, issue, solution = row
            if city not in data:
                data[city] = []
            data[city].append({'issue': issue, 'solution': solution})
    return data

city_data = load_data()

@app.route('/')
def index():
    return render_template('index.html', cities=city_data.keys())


@app.route('/get_issues/<city>')
def get_issues(city):
    issues = city_data.get(city, [])
    return {'issues': issues}

if __name__ == '__main__':
    app.run(debug=True)
