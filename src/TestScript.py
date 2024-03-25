import glm
import numpy as np
from include import HandEye
import random
def normalize_2d(matrix):
    norm = np.linalg.norm(matrix)
    matrix = matrix/norm  # normalized matrix
    return matrix

def generateRotation(theta):
    R=np.array([[np.cos(theta),-np.sin(theta),0],
               [np.sin(theta),np.cos(theta),0],
               [0,0,1]])
    return R

hand_eye_obj=HandEye.HandEye()

#a=np.array([0.1,0.2,0.3,0.4])
#b=np.array([0.5,0.6,0.7,0.8])

#hand_eye_obj.contructK(a,b)

#R=np.array([[0.2,0.5,0.3],
 #           [0.8,0.1,0.11],
  #          [-0.2,-0.55,-0.25]])
#R_new=hand_eye_obj.EnforceOrthogonality(R)
#A=np.array([[0.2,0.5,0.3,2],
        #    [0.8,0.1,0.11,5],
        #    [-0.2,-0.55,-0.25,6],
         #   [0,0,0,1]])
#a,a_prime=hand_eye_obj.HomoToDualQuat(A)

transA=normalize_2d(np.random.randn(1,3))
RA=generateRotation(random.uniform(0,1)*np.pi)
transB=normalize_2d(np.random.randn(1,3))
RB=generateRotation(random.uniform(0,1)*np.pi)
A=np.identity(4)
B=np.identity(4)
A[0:3,0:3]=RA
A[0:3,3]=transA
B[0:3,0:3]=RB
B[0:3,3]=transB
A=[A]
B=[B]
print("A: "+str(A))
print("B: "+str(B))
for i in range(0,3):
    transA=normalize_2d(np.random.randn(1,3))
    RA=generateRotation(random.uniform(0,1)*np.pi)
    transB=normalize_2d(np.random.randn(1,3))
    RB=generateRotation(random.uniform(0,1)*np.pi)
    new_A=np.identity(4)
    new_B=np.identity(4)
    new_A[0:3,0:3]=RA
    new_A[0:3,3]=transA
    new_B[0:3,0:3]=RB
    new_B[0:3,3]=transB

    A.append(normalize_2d(new_A))
    B.append(normalize_2d(new_B))

A = np.array(A)
B = np.array(B)
print("A: "+str(A))
print("B: "+str(B))
hand_eye_obj.ComputeHandEye(A,B)




