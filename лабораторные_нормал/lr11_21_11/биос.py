class CPU:
    def __init__(self, x):
        pass
# Оперативная пямать
class Memory:
    def __init__(self, x): 
        pass
class Hard_drive:
    def __init__(self, x): 
        pass
class Facade:
    def CheckCPU(x): 
        return CPU(x)
    CheckCPU = staticmethod(CheckCPU)
    def CheckMemory(x): 
        return Memory(x)
    CheckMemory = staticmethod(CheckMemory)
    def CheckHD(x): 
        return Hard_drive(x)
    CheckHD = staticmethod(CheckHD)
if __name__ == '__main__':
    a = Facade.CheckCPU("Raizen_5490")
    b = Facade.CheckMemory("Kingston_16GB_PC3_12800")
    c = Facade.CheckHD("Hitachi_Travelstar_7K1000")