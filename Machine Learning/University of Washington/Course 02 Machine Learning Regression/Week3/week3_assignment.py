# -*- coding: utf-8 -*-
"""Week3 Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JM0rirns26gbM-BFzqTCkYoXOfLyBxyv
"""

!pip install turicreate

import turicreate
from turicreate import SFrame
import numpy as np

"""1. You’re going to write a function that adds powers of a feature to columns of a data frame. For those using SFrames:

Recall that if we have an SArray ‘tmp’ we can get a new SArray with all the values to the third power with:
"""

tmp = turicreate.SArray([1., 2., 3.])
tmp_cubed = tmp.apply(lambda x: x**3)
print(tmp)
print(tmp_cubed)

"""We can create an empty SFrame with:"""

my_SFrame = turicreate.SFrame()

"""And append the tmp to it with:"""

my_SFrame['power_1'] = tmp
print(my_SFrame)

"""Where here ‘power_1’ will refer to the power our feature was raised to.

2. Write your own function called ‘polynomial_sframe’ (or otherwise) which accepts an array ‘feature’ and a maximal ‘degree’ and returns an data frame (e.g. SFrame) with the first column equal to ‘feature’ and the remaining columns equal to ‘feature’ to increasing integer powers up to ‘degree’.

e.g. if you’re using SFrames, you can complete the following function:

    def polynomial_sframe(feature, degree):
        # assume that degree >= 1
        # initialize the SFrame:
        poly_sframe = turicreate.SFrame()
        # and set poly_sframe['power_1'] equal to the passed feature
        ...
        # first check if degree > 1
        if degree > 1:
            # then loop over the remaining degrees:
            for power in range(2, degree+1):
                # first we'll give the column a name:
                name = 'power_' + str(power)
                # assign poly_sframe[name] to be feature^power
                ...
        return poly_sframe
"""

import math

def polynomial_sframe(feature, degree):
    # assume that degree >= 1
    # initialize the SFrame:
    poly_sframe = turicreate.SFrame()
    # and set poly_sframe['power_1'] equal to the passed feature
    poly_sframe['power_1'] = feature
    # first check if degree > 1
    if degree > 1:
        # then loop over the remaining degrees:
        for power in range(2, degree+1):
            # first we'll give the column a name:
            name = 'power_' + str(power)
            # assign poly_sframe[name] to be feature^power
            poly_sframe[name] = feature.apply(lambda x: x**power)
    return poly_sframe

print(polynomial_sframe(tmp, 3))

"""3. we will be working with the house Sales data as in the previous notebooks. Load in the data and also sort the sales SFrame by ‘sqft_living’. When we plot the fitted values we want to join them up in a line and this works best if the variable on the X-axis (which will be ‘sqft_living’) is sorted. For houses with identical square footage, we break the tie by their prices."""

sales = turicreate.SFrame('/content/drive/My Drive/Colab Notebooks/Machine Learning/Course 2 Machine Learning Regression/Week2/Assignment1/home_data.sframe')

sales = sales.sort(['sqft_living','price'])
sales

"""4. Make a 1 degree polynomial SFrame with sales[‘sqft_living’] as the the feature. Call it ‘poly1_data’.

5. Add sales[‘price’] to poly1_data as this will be our output variable. e.g. if you’re using SFrames

        poly1_data = polynomial_sframe(sales['sqft_living'], 1)
        poly1_data['price'] = sales['price']
"""

poly1_data = polynomial_sframe(sales['sqft_living'], 1)
poly1_data['price'] = sales['price']

"""6. Use `turicreate.linear_regression.create` (or another linear regression library) to compute the regression weights for predicting sales[‘price’] based on the 1 degree polynomial feature ‘sqft_living’. The result should be an intercept and slope. e.g if you’re using Turi Create:

        model1 = turicreate.linear_regression.create(poly1_data, 
                target = 'price',
                features = ['power_1'], validation_set = None)
  
If you use `turicreate.linear_regression.create()` to estimate these models please ensure that you set validation_set = None. This way you will get the same answer every time you run the code.
"""

