from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

# The home page route
@app.route('/')
def home():
    return render_template('home.html')

# The crop monitoring page route
@app.route('/monitor', methods=['GET', 'POST'])
def monitor():
    if request.method == 'POST':
        # Read the uploaded CSV file
        file = request.files['inputfile']
        df = pd.read_csv(file)

        # Generate a line plot for the temperature and humidity data
        fig, ax = plt.subplots()
        ax.plot(df['date'], df['temperature'], label='Temperature')
        ax.plot(df['date'], df['humidity'], label='Humidity')
        ax.legend()
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title('Crop Monitoring')
        plt.grid(True)

        # Save the plot to a PNG file and display it on the web page
        plt.savefig('static/plot.png')
        return render_template('monitor.html', plot='plot.png')
    else:
        return render_template('monitor.html')

if __name__ == '__main__':
    app.run(debug=True)
