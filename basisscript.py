import pyvisa

rm = pyvisa.ResourceManager("@py")

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n")

device.query(f"OUT:CH0 1023")

device.query(f"MEAS:CH1")
device.query(f"MEAS:CH2")