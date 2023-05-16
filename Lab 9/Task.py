p1Prior = 0.3
p2Prior = 0.2
p3Prior = 0.5

pDGivenP1 = 0.01
pDGivenP2 = 0.03
pDGivenP3 = 0.02

pD = p1Prior * pDGivenP1 + p2Prior * pDGivenP2 + p3Prior * pDGivenP3

posteriorP1 = (p1Prior * pDGivenP1) / pD
posteriorP2 = (p2Prior * pDGivenP2) / pD
posteriorP3 = (p3Prior * pDGivenP3) / pD

if posteriorP1 > posteriorP2 and posteriorP1 > posteriorP3:
    print("Plan 1 was most likely used and responsible.")
elif posteriorP2 > posteriorP1 and posteriorP2 > posteriorP3:
    print("Plan 2 was most likely used and responsible.")
else:
    print("Plan 3 was most likely used and responsible.")
