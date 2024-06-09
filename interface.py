#ADC
import smbus
import time

# Initialize SMBus object
bus = smbus.SMBus(1)  # Use 1 for Raspberry Pi's I2C bus 1
# ADC address
adc_address = 0x48

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
    # Write 16-bit configuration data to the ADC register
    write_16bit_register(adc_address, 0x01, 0b1100001011100011)

    # Set the address pointer to the conversion register
    bus.write_byte(adc_address, 0x00)

    # Read the conversion result from the ADC
    conversion_result = read_16bit_register(adc_address, 0x00) >> 4
    # wait for communication time
    time.sleep(0.1)
    # convert conversion result into voltage value
    output_value= conversion_result * 0.003
    # Print the voltage value
    print("UTD_SDA_EXT:", output_value)

except Exception as e:
    print("Error:", str(e))
finally:
    # Cleanup
    bus.close()
