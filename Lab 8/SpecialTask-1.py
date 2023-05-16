from pomegranate import *
from node import *
studyTime = Node(DiscreteDistribution({'Low': 0.2, 'Medium': 0.5, 'High': 0.3}), name='studyTime')
examScore = Node(ConditionalProbabilityTable([
    ['Low', 'Low', 0.3],
    ['Low', 'Medium', 0.4],
    ['Low', 'High', 0.3],
    ['Medium', 'Low', 0.2],
    ['Medium', 'Medium', 0.5],
    ['Medium', 'High', 0.3],
    ['High', 'Low', 0.1],
    ['High', 'Medium', 0.3],
    ['High', 'High', 0.6],
], [studyTime.distribution]), name='examScore')
passFinalExam = Node(ConditionalProbabilityTable([
    ['Low', True, 0.1],
    ['Low', False, 0.9],
    ['Medium', True, 0.4],
    ['Medium', False, 0.6],
    ['High', True, 0.9],
    ['High', False, 0.1],
], [examScore.distribution]), name='passFinalExam')

model = BayesianNetwork('Passing Final Exam Prediction')
model.add_states(studyTime, examScore, passFinalExam)

model.add_edge(studyTime, examScore)
model.add_edge(examScore, passFinalExam)

model.bake()

mediumScoreGivenHighTime = model.predict_proba({'studyTime': 'High'})[1].parameters[0]['Medium']
print("Probability of getting a medium exam score given high study time:",mediumScoreGivenHighTime)

passGivenMediumScore = model.predict_proba({'examScore': 'Medium'})[2].parameters[0][True]
print("Probability of passing the final exam given a medium exam score:",passGivenMediumScore)
