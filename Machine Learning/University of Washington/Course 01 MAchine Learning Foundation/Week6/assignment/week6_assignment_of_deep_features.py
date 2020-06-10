# -*- coding: utf-8 -*-
"""Week6_assignment of Deep Features.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xf64mU-1E8qYARHUuUsfXJZvkBG1WOxU
"""

!pip install turicreate

import turicreate

"""# **Load a comman image analysis dataset**"""

image_train = turicreate.SFrame('/content/drive/My Drive/Colab Notebooks/Machine Learning/Week6/Practice/image_train_data/')
image_test = turicreate.SFrame('/content/drive/My Drive/Colab Notebooks/Machine Learning/Week6/Practice/image_test_data/')

"""# **Train a nearest-neighbour model for retrieving images using deep featres**"""

knn_model = turicreate.nearest_neighbors.create(image_train,
                                                features=['deep_features'],
                                                label = 'id')

"""# **Task 1: Compute summary statistics of the data**
Sketch summaries are techniques for computing summary statistics of data very quickly. In GraphLab Create, SFrames and SArrays include a method:

.sketch_summary()
which computes such summary statistics. Using the training data, compute the sketch summary of the ‘label’ column and interpret the results. What’s the least common category in the training data?
"""

sketch = turicreate.Sketch(image_train['label'])

sketch_summary = image_train['label'].summary()

sketch_summary

"""# **Task 2: Create category-specific image retrieval models**
In most retrieval tasks, the data we have is unlabeled, thus we call these unsupervised learning problems. However, we have labels in this image dataset, and will use these to create one model for each of the 4 image categories, {‘dog’,’cat’,’automobile’,bird’}. To start, follow these steps:


Similarly to the image retrieval notebook you downloaded, you are going to create a nearest neighbor model using the 'deep_features' as the features, but this time create one such model for each category, using the training_data. You can call the model with the ‘dog’ data the dog_model, the one with the ‘cat’ data the cat_model, as so on. You now have a nearest neighbors model that can find the nearest ‘dog’ to any image you give it, the dog_model; one that can find the nearest ‘cat’, the cat_model; and so on.


*   Split the SFrame with the training data into 4 different SFrames. Each of these will contain data for 1 of the 4 categories above. Hint: if you use a logical filter to select the rows where the ‘label’ column equals ‘dog’, you can create an SFrame with only the data for images labeled ‘dog’.

*   Similarly to the image retrieval notebook you downloaded, you are going to create a nearest neighbor model using the 'deep_features' as the features, but this time create one such model for each category, using the training_data. You can call the model with the ‘dog’ data the dog_model, the one with the ‘cat’ data the cat_model, as so on. You now have a nearest neighbors model that can find the nearest ‘dog’ to any image you give it, the dog_model; one that can find the nearest ‘cat’, the cat_model; and so on.


Using these models, answer the following questions. The cat image below is the first in the test data

You can access this image, similarly to what we did in the iPython notebooks above, with this command:

    image_test[0:1]
 
  What is the nearest ‘cat’ labeled image in the training data to the cat image above (the first image in the test data)?

### **a) Split training data into 4 different categories**
"""

automobile = image_train.filter_by(['automobile'],'label')
cat = image_train.filter_by(['cat'],'label')
dog = image_train.filter_by(['dog'],'label')
bird = image_train.filter_by(['bird'],'label')

"""### **b) Create nearest neighbor model for each category**"""

automobile_model  = turicreate.nearest_neighbors.create(automobile, features=['deep_features'],
                                                     label='id')

cat_model  = turicreate.nearest_neighbors.create(cat, features=['deep_features'],
                                                     label='id')

dog_model  = turicreate.nearest_neighbors.create(dog, features=['deep_features'],
                                                     label='id')

bird_model  = turicreate.nearest_neighbors.create(bird, features=['deep_features'],
                                                     label='id')

image_test['image'][0:1].explore()

cat_model.query(image_test[0:1])

