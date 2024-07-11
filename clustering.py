import pandas as pd
from sklearn.cluster import KMeans
import numpy as np

def load_data(file_path):
    # Load data from CSV
    df = pd.read_csv(file_path)
    return df

def perform_clustering(data, num_clusters):
    # Assuming the data has columns 'customer_id', 'purchase_amount', and 'frequency'
    features = data[['purchase_amount', 'frequency']].values
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(features)
    data['cluster'] = kmeans.labels_
    clusters = data.groupby('cluster').mean().reset_index()
    centers = kmeans.cluster_centers_
    
    return data, centers
