#test#copy
import smbus
import time

# Initialize SMBus object
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi's I2C bus 1
# ADC and expander addresses
adc_address = 0x48
expander_address = 0x20

# Function to write 8-bit data to a register
def write_data(address,reg, data):
    bus.write_byte_data(address,reg, data)
# Function to read 8-bit data from a register
def read_data(address,reg):
    return bus.read_byte_data(address,reg)
# Function to write 16-bit data to the ADC register
def write_16bit_register(address, register, data):
    # Split the 16-bit data into two 8-bit values (MSB and LSB)
    msb = (data >> 8) & 0xFF
    lsb = data & 0xFF
    # Write MSB and LSB to the specified register
    bus.write_i2c_block_data(address, register, [msb, lsb])
# Function to read a 16-bit data from the ADC register
def read_16bit_register(address, register):
    # Read two bytes from the specified register
    data = bus.read_i2c_block_data(address, register, 2)
    # Combine the two bytes into a single 16-bit value
    return (data[0] << 8) | data[1]

try:
# Function of ADC
    # Write 16-bit configuration data to the ADC register
    write_16bit_register(adc_address, 0x01, 0b1100000011100011)
    # Set the address pointer to the conversion register
    bus.write_byte(adc_address, 0x00)

# Function of GPIO expander
    # Write to config expander Register
    write_data(expander_address, 0x06, 0b11111000)
    write_data(expander_address, 0x07, 0b01111111)

    # Write to Output Port Register
    # enable path S1
    write_data(expander_address, 0x02, 0b11111001)
    write_data(expander_address, 0x03, 0b01111111)
   # Read the conversion result from the ADC
    conversion_result = read_16bit_register(adc_address, 0x00) >> 4
    time.sleep(0.1)
    output_value= conversion_result * 0.003
    # Print the conversion result
    print("UTD_3V3 voltage level test:", output_value)
    
    # enable path S3
    write_data(expander_address, 0x02, 0b11111011)
    write_data(expander_address, 0x03, 0b01111111)
    # Read the conversion result from the ADC
    conversion_result = read_16bit_register(adc_address, 0x00) >> 4
    time.sleep(0.1)
    output_value= conversion_result * 0.003
    # Print the conversion result
    print("UTD_5V voltage level test:", output_value)

    # disable paths
    write_data(expander_address, 0x02, 0b11111111)
    write_data(expander_address, 0x03, 0b11111111)
    time.sleep(0.1)
    print("test pathes are now close")

    # Read the conversion result from the ADC
    conversion_result = read_16bit_register(adc_address, 0x00)
    time.sleep(0.1)
    # Print the conversion result
    print("Exit:", conversion_result >> 4)

except Exception as e:
    print("Error:", str(e))
finally:
    # Cleanup
    bus.close()