model1 = turicreate.linear_regression.create(poly1_data, 
                                             target = 'price',
                                             features = ['power_1'],
                                             validation_set = None)

model1.coefficients

"""7. Next use the produce a scatter plot of the training data (just square feet vs price) and add the fitted model. e.g. with matplotlib and SFrames:

        import matplotlib.pyplot as plt
        %matplotlib inline
        plt.plot(poly1_data['power_1'],poly1_data['price'],'.',
        poly1_data['power_1'], model1.predict(poly1_data),'-')
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
plt.plot(poly1_data['power_1'],poly1_data['price'],'.',
         poly1_data['power_1'], model1.predict(poly1_data),'-')

"""8. Now that you have plotted the results using a 1st degree polynomial, try it again using a 2nd degree and 3rd degree polynomial. Look at the fitted lines, do they appear as you would expect?

###2nd degree polynomial
"""

poly2_data = polynomial_sframe(sales['sqft_living'], 2)

poly2_features = poly2_data.column_names() # get the name of the features
poly2_data['price'] = sales['price']

model2 = turicreate.linear_regression.create(poly2_data, 
                                             target = 'price',
                                             features = poly2_features,
                                             validation_set = None)

model2.coefficients

plt.plot(poly2_data['power_1'],poly2_data['price'],'.',
         poly2_data['power_1'], model2.predict(poly2_data),'-')

"""###3rd degree polynomial"""

poly3_data = polynomial_sframe(sales['sqft_living'], 3)

poly3_features = poly3_data.column_names() # get the name of the features
poly3_data['price'] = sales['price']

model3 = turicreate.linear_regression.create(poly3_data, 
                                             target = 'price',
                                             features = poly3_features,
                                             validation_set = None)

model3.coefficients

plt.plot(poly3_data['power_1'],poly3_data['price'],'.',
         poly3_data['power_1'], model3.predict(poly3_data),'-')

"""9. Now try a 15th degree polynomial. Print out the coefficients and look at the resulted fitted line. Do you think this degree is appropriate for these data? If we were to use a different subset of the data do you think we would get pretty much the same curve?

###15th degree curve
"""

poly15_data = polynomial_sframe(sales['sqft_living'], 15)

poly15_features = poly15_data.column_names() # get the name of the features
poly15_data['price'] = sales['price']

model15 = turicreate.linear_regression.create(poly15_data, 
                                             target = 'price',
                                             features = poly15_features,
                                             validation_set = None)

model15.coefficients

plt.plot(poly15_data['power_1'], poly15_data['price'], '.',
         poly15_data['power_1'], model15.predict(poly15_data), '-')

"""10. If you’re using SFrames then create four subsets as follows:

*   first split sales into 2 subsets with .random_split(.5) use seed = 0!
*   next split these into 2 more subsets (4 total) using random_split(0.5) again set seed = 0!
*   you should have 4 subsets of (approximately) equal size, call them set_1, set_2, set_3, and set_4
"""

set1_1, set2_2 = sales.random_split(.5, seed=0)
set1, set2 = set1_1.random_split(.5, seed=0)
set3, set4 = set2_2.random_split(.5, seed=0)

"""11. Estimate a 15th degree polynomial on all 4 sets, plot the results and view the coefficients for all four models."""

set1_data = polynomial_sframe(set1['sqft_living'], 15)
set1_features = set1_data.column_names() # get the name of the features
set1_data['price'] = set1['price']
set1_model = turicreate.linear_regression.create(set1_data, 
                                             target = 'price',
                                             features = set1_features,
                                             validation_set = None)
set1_model.coefficients.print_rows(num_rows=16)
plt.plot(set1_data['power_1'], set1_data['price'], '.', set1_data['power_1'], set1_model.predict(set1_data), '-')

set2_data = polynomial_sframe(set2['sqft_living'], 15)
set2_features = set2_data.column_names() # get the name of the features
set2_data['price'] = set2['price']
set2_model = turicreate.linear_regression.create(set2_data, 
                                             target = 'price',
                                             features = set2_features,
                                             validation_set = None)
