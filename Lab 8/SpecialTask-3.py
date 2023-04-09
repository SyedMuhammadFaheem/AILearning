from pomegranate import *


cpuUsage = Node(DiscreteDistribution({'low': 0.3, 'med': 0.5, 'high': 0.2}), name='cpuUsage')
memUsage = Node(DiscreteDistribution({'low': 0.3, 'med': 0.5, 'high': 0.2}), name='memUsage')
diskUsage = Node(DiscreteDistribution({'low': 0.3, 'med': 0.5, 'high': 0.2}), name='diskUsage')
osType = Node(DiscreteDistribution({'windows': 0.5, 'linux': 0.5}), name='osType')
netTraffic = Node(DiscreteDistribution({'low': 0.3, 'med': 0.5, 'high': 0.2}), name='netTraffic')

appType_cpt = ConditionalProbabilityTable(
    [[ 'low', 'windows', 'A', 0.3 ],
     [ 'low', 'linux', 'B', 0.7 ],
     [ 'med', 'windows', 'C', 0.6 ],
     [ 'med', 'linux', 'D', 0.4 ],
     [ 'high', 'windows', 'E', 0.9 ],
     [ 'high', 'linux', 'F', 0.1 ]],
    [cpuUsage.distribution, memUsage.distribution, osType.distribution])

appType = Node(appType_cpt, name='appType')

model = BayesianNetwork('System Failure')
model.add_states(cpuUsage, memUsage, diskUsage, osType, netTraffic, appType)
model.add_edge(cpuUsage, appType)
model.add_edge(memUsage, appType)
model.add_edge(diskUsage, appType)
model.add_edge(osType, appType)
model.add_edge(netTraffic, appType)
model.bake()

probFailure = model.predict_proba({'cpuUsage': 'high', 'memUsage': 'high', 'diskUsage': 'high', 'osType': 'windows', 'netTraffic': 'med'})
print(probFailure[model.states.index(appType)].parameters[0]['E'])
