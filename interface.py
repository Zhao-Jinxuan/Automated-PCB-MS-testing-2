#test#copy
import smbus
import time

# Initialize SMBus object
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi's I2C bus 1
# ADC and expander addresses
adc_address = 0x48
expander_address = 0x20

# Function to write data to an I2C device
def write_data(address,reg, data):
    bus.write_byte_data(address,reg, data)
# Function to read data from an I2C device
def read_data(address,reg):
    return bus.read_byte_data(address,reg)

try:
# Function of GPIO expander
    # Write to config expander Register
    write_data(expander_address, 0x06, 0b11111000)
    # check write and read to register successfully
    v1= read_data(expander_address, 0x06)
    print(v1)
    #
    write_data(expander_address, 0x07, 0b01111111)

    # Write to Output Port Register
    # enable path S0
    write_data(expander_address, 0x02, 0b11111000)
    write_data(expander_address, 0x03, 0b01111111)
    print("continuity test 1:")
    
    # enable path S2
    write_data(expander_address, 0x02, 0b11111010)
    write_data(expander_address, 0x03, 0b01111111)
    print("continuity test 2:")

    # enable path S4
    write_data(expander_address, 0x02, 0b11111100)
    write_data(expander_address, 0x03, 0b01111111)
    print("continuity test 3:")

    # enable path S5
    write_data(expander_address, 0x02, 0b11111101)
    write_data(expander_address, 0x03, 0b01111111)
    print("continuity test 4:")

     # enable path S1
    write_data(expander_address, 0x02, 0b11111001)
    write_data(expander_address, 0x03, 0b01111111)
    print("3v3 voltage test 1:")
    
    # enable path S3
    write_data(expander_address, 0x02, 0b11111011)
    write_data(expander_address, 0x03, 0b01111111)
    print("5V voltage test 2:")

    # disable paths
    write_data(expander_address, 0x02, 0b11111111)
    write_data(expander_address, 0x03, 0b11111111)
    time.sleep(0.5)
    print("test pathes are now close")

except Exception as e:
    print("Error:", str(e))
finally:
    # Cleanup
    bus.close()
