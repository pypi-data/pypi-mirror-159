# Copyright © 2022 Electric Power Research Institute, Inc. All rights reserved.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met: 
# · Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# · Redistributions in binary form must reproduce the above copyright notice, 
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# · Neither the name of the EPRI nor the names of its contributors may be used 
#   to endorse or promote products derived from this software without specific
#   prior written permission.


from opender.auxiliary_funcs.low_pass_filter import LowPassFilter
from opender.auxiliary_funcs.flipflop import FlipFlop


class FreqDroop:
    """
    Frequency-droop Function
    EPRI Report Reference: Section 3.6.3 in Report #3002021694: IEEE 1547-2018 DER Model
    """
    
    def __init__(self):
        self.pf_lpf = LowPassFilter()
        self.p_pf_pre_pu_prev = None
        self.p_out_kw_prev = None
        self.pf_uf_prev = None
        self.pf_of_prev = None
        self.pf_uf = None
        self.pf_of = None
        self.p_pf_pu = 0
        self.p_pf_pu_prev = None
        self.pf_uf_active_ff = FlipFlop(0)
        self.pf_of_active_ff = FlipFlop(0)
        self.pf_uf_active = 0
        self.pf_of_active = 0

    def calculate_p_pf_pu(self, der_file, exec_delay, der_input, p_out_kw, ap_limit_pu, p_pv_limit_pu):
        
        """
        Calculate power reference according to frequency-droop function

        Variable used in this function:
        
        :param f_meas_hz:	DER frequency measurement in Hertz, from model input
        :param pf_dbof_exec:	Over frequency deadband offset from nominal frequency signal (PF_DBOF) after execution delay
        :param pf_dbuf_exec:	Under frequency deadband offset from nominal frequency signal (PF_DBUF) after execution delay
        :param pf_kof_exec:	Over frequency slope signal (PF_KOF) after execution delay
        :param pf_kuf_exec:	Under frequency slope signal (PF_KUF) after execution delay
        :param pf_olrt_exec:	Frequency-Active power open-loop response time signal (PF_OLRT) after execution delay
        :param pf_olrt_appl:  Applied open-loop response time for frequency droop function
        :param p_dc_pu:	DER available DC power in pu
        :param NP_EFFICIENCY:	DER system efficiency for DC/AC power conversion
        :param NP_P_MIN_PU:	DER minimum active power output
        :param NP_P_MAX:	DER active power rating at unity power factor

        Internal variables:
        
        :param pf_of:	Over-frequency detected
        :param pf_uf:	Under-frequency detected
        :param p_pf_pre_pu:	Pre-disturbance active power output, defined by the active power output at the point of time the frequency exceeds the deadband.

        Internal state variables:
        
        :param p_pf_pre_pu_prev:	Value of variable p_pf_pre_pu (pre-disturbance active power output) in the previous time step (initialized by the first value of p_dc_kw×NP_EFFICIENCY/NP_P_MAX)
        :param p_out_kw_prev:	Value of variable p_out_kw (DER model output active power) in the previous time step (initialized by the first value of p_dc_kw×NP_EFFICIENCY)
        :param pf_of_prev:	Value of variable pf_of (Over-frequency detected) in the previous time step (initialized by 0)
        :param pf_uf_prev:	Value of variable pf_uf (Under-frequency detected) in the previous time step (initialized by 0)

        Output:
        
        :param p_pf_pu	Output active power from frequency-droop function
        """

        # Eq. 22, detect if in under-frequency or over-frequency condition
        if(der_input.freq_hz < (60 - exec_delay.pf_dbuf_exec)) and der_file.PF_MODE_ENABLE:
            self.pf_uf = 1
        else:
            self.pf_uf = 0
            
        if(der_input.freq_hz > (60 + exec_delay.pf_dbof_exec)) and der_file.PF_MODE_ENABLE:
            self.pf_of = 1
        else:
            self.pf_of = 0

        # Initialize internal state variables for under- and over-frequency condition detection
        if(self.pf_uf_prev is None):
            self.pf_uf_prev = self.pf_uf
        if(self.pf_of_prev is None):
            self.pf_of_prev = self.pf_of

        # Initialize internal state variables of DER output in previous time step
        if(self.p_out_kw_prev is None):
            self.p_out_kw_prev = min((der_input.p_dc_pu * der_file.NP_P_MAX * der_file.NP_EFFICIENCY),
                                     (ap_limit_pu*der_file.NP_P_MAX),
                                     (p_pv_limit_pu*der_file.NP_P_MAX))
        else:
            self.p_out_kw_prev = p_out_kw

        # Initialize internal state variables of pre-disturbance active power output
        if(self.p_pf_pre_pu_prev is None):
            self.p_pf_pre_pu_prev = min((der_input.p_dc_pu * der_file.NP_EFFICIENCY),ap_limit_pu,p_pv_limit_pu)

        # Eq. 23, calculate pre-disturbance active power output
        p_pf_pre_pu_temp = self.p_out_kw_prev / der_file.NP_P_MAX
        if(self.pf_uf == 1 and self.pf_uf_prev ==1):
            p_pf_pre_pu = self.p_pf_pre_pu_prev
        elif(self.pf_of == 1 and self.pf_of_prev == 1):
            p_pf_pre_pu = self.p_pf_pre_pu_prev
        else:
            p_pf_pre_pu = p_pf_pre_pu_temp

        # Eq. 24, calculate active power reference according to frequency-droop
        p_pf_of_pu = p_pf_pre_pu - ((der_input.freq_hz - (60 + exec_delay.pf_dbof_exec)) / (60 * exec_delay.pf_kof_exec))
        p_pf_of_pu = max(p_pf_of_pu, der_file.NP_P_MIN_PU)
        
        p_pf_uf_pu = p_pf_pre_pu + (((60 - exec_delay.pf_dbof_exec) - der_input.freq_hz) / ( (60 * exec_delay.pf_kuf_exec)))
        p_pf_uf_pu = min(p_pf_uf_pu, der_input.p_dc_pu * der_file.NP_EFFICIENCY)
        
        if(self.pf_of == 1):
            p_pf_ref_pu = p_pf_of_pu
        elif(self.pf_uf == 1):
            p_pf_ref_pu = p_pf_uf_pu
        else:
            p_pf_ref_pu = min((der_input.p_dc_pu * der_file.NP_EFFICIENCY),ap_limit_pu, p_pv_limit_pu)

        # Eq. 25, apply the low pass filter
        pf_olrt_appl = exec_delay.pf_olrt_exec if self.pf_uf or self.pf_of or self.pf_uf_active or self.pf_of_active else 0
        self.p_pf_pu = self.pf_lpf.low_pass_filter(p_pf_ref_pu, pf_olrt_appl)

        # Initialize internal state variable for the first time step of simulation
        if self.p_pf_pu_prev is None:
            self.p_pf_pu_prev = self.p_pf_pu

        # Eq. 26, decide if frequency droop function is active
        pf_uf_active_set = self.pf_uf and der_file.PF_MODE_ENABLE
        pf_uf_active_reset = (not pf_uf_active_set) and abs(self.p_pf_pu-p_pf_ref_pu)<1.e-2
        self.pf_uf_active = self.pf_uf_active_ff.flipflop(pf_uf_active_set, pf_uf_active_reset)

        pf_of_active_set = self.pf_of and der_file.PF_MODE_ENABLE
        pf_of_active_reset = (not pf_of_active_set) and abs(self.p_pf_pu-p_pf_ref_pu)<1.e-2
        self.pf_of_active = self.pf_of_active_ff.flipflop(pf_of_active_set, pf_of_active_reset)

        # Save the values for calculations in next time step
        self.pf_uf_prev = self.pf_uf
        self.pf_of_prev = self.pf_of
        self.p_pf_pre_pu_prev = p_pf_pre_pu
        self.p_pf_pu_prev = self.p_pf_pu

        return self.p_pf_pu, self.pf_uf_active, self.pf_of_active
