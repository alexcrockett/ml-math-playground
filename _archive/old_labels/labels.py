# Import libraries
import sys
import os
import numpy as np
import pandas as pd
from scipy.stats import norm

# Import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import files
from suds.sud.data.format import training_data as td01
from suds.sud.data.format.training_data import import_fu, batch_all_values

# Retrieve formatted data
formatted_data = import_fu()

all_batches = []
for data in formatted_data:
	batches = batch_all_values(data)
	all_batches.append(batches)

# Function to get a specific batch for a specific stock
def get_specific_batch(stock_index, batch_number):
	try:
		return all_batches[stock_index][batch_number]
	except IndexError:
		print("Invalid stock index or batch number")
		return None

def label_calc(index, batch):
	batch_data = get_specific_batch(index, batch)  # Get the specific batch data
	values_signs = np.sign(batch_data)  # Calculate the sign of the data values
	mean_values = np.mean(batch_data, axis=0)  # Calculate mean
	std_values = np.std(batch_data, axis=0)  # Calculate the standard deviation
	z_data = (batch_data - mean_values) / std_values  # Compute z-scores (standard scores) for the data
	probability_values = norm.cdf(z_data)  # Convert z-scores to probabilities using the CDF of the normal distribution
	labeled_data = probability_values * values_signs # Multiply by the sign to retain direction
	return labeled_data