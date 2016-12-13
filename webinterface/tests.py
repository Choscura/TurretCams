from dxl.dxlchain import DxlChain

chain = DxlChain("/dev/ttyACM0", rate = 57600, timeout = 0.02)

print(chain.get_motor_list())
