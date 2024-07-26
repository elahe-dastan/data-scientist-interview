# Classifying monsters 
#
# You need to classify monsters into being Ghosts, Goblins, or Ghouls
#
# Data
#  * CSV file available at /home/coderpad/data/monsters.csv
#
# Data files contains the following fields
#  * id - id of the creature
#  * bone_length - average length of bone in the creature, normalized between 0 and 1
#  * rotting_flesh - percentage of rotting flesh in the creature
#  * hair_length - average hair length, normalized between 0 and 1
#  * has_soul - percentage of soul in the creature
#  * color - dominant color of the creature: 'white','black','clear','blue','green','blood'
#  * type - target variable: 'Ghost', 'Goblin', and 'Ghoul'
#
# Available libraries: numpy, scipy, pandas, scikit-learn, and statsmodels

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder


data_file_path = '/home/coderpad/data/monsters.csv'


df = pd.read_csv(data_file_path)
enc = OrdinalEncoder()
df[['color', 'type']] = enc.fit_transform(df[['color', 'type']])

X = df[['bone_length', 'rotting_flesh', 'hair_length', 'has_soul', 'color']]
y = df['type']


rfc = RandomForestClassifier()
rfc.fit(X, y)

rfc.pre



# lines = []
# with open(data_file_path) as f:
#     lines = f.readlines()

# print(lines)
