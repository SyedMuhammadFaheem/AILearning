from pomegranate import *

age = Node(DiscreteDistribution({'<40': 0.333, '40-60': 0.333, '>60': 0.334}), name='age')
hd = Node(DiscreteDistribution({'No': 0.6, 'Yes': 0.4}), name='hd')
chol = Node(DiscreteDistribution({'High': 0.35, 'Normal': 0.65}), name='chol')

ageHdChol = ConditionalProbabilityTable(
    [        ['<40', 'No', 'High', 0.6],
        ['<40', 'No', 'High', 'Normal', 0.2],
        ['<40', 'No', 'High', 'High', 0.2],
        ['<40', 'No', 'Normal', 'Normal', 0.2],
        ['<40', 'No', 'Normal', 'High', 0.2],
        ['<40', 'No', 'High', 'Normal', 0.2],
        ['<40', 'No', 'High', 'High', 0.2],
        ['<40', 'Yes', 'High', 0.4],
        ['<40', 'No', 'Normal', 0.2],
        ['<40', 'Yes', 'Normal', 0.8],
        ['40-60', 'No', 'High', 0.25],
        ['40-60', 'Yes', 'High', 0.75],
        ['40-60', 'No', 'Normal', 0.5],
        ['40-60', 'Yes', 'Normal', 0.5],
        ['>60', 'No', 'High', 0.4],
        ['>60', 'Yes', 'High', 0.6],
        ['>60', 'No', 'Normal', 0.7],
        ['>60', 'Yes', 'Normal', 0.3]
    ],
    [age.distribution, hd.distribution, chol.distribution]
)


ageHdCholNode = Node(ageHdChol, name='ageHdChol')

model = BayesianNetwork('Heart Disease Prediction')
model.add_states(age, hd, chol, ageHdCholNode)

model.add_edge(age, ageHdCholNode)
model.add_edge(hd, ageHdCholNode)
model.add_edge(chol, ageHdCholNode)

model.bake()
# print(ageHdChol.keys())

probHdGivenAgeChol = model.predict_proba({'age': '<40', 'chol': 'High'})[1].parameters[0]['Yes']
print(f"Conditional probability of heart disease given age=<40 and cholesterol=High: {probHdGivenAgeChol:.2f}")