def get_images_from_ids(query_result):
    return image_train.filter_by(query_result['reference_label'],'id')

"""**What is the nearest ‘cat’ labeled image in the training data to the cat image above (the first image in the test data)?**"""

cat_image = image_train[image_train['id']==16289]
cat_image['image'].explore()

get_images_from_ids(cat_model.query(image_test[0:1]))['image'].explore()

"""**What is the nearest ‘dog’ labeled image in the training data to the cat image above (the first image in the test data)?**"""

dog_model.query(image_test[0:1])

dog_image = image_train[image_train['id']==16976]
dog_image['image'].explore()

get_images_from_ids(dog_model.query(image_test[0:1]))['image'].explore()

"""# **Task 3: Try a simple example of nearest-neighbors classification**

When we queried a nearest neighbors model, the ‘distance’ column in the table above shows the computed distance between the input and each of the retrieved neighbors. In this question, you will use these distances to perform a classification task, using the idea of a nearest-neighbors classifier.



*   For the first image in the test data (image_test[0:1]), 
which we used above, compute the mean distance between this image at its 5 nearest neighbors that were labeled ‘cat’ in the training data (similarly to what you did in the previous question). Save this result.

*   Similarly, for the first image in the test data (image_test[0:1]), which we used above, compute the mean distance between this image at its 5 nearest neighbors that were labeled ‘dog’ in the training data (similarly to what you did in the previous question). Save this result.

*   On average, is the first image in the test data closer  to its 5 nearest neighbors in the ‘cat’ data or in the ‘dog’ data? (In a later course, we will see that this is an example of what is called a k-nearest neighbors classifier, where we use the label of neighboring points to predict the label of a test point.)
"""

cat_model.query(image_test[0:1])['distance'].mean()

dog_model.query(image_test[0:1])['distance'].mean()

"""# **Task 4: Compute nearest neighbors accuracy**
A nearest neighbor classifier predicts the label of a point as the most common label of its nearest neighbors. In this question, we will measure the accuracy of a 1-nearest-neighbor classifier, i.e., predict the output as the label of the nearest neighbor in the training data. Although there are simpler ways of computing this result, we will go step-by-step here to introduce you to more concepts in nearest neighbors and SFrames, which will be useful later in this Specialization.



*   Training models: For this question, you will need the nearest neighbors models you learned above on the training data, i.e., the dog_model, cat_model, automobile_model and bird_model.

*   Spliting test data by label: Above, you split the train data SFrame into one SFrame for images labeled ‘dog’, another for those labeled ‘cat’, etc. Now, do the same for the test data. You can call the resulting SFrames



    image_test_cat, image_test_dog, image_test_bird, image_test_automobile
"""

image_test_automobile = image_test.filter_by(['automobile'],'label')
image_test_cat = image_test.filter_by(['cat'],'label')
image_test_dog = image_test.filter_by(['dog'],'label')
image_test_bird = image_test.filter_by(['bird'],'label')

"""Finding nearest neighbors in the training set for each part of the test set: Thus far, we have queried, 
    
      e.g. dog_model.query()

our nearest neighbors models with a single image as the input, but you can actually query with a whole set of data, and it will find the nearest neighbors for each data point. Note that the input index will be stored in the ‘query_label’ column of the output SFrame.

Using this knowledge find the closest neighbor in to the dog test data using each of the trained models, 
     
     e.g. dog_cat_neighbors = cat_model.query(image_test_dog, k=1)

finds 1 neighbor (that’s what k=1 does) to the dog test images (image_test_dog) in the cat portion of the training data (used to train the cat_model).

Now, do this for every combination of the labels in the training and test data.



*   Create an SFrame with the distances from ‘dog’ test examples to the respective nearest neighbors in each class in the training data: The ‘distance’ column in dog_cat_neighbors above contains the distance between each ‘dog’ image in the test set and its nearest ‘cat’ image in the training set. The question we want to answer is how many of the test set ‘dog’ images are closer to a ‘dog’ in the training set than to a ‘cat’, ‘automobile’ or ‘bird’. So, next we will create an SFrame containing just these distances per data point. The goal is to create an SFrame called dog_distances with 4 columns:



1. dog_distances[‘dog-dog’] ---- storing dog_dog_neighbors[‘distance’]

2. dog_distances[‘dog-cat’] ---- storing dog_cat_neighbors[‘distance’]

3. dog_distances[‘dog-automobile’] ---- storing dog_automobile_neighbors[‘distance’]

4. dog_distances[‘dog-bird’] ---- storing dog_bird_neighbors[‘distance’]
"""

