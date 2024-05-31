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

# Function of ADC
try:
    # Write to Config ADC Register
    write_data(adc_address, 0x01, 0b1100001011100011)
    # Read ADC Conversion Register
    conversion_r = read_data(adc_address, 0x00)
    # Wait for conversion time
    time.sleep(5)
    # Print conversion result
    print(conversion_r)

except Exception as e:
    print("Error:", str(e))
finally:
    # Cleanup
    bus.close()
