from dxl.dxlchain import DxlChain

def turretconnect():
	chain = DxlChain("/dev/ttyACM0", rate=57600)
	chain.sync_write_pos_speed([1,2][512,512],[512,512])
