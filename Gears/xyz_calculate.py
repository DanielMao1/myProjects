import camera_configs
import numpy as np
#cam=camera_configs.right_camera_matrix
# r=camera_configs.R
# t=camera_configs.T
cam=np.array([[988.4811,-4.6932,600.3510],[0,989.7077,360.3455],[0,0,1]])
r=np.array([[0.9990,-0.0096,0.0439],[-0.0105,0.9998,-0.0196],[-0.0437,0.0201,0.9988]])
t=np.array([[-150],[-4.4888],[11.9268]])



def calculate_world_xyz(x1,y1,x2,y2):

    x1=x1-cam[0][2]
    y1=y1-cam[1][2]
    x2=x2-cam[0][2]
    y2=y2-cam[1][2]

    z=cam[1][1]*(cam[1][1]*t[0]-x2*t[2])/\
      (x2*(r[2][0]*x1+r[2][1]*y1+cam[1][1]*r[2][2])-cam[1][1]*
       (r[0][0]*x1+r[0][1]*y1+cam[1][1]*r[0][2]))
    y=z*y1/cam[1][1]
    x=z*x1/cam[0][0]

    return (x,y,z)