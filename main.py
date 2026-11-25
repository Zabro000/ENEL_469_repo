from project_functions import theo_calcs as TC

BETA = 160
VCC = 9 
VT = 0.025
Av0 = 20


def voltage_amp_function():
    # parameters for votlage amp with our method of solving for numbers
    r11 = 70
    r9 = 10e3
    ic = 1.5e-3

    TC.theo_calcs_voltage_amp(VCC, VT, BETA, ic, Av0, r11,  r9, True)

def output_buffer_fucntion():
    # parameters for the output buffer
    r16 = 20e3
    vce5 = 8.5
    ic5 = 6.5e-3
    ic4 = 40e-6
    TC.theo_calcs_output_buffer(VCC, BETA, vce5, ic5, ic4, r16, True)




voltage_amp_function()
output_buffer_fucntion()















