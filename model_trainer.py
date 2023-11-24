import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the pickle and unpack it back into the dictionary
landmark_coord_dict = pickle.load(open('./data.pickle', 'rb'))
# Separate the landmark coordinates and labels while converting into array
landmark_coord = np.asarray(landmark_coord_dict['data'])
labels = np.asarray(landmark_coord_dict['labels'])
# Prepare training set and testing set. Here 25% of the data is reserved for testing
landmark_coord_train, landmark_coord_test, labels_train, labels_test = train_test_split(landmark_coord, labels,
                                                                                        test_size=0.25, shuffle=True,
                                                                                        stratify=labels)
# We will be using Random Forest Classifier for its high accuracy, efficiency for this large dataset, and doesn't
# over fit
model = RandomForestClassifier()
model.fit(landmark_coord_train, labels_train)
# Test the generated model
predicted_labels = model.predict(landmark_coord_test)
# Calculate the accuracy of the generated model
score = accuracy_score(predicted_labels, labels_test)
print('%.2f of samples were classified correctly !' % (score * 100))

# Save the model as a pickle-rick!
f = open('model.pickle', 'wb')
pickle.dump(model, f)
f.close()
