# -*- coding: utf-8 -*-
import time
import random
import nxt.locator as nxtl
import nxt.motor as nxtm

def main():
    nc = NXTControl()
    nc.do()

class NXTControl():
    def spin_around(self, b, flag):
        m_right = nxtm.Motor(b, nxtm.PORT_C)
        if flag:
            #m_right.turn(10, 360)
            milsec = random.uniform(3.0,5.0)
            time.sleep(milsec)
        else:
            m_right.turn(60, 720)
    
    def do(self):
        b = nxtl.find_one_brick(debug=True,strict=True,
                                method=nxtl.Method(usb=True, bluetooth=False))
        
        start = time.time()
        time_bomb = random.randint(25,35)
        
        if b:
            while(True):
                elapsed_time = time.time() - start
                if elapsed_time < time_bomb:
                    flag = True
                else:
                    flag = False
                    start = time.time()
                    time_bomb = random.randint(25,35)
                    
                # execute the action
                self.spin_around(b, flag)
        else:
            print('No NXT bricks found')
            
if __name__ == '__main__':
    main()
