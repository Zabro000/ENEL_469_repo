from engineering_notation import EngNumber
def value_print_block(title: str = None):
    if title is None: 
        print()

    else:
        print()
        print(f"{title:-^100}")

def value_printer(sentance, value, unit: str = None, floating: int = None, end = None) -> None:

    if floating is None:
        floating = 2

    if unit is None:
        unit = " "

    eng_number = EngNumber(value)

    if not end:
        message = f"~ {sentance}: {eng_number}{unit}"
        print(message)
    else:
        message = f"~ {sentance}: {eng_number}{unit} {end}"
        print(message)




def theo_calcs_voltage_amp(VCC, VT, BETA, assumed_ic, assumed_open_voltage_gain, assumed_r11, assumed_r9, value_print = None):
    gm = assumed_ic / VT
    calced_r12 = assumed_open_voltage_gain * (1 + gm * assumed_r11) / gm

    ALPHA = BETA / (BETA + 1)

    calced_r13 = (1 / ALPHA) * ((3 / assumed_ic) - ALPHA * assumed_r11 - calced_r12)

    vb = 0.7 + (1 / ALPHA) * (assumed_ic) * (assumed_r11 +  calced_r13) 

    i1 = (VCC - vb) / (assumed_r9)

    ib = assumed_ic / BETA

    i2 = i1 - ib

    calced_r10 = vb / i2

    if value_print:
        value_print_block("Voltage amp calculations")
        value_printer("Assumed R11", assumed_r11, "ohm")
        value_printer("Calc'd R12", calced_r12, "ohm")
        value_printer("Calc'd R13", calced_r13, "ohm")
        value_printer("Assumed R9", assumed_r9, "ohm")
        value_printer("Calc'd R10", calced_r10, "ohm")
        

def theo_calcs_output_buffer(VCC, BETA, assumed_vce5, assumed_ic5, assumed_ic4, assumed_r16, value_print = None):
    ve5 = VCC - assumed_vce5
    vb4 = VCC - 1.9
    ALPHA = BETA / (BETA + 1)

    ie5 = (1 / ALPHA) * assumed_ic5

    calced_r17 = ve5 / ie5

    i2 = vb4 / assumed_r16

    ib4 = assumed_ic4 / BETA

    calced_r15 = vb4 / (i2 + ib4)

    if value_print:
        value_print_block("Output buffer calculations")
        value_printer("Assumed R16", assumed_r16, "ohm")
        value_printer("Calc'd R17", calced_r17, "ohm")
        value_printer("Calc'd R15", calced_r15, "ohm")







