from pomegranate import *


ageHdChol = ConditionalProbabilityTable(
    [['<40', 'No', 'High', 100],
     ['<40', 'Yes', 'High', 150],
     ['40-60', 'No', 'High', 150],
     ['40-60', 'Yes', 'High', 255],
     ['>60', 'No', 'High', 150],
     ['>60', 'Yes', 'High', 250],
     ['<40', 'No', 'Normal', 150],
     ['<40', 'Yes', 'Normal', 100],
     ['40-60', 'No', 'Normal', 200],
     ['40-60', 'Yes', 'Normal', 240],
     ['>60', 'No', 'Normal', 200],
     ['>60', 'Yes', 'Normal', 210]],
    [age.distribution, hd.distribution, chol.distribution]
)

age = Node(DiscreteDistribution({'<40': 0.333, '40-60': 0.333, '>60': 0.334}), name='age')
hd = Node(DiscreteDistribution({'No': 0.6, 'Yes': 0.4}), name='hd')
chol = Node(DiscreteDistribution({'High': 0.35, 'Normal': 0.65}), name='chol')

ageHdCholNode = Node(age_hd_chol, name='ageHdChol')

model = BayesianNetwork('Heart Disease Prediction')
model.add_states(age, hd, chol, ageHdCholNode)

model.add_edge(age, ageHdCholNode)
model.add_edge(hd, ageHdCholNode)
model.add_edge(chol, ageHdCholNode)

model.bake()

probHdGivenAgeChol = model.predict_proba({'age': '<40', 'chol': 'High'})[1].parameters[0]['Yes']
print(f"Conditional probability of heart disease given age=<40 and cholesterol=High: {probHdGivenAgeChol:.2f}")
