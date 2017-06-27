# blend.py
# Description: Linear blend to find optimal alpha vector
# Author: Tristan Nee
# Date: 25/27/2017

import numpy as np
import sys

print('Loading in file predictions.dta...')
pred = np.loadtxt('predictions.dta') # NxM matrix of predictions
predT = np.matrix.transpose(pred) # Compute transpose for later computations

N = np.shape(pred)[0] # Amount of ratings predicted in each predictor (2749898)
M = np.shape(pred)[1] # Amount of predictors
num_quiz = 1408342 # Number of points in quiz

# Sum of s_k^2 values obtained from the RMSE of submitting
# a solution of all zeros.
SE0 = (3.84358**2)*N;

# Results of SE values for each model. We must manually adjust the SEs array
# based on the amount of models and their respective RMSE scores.
RMSEs = [0.91622, 0.91566] # RMSE values from each model

if len(RMSEs) != M:
	print('Error: Length of RMSEs array must equal amount of models '
		'in predictions.dta')
	sys.exit(0)

SEs = list(map(lambda x : x * x * N, RMSEs))

ATs = np.zeros(M) # The A^Ts matrix

print('Blending results...')
for i in range(M):
	ATs[i] = .5*(sum(map(lambda x : x * x, pred[:, i])) + SE0 - SEs[i])

alpha = np.matmul(np.linalg.inv(np.matmul(predT, pred)), ATs)
print("Alpha vector below:")
print(alpha)
new_ratings = np.matmul(pred, alpha)

# Write our results to file
print('Writing results to file results_blended.dta...')
np.savetxt('results_blended.dta', new_ratings)