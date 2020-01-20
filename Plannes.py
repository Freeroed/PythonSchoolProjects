class Proccess:
    def __init__(self, aprTime, priority, cpuBurst):
        self.aprTime = aprTime
        self.priority = priority
        self.cpuBurst = cpuBurst
        self.status = " "

proccesses = [Proccess(0,10,8),  
Proccess(2,9,6),
Proccess(4,8,5),
Proccess(6,7,4),
Proccess(8,6,3),
Proccess(8,5,7),
Proccess(6,4,9),
Proccess(4,3,10),
Proccess(2,2,2),
Proccess(0,1,1)
]

answers = ["","","","","","","","","",""]

def getShorted(proccesses):
    sht = proccesses[0].cpuBurst
    for prc in proccesses:
        if prc.cpuBurst < sht:
            sht = prc.cpuBurst
    return sht

def getMXPriority(proccesses, shorted):
    mx = proccesses[0].priority
    for prc in proccesses:
        if prc.priority<mx and prc.cpuBurst == shorted:
            mx = prc.priority
    return mx
