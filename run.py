import nxt.locator as nxtl
import nxt.motor as nxtm
import random

def spin_around(b, flag):
    m_right = nxtm.Motor(b, nxtm.PORT_C)
    if flag:
        m_right.turn(10, 360)
    else:
        m_right.turn(-127, 720)
        
b = nxtl.find_one_brick(debug=True,strict=True,method=nxtl.Method(usb=True, bluetooth=False))
if b:
    for i in range(30):
        var = random.randint(1,5)
        if var == 1:
            flag = True
        else:
            flag = False
        spin_around(b, flag)
else:
    print('No NXT bricks found')