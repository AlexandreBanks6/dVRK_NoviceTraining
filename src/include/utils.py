##File with utility functions for converting between transformation types, enforcing orthogonality, and converting from opencv vectors  to
#homogeneous transforms

import numpy as np
import glm
import tf_conversions.posemath as pm
import cv2



def invHomogeneous(transform):
    #Input: Homogeneous transform (numpy)
    #Output: Inverse of homogeneous transform (numpy)

    R=transform[0:3,0:3]

    R_trans=np.transpose(R)
    d=transform[0:3,3]
    neg_R_trans_d=-1*np.dot(R_trans,d)
    inverted_transform=np.identity(4)
    inverted_transform[0:3,0:3]=R_trans
    inverted_transform[0:3,3]=neg_R_trans_d
    return inverted_transform

def convertRvecTvectoHomo(rvec,tvec):
    #Input: OpenCV rvec (rotation) and tvec (translation)
    #Output: Homogeneous Transform
    Rot,_=cv2.Rodrigues(rvec)
    transform=np.identity(4)
    transform[0:3,0:3]=Rot
    transform[0:3,3]=tvec
    return transform


def EnforceOrthogonalityNumpy(R):
    #Function which enforces a rotation matrix to be orthogonal
    #Input: R is a 3x3 numpy rotation

    #Extracting columns of rotation matrix
    x=R[:,0] 
    y=R[:,1]
    z=R[:,2]
    diff_err=np.dot(x,y)
    x_orth=x-(0.5*diff_err*y)
    y_orth=y-(0.5*diff_err*x)
    z_orth=np.cross(x_orth,y_orth)
    x_norm=0.5*(3-np.dot(x_orth,x_orth))*x_orth
    y_norm=0.5*(3-np.dot(y_orth,y_orth))*y_orth
    z_norm=0.5*(3-np.dot(z_orth,z_orth))*z_orth
    R_new=np.column_stack((x_norm,y_norm,z_norm))

    return R_new


def enforceOrthogonalPyKDL(self,pykdl_frame):
    #Takes in a pykdl frame and enforces orthogonality
    pykdl_frame_new=pm.toMatrix(pykdl_frame)
    pykdl_frame_new[0:3,0:3]=EnforceOrthogonalityNumpy(pykdl_frame_new[0:3,0:3])
    pykdl_frame_new=pm.fromMatrix(pykdl_frame_new)
    return pykdl_frame_new


def enforceOrthogonalGLM(self,GLM_frame):
    #Takes in a pykdl frame and enforces orthogonality
    frame_new=np.array(GLM_frame.to_list())
    frame_new[0:3,0:3]=EnforceOrthogonalityNumpy(frame_new[0:3,0:3])
    frame_new=glm.mat4(*frame_new.flatten())
    return frame_new



def rotationX(theta):
    #Rotate about x axis by theta
    R=np.array([[1,0,0],
               [0,np.cos(theta),-np.sin(theta)],
               [0,np.sin(theta),np.cos(theta)]])
    return R

def rotationY(theta):
    #Rotate about x axis by theta
    R=np.array([[1,0,0],
               [0,np.cos(theta),-np.sin(theta)],
               [0,np.sin(theta),np.cos(theta)]])
    return R

def rotationZ(theta):
    #Rotate about z axis by theta
    R=np.array([[np.cos(theta),0,np.sin(theta)],
               [0,0,0],
               [-np.sin(theta),0,np.cos(theta)]])
    return R


def SkewSymmetricMatrix(v):
    #Takes the skew symmetric matrix of a vector
    skew_mat=np.array([[0,-v[2],v[1]],
                        [v[2],0,-v[0]],
                        [-v[1],v[0],0]])       
    
    return skew_mat

def convertPyDK_To_GLM(pykdl_frame):
    numpy_frame=pm.toMatrix(pykdl_frame)
    glm_frame=glm.mat4(*numpy_frame.flatten())
    return glm_frame

