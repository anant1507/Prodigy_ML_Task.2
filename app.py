from flask import Flask, request, render_template, redirect, url_for
from clustering import perform_clustering, load_data

app = Flask(__name__)

# Load the data
data_file = 'data/purchase_data.csv'
data = load_data(data_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cluster', methods=['POST'])
def cluster():
    # Get the number of clusters from the form
    num_clusters = int(request.form.get('num_clusters', 3))
    
    # Perform clustering
    clusters, centers = perform_clustering(data, num_clusters)
    
    # Render results
    return render_template('results.html', clusters=clusters, centers=centers)

if __name__ == '__main__':
    app.run(debug=True)