dog_cat_neighbors = cat_model.query(image_test_dog, k=1)

dog_dog_neighbors = dog_model.query(image_test_dog, k=1)

dog_automobile_neighbors = automobile_model.query(image_test_dog, k=1)

dog_bird_neighbors = bird_model.query(image_test_dog, k=1)

"""### Compute Dog distances"""

dog_distances = turicreate.SFrame({'dog_automobile': dog_automobile_neighbors['distance'],
                              'dog_bird': dog_bird_neighbors['distance'],
                              'dog_cat': dog_cat_neighbors['distance'],
                              'dog_dog': dog_dog_neighbors['distance']
                             })

dog_distances.head()

"""Computing the number of correct predictions using 1-nearest neighbors for the dog class: Now that you have created the SFrame dog_distances, you will learn to use the method
    
    .apply()
on this SFrame to iterate line by line and compute the number of ‘dog’ test examples where the distance to the nearest ‘dog’ was lower than that to the other classes. You will do this in three steps:

i. Consider one row of the SFrame dog_distances. Let’s call this variable row. You can access each distance by calling, for example,

    row[‘dog_cat’]

which, in example table above, will have value equal to 36.4196077068 for the first row.

Create a function starting with

    def is_dog_correct(row):

which returns 1 if the value for row[‘dog_dog’] is lower than that of the other columns, and 0 otherwise. That is, returns 1 if this row is correctly classified by 1-nearest neighbors, and 0 otherwise.
"""

def is_dog_correct(row):
  if row['dog_dog'] <= min(row.values()):
    return 1
  else:
    return 0

"""2. Using the function is_dog_correct(row), you can check if 1 row is correctly classified. Now, you want to count how many rows are correctly classified. You could do a for loop iterating through each row and applying the function is_dog_correct(row). This method will be really slow, because the SFrame is not optimized for this type of operation.

Instead, we will use the  **.apply()** method to iterate the function is_dog_correct for each row of the SFrame.

  3. Computing the number of correct predictions for ‘dog’: You can now call:

    **dog_distances.apply(is_dog_correct)**

which will return an SArray (a column of data) with a 1 for every correct row and a 0 for every incorrect one.et?
"""

dog_distances.apply(is_dog_correct)

"""You can call:

    .sum()

on the result to get the total number of correctly classified ‘dog’ images in the test set!
"""

dog_distances.apply(is_dog_correct).sum()

"""**Hint:** To make sure your code is working correctly, if you were to do steps 1) and 2) in this question to count the number of correctly classified ‘cat’ images in the test data, instead of ‘dog’, the result would be 548."""

cat_distances = turicreate.SFrame({'cat_automobile': automobile_model.query(image_test_cat, k=1)['distance'],
                                 'cat_bird': bird_model.query(image_test_cat, k=1)['distance'],
                                 'cat_cat': cat_model.query(image_test_cat, k=1)['distance'],
                                 'cat_dog': dog_model.query(image_test_cat, k=1)['distance'],
                                })

def is_cat_correct(row):  
    if row['cat_cat'] <= min(row.values()):     
        return 1    
    else:        
        return 0

cat_distances.apply(is_cat_correct).sum()

"""### Accuracy of the dog_test_data"""

dog_distances.apply(is_dog_correct).sum()/len(dog_distances)

