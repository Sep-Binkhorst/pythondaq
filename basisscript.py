import pyvisa

rm = pyvisa.ResourceManager("@py")

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n")

for voltage in range(0, 1023):
    device.query(f"OUT:CH0 {voltage}")
    raw_u2 = device.query(f"MEAS:CH2?")
    print(f"De raw voltage op de weerstand is {raw_u2}")
    voltage_u2 = float(raw_u2) * (3.3/1024)
    print(f"De voltage op de weerstand is {voltage_u2}")
    raw_u1 = device.query(f"MEAS:CH1?")
    voltage_u1 = float(raw_u1) * (3.3/1024)

    raw_led = float(raw_u1) - float(raw_u2)
    voltage_led = voltage_u1 - voltage_u2
    print(f"De raw voltage op de led is {raw_led}")
    print(f"De voltage op de led is {voltage_led}")



