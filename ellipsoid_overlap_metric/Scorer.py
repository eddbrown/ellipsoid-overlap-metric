from sklearn.covariance import EmpiricalCovariance as EC
import numpy as np
from scipy import linalg
from shapely import geometry
from shapely import affinity

def score(A,B):
    shapeA = shape_(A)
    shapeB = shape_(B)
    intersection = shapeA.intersection(shapeB)
    intersection_area = intersection.area

    return(round(min(intersection_area/shapeA.area, intersection_area/shapeB.area),3))

def shape_(data):
    ec = EC()
    centre = np.mean(data,axis=0)
    covar = ec.fit(data).covariance_
    v, w = linalg.eigh(covar)
    v = 2. * np.sqrt(2.) * np.sqrt(v)
    u = w[0] / linalg.norm(w[0])
    angle = np.arctan(u[1] / u[0])
    angle = 180. * angle / np.pi
    circ = geometry.Point(centre).buffer(1)
    ellipse  = affinity.scale(circ,float(v[0]),float(v[1]))


    return affinity.rotate(ellipse,angle)
