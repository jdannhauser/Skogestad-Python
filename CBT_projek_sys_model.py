import numpy as np 
import scipy.linalg as sc_lin


def sys(s):


    
    A=np.matrix([[-1.4E-2   ,4.3E-3   ,0    ,     0 ,       0  ,     0  ,       0 ,       0       , 0    ,    0   ,      0        ],
      [9.5E-3  ,   -1.38E-2, 4.6E-3 ,   0      ,  0 ,      0  ,       0     ,   0    ,    0  ,      0     ,    5E-4     ],
     [ 0        ,  9.5E-3 ,  -1.41E-2 , 6.3E-3  , 0   ,    0 ,        0     ,   0  ,      0     ,   0      ,   2E-4     ],
     [ 0     ,     0    ,    9.5E-3,    -1.58E-2, 1.1E-2 , 0   ,      0     ,   0    ,    0  ,      0    ,     0        ],
     [ 0   ,       0   ,     0 ,        9.5E-3 ,  -3.12E-2, 1.5E-2  , 0       , 0    ,    0   ,     0      ,   0        ],
      [0    ,      0     ,   0  ,       0,        2.02E-2 , -3.52E-2 ,2.2E-2 ,  0      ,  0     ,   0        , 0        ],
     [ 0   ,       0  ,      0   ,      0     ,   0        ,2.02E-2 , -4.22E-2, 2.8E-2 ,  0   ,     0        , 0        ],
     [ 0 ,         0  ,      0 ,        0 ,       0     ,   0   ,     2.02E-2,  -4.82E-2, 3.7E-2,   0  ,       2E-4     ], 
     [ 0    ,      0   ,     0 ,        0    ,    0   ,     0  ,      0       , 2.02E-2,  -5.72E-2, 4.2E-2 ,   5E-4     ],
     [ 0   ,       0     ,   0  ,       0    ,    0  ,      0 ,       0   ,     0   ,     2.02E-2 ,  -4.83E-2 ,5E-4     ],
     [ 2.55E-2 ,   0    ,    0     ,    0     ,   0    ,    0     ,   0    ,    0 ,       0  ,       2.55E-2  ,-1.85E-2 ]])
    
    
    
    B=np.matrix(
      [[0   ,         0  ,         0       ],
      [ 5E-6    ,     -4E-5,       2.5E-3  ],
      [ 2E-6  ,       -2E-5,       5E-3    ],
      [ 1E-6  ,       -1E-5,       5E-3    ],
      [ 0       ,     0   ,        5E-3    ],
      [ 0        ,    0      ,     5E-3    ],
      [ -5E-6   ,     1E-5  ,      5E-5    ],
      [ -1E-5 ,       3E-5   ,     5E-5    ],
      [ -4E-5   ,     5E-6 ,       2.5E-5  ],
      [ -2E-5    ,    2E-6  ,      2.5E-3  ],
      [ 4.6E-04  ,    4.6E-4  ,    0       ]])
    
        
    
    E=np.matrix(
       [[ 0],
        [0],
        [0],
        [0],
        [1E-2],
        [0],
        [0],
        [0],
        [0],
        [0],
        [0]])
    
    
    
    C=np.matrix(
    [[0,  0  ,0 , 0 , 0 , 0,  0,  0,  0,  1,  0 ],
    [   1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ],
    [   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1 ]])
    
    Scaling_mat     = np.matrix([[], [], []])
    G_process = C*sc_lin.inv(s*np.identity(np.shape(A)[0])-A)*B
    Gd_process =C*sc_lin.inv(s*np.identity(np.shape(A)[0])-A)*E
    
    return G_process , Gd_process