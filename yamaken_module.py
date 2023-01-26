import numpy as np
def norm(vec):
    return ((vec[0])**2+(vec[1])**2)**0.5
def yamaken_kakudo_check(pointA, pointB, pointC):
    #三点入力　んでベクトルAB，ベクトルBCの角度と直角判定
    v_ab = pointB - pointA
    v_bc = pointC - pointB
    o_ab = norm(v_ab)
    o_bc = norm(v_bc)

    theta = np.degrees(np.arccos((np.dot(v_ab, v_bc))/(o_ab*o_bc)))
    print(theta)


    if np.dot(v_ab, v_bc) < 0.1 and np.dot(v_ab, v_bc) > -0.1:
        print("omedetou")
        print(np.dot(v_ab, v_bc))

    else:
        print("donmai")

if __name__ == "__main__":
    a = np.array([-0.0377227,0.0644253])
    b = np.array([-0.0268957,0.0924034])
    c = np.array([-0.00745963,0.129708])
    yamaken_kakudo_check(a,b,c)