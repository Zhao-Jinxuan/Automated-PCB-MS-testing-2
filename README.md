# Automated-PCB-MS-testing-2
5 branches in total: main, ADC-check, GPIO-expander-check,continuity-test and voltage-level-test. History of programming can be seen.

To prepare an environment for running code: please choose Visual Studio Code software, open a remote control window connected to host of Raspberry Pi, and define I2C mode of Raspberry Pi in terminal window.

To use the code:
Step 1: input 'sudo i2cdetect -y 1' in the terminal window to find I2C devices' unique addresses. (ADC and GPIO expander)
Step 2: look into Branch ADC-check and GPIO-expander-check, these 2 branches aim at configuring ADC and GPIO expander as I2C devices, change the values or time according to required performance based on their datasheets.
Step 3: To run the automated testing system, Branch continuity-test is the code used for running the continuity test, and Brach voltage-level-test includes the code used for running the voltage level test.
or when continuity test and voltage level test can be executed at the same time (when UTD isn't powered on), run Branch main can output all test results.

example of Expected output:

Step 1:
![image](https://github.com/Zhao-Jinxuan/Automated-PCB-MS-testing-2/assets/159006763/a98d3cc7-1de6-4dac-b336-8507e9b09ba5)
or
![image](https://github.com/Zhao-Jinxuan/Automated-PCB-MS-testing-2/assets/159006763/317d8326-344f-4dfa-b03d-86b247cc36f8)

Step 3:
![image](https://github.com/Zhao-Jinxuan/Automated-PCB-MS-testing-2/assets/159006763/f4f60c23-f1f6-4b6c-856b-72084c788b3a)
![image](https://github.com/Zhao-Jinxuan/Automated-PCB-MS-testing-2/assets/159006763/fbe62272-c2ba-4d8e-9c06-b4f434db4c38)