set2_model.coefficients.print_rows(num_rows=16)
plt.plot(set2_data['power_1'], set2_data['price'], '.', set2_data['power_1'], set2_model.predict(set2_data), '-')

set3_data = polynomial_sframe(set3['sqft_living'], 15)
set3_features = set3_data.column_names() # get the name of the features
set3_data['price'] = set3['price']
set3_model = turicreate.linear_regression.create(set3_data, 
                                             target = 'price',
                                             features = set3_features,
                                             validation_set = None)
set3_model.coefficients.print_rows(num_rows=16)
plt.plot(set3_data['power_1'], set3_data['price'], '.', set3_data['power_1'], set3_model.predict(set3_data), '-')

set4_data = polynomial_sframe(set4['sqft_living'], 15)
set4_features = set4_data.column_names() # get the name of the features
set4_data['price'] = set4['price']
set4_model = turicreate.linear_regression.create(set4_data, 
                                             target = 'price',
                                             features = set4_features,
                                             validation_set = None)
set4_model.coefficients.print_rows(num_rows=16)
plt.plot(set4_data['power_1'], set4_data['price'], '.', set4_data['power_1'], set4_model.predict(set4_data), '-')

"""#12. **Quiz Question:** Is the sign (positive or negative) for power_15 the same in all four models?

#13. **Quiz Question:** True/False the plotted fitted lines look the same in all four plots : False

14. Since the “best” polynomial degree is unknown to us we will use cross validation to select the best degree. If you’re using SFrames then create a training, validation and testing subsets as follows:

First split sales into training_and_validation and testing with sales.random_split(0.9) use seed = 1!

Next split training_and_validation into training and validation using .random_split(0.5) use seed = 1!
"""

training_and_validation, test = sales.random_split(.9, seed=1)
training, validation = training_and_validation.random_split(.5, seed=1)

"""15. Now for each degree from 1 to 15:


*   Build an polynomial data set using training_data[‘sqft_living’] as the feature and the current degree

*   Add training_data[‘price’] as a column to your polynomial data set

*   Learn a model on TRAINING data to predict ‘price’ based on your polynomial data set at the current degree

*   Compute the RSS on VALIDATION for the current model (print or save the RSS)

Hint: in turicreate.linear_regression.create() you can set verbose = False if you want to suppress the interim output of linear_regression.create().
"""

for i in range(1,16):
  poly_data = polynomial_sframe(training['sqft_living'], i)
  my_features = poly_data.column_names()
  poly_data['price'] = training['price']
  model = turicreate.linear_regression.create(poly_data,
                                              target = 'price',
                                              features = my_features,
                                              validation_set = None,
                                              verbose = False)
  
  validation_data = polynomial_sframe(validation['sqft_living'], i)
  validation_data['price'] = validation['price']
  predictions = model.predict(validation_data)
  RSS = ((predictions - validation_data['price']) * (predictions - validation_data['price'])).sum()
  print(str(RSS))
  #print(model.evaluate)

"""#16. **Quiz Question:** Which degree (1, 2, …, 15) had the lowest RSS on Validation data?

6th

17. Now that you have selected a degree compute the RSS on TEST data for the model with the best degree from the Validation data.
"""

train_data = polynomial_sframe(training['sqft_living'], 6)
train_features = train_data.column_names()
train_data['price'] = training['price']
model = turicreate.linear_regression.create(train_data, 
                                          target = 'price', 
                                          features = train_features, 
                                          validation_set = None, 
                                          verbose=False)

test_data = polynomial_sframe(test['sqft_living'], 6)
test_data['price'] = test['price'] 

# First get the predictions
predictions = model.predict(test_data)
# then compute the residuals (since we are squaring it doesn't matter which order you subtract)
residuals = test_data['price'] - predictions
# square the residuals and add them up
residuals_squared = residuals * residuals
RSS = residuals_squared.sum()
print("Degree: %s, Test Data RSS: $%.6f" % (6, RSS))

"""#18. **Quiz Question:** what is the RSS on TEST data for the model with the degree selected from Validation data?"""



