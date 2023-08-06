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


# -*- coding: utf-8 -*-

from opender.auxiliary_funcs.time_delay import TimeDelay
from .auxiliary_funcs.flipflop import FlipFlop
from opender.auxiliary_funcs.cond_delay import ConditionalDelay
from . import operating_condition_input_processing
import numpy as np


#%%
class EnterServiceTrip:
    """
    Enter Service and Trip related behaviors
    """
    def __init__(self, STATUS_INIT):
        """
        :NP_P_MIN_PU:	DER minimum active power output
        :ES_RANDOMIZED_DELAY_ACTUAL:	Specified value for enter service randomized delay for simulation purpose
        :NP_P_MAX:  Active power maximum rating
        :NP_VA_MAX: Apparent power maximum rating
        :STATUS_INIT:   Initial DER Status
        """
        # initialize object parameters
        self.es_flag = 0
        self.es_randomized_delay_time = 0

        self.vft_delay = ConditionalDelay()
        self.uv1_delay = ConditionalDelay()
        self.uv2_delay = ConditionalDelay()
        self.ov1_delay = ConditionalDelay()
        self.ov2_delay = ConditionalDelay()
        self.uf1_delay = ConditionalDelay()
        self.uf2_delay = ConditionalDelay()
        self.of1_delay = ConditionalDelay()
        self.of2_delay = ConditionalDelay()

        self.rand_delay = TimeDelay()
        self.der_status_flipflop = FlipFlop(STATUS_INIT)
        self.der_status = STATUS_INIT
        self.debug = None


    def es_decision(self, der_file, exec_delay,  der_input:operating_condition_input_processing.DERInputs):
        """
        Generate DER status (ON/OFF) based on enter service and trip settings
        EPRI Report Reference: Section 3.5 in Report #3002021694: IEEE 1547-2018 DER Model

        Variable used in this function:
        
        :param es_permit_service_exec: Permit service activated by request from the area EPS operator (ES_PERMIT_SERVICE) after execution delay
        :param v_low_pu: Minimum applicable voltage as enter service, over voltage trip criterion in per unit
        :param v_high_pu: Maximum applicable voltage as enter service, over voltage trip criterion in per unit
        :param freq_hz: Frequency at RPA
        :param p_dc_pu: DER available DC power in per unit
        :param es_v_low_exec: Minimum applicable voltage for enter service criteria (ES_V_LOW) signal after execution delay
        :param es_v_high_exec: Maximum applicable voltage for enter service criteria (ES_V_HIGH) signal after execution delay
        :param es_f_low_exec: Minimum frequency for enter service criteria (ES_F_LOW) signal after execution delay
        :param es_f_high_exec: Maximum frequency for enter service criteria (ES_F_HIGH) signal after execution delay
        :param es_delay_exec: Minimum intentional delay before initiating softstart (ES_DELAY) signal after execution delay
        :param uv1_trip_v_exec: Low voltage must trip curve point UV1 voltage setting (UV1_TRIP_V) signal after execution delay
        :param uv1_trip_t_exec: Low voltage must trip curve point UV1 duration setting (UV1_TRIP_T) signal after execution delay
        :param ov1_trip_v_exec: High voltage must trip curve point OV1 voltage setting (OV1_TRIP_V) signal after execution delay
        :param ov1_trip_t_exec: High voltage must trip curve point OV1 duration setting (OV1_TRIP_T) signal after execution delay
        :param uv2_trip_v_exec: Low voltage must trip curve point UV2 voltage setting (UV2_TRIP_V) signal after execution delay
        :param uv2_trip_t_exec: Low voltage must trip curve point UV2 duration setting (UV2_TRIP_T) signal after execution delay
        :param ov2_trip_v_exec: High voltage must trip curve point OV2 voltage setting (OV2_TRIP_V) signal after execution delay
        :param ov2_trip_t_exec: High voltage must trip curve point OV2 duration setting (OV2_TRIP_T) signal after execution delay
        :param uf1_trip_f_exec: Low frequency must trip curve point UF1 voltage setting (UF1_TRIP_V) signal after execution delay
        :param uf1_trip_t_exec: Low frequency must trip curve point UF1 duration setting (UF1_TRIP_T) signal after execution delay
        :param of1_trip_f_exec: High frequency must trip curve point OF1 voltage setting (OF1_TRIP_V) signal after execution delay
        :param of1_trip_t_exec: High frequency must trip curve point OF1 duration setting (OF1_TRIP_T) signal after execution delay
        :param uf2_trip_f_exec: Low frequency must trip curve point UF2 voltage setting (UF2_TRIP_V) signal after execution delay
        :param uf2_trip_t_exec: Low frequency must trip curve point UF2 duration setting (UF2_TRIP_T) signal after execution delay
        :param of2_trip_f_exec: High frequency must trip curve point OF2 voltage setting (OF2_TRIP_V) signal after execution delay
        :param of2_trip_t_exec: High frequency must trip curve point OF2 duration setting (OF2_TRIP_T) signal after execution delay
        :param es_randomized_delay_exec: Maximum time for enter service randomized delay (ES_RANDOMIZED_DELAY) signal after execution delay
        :param es_ramp_rate_exec: Enter service soft-start duration (ES_RAMP_RATE) signal after execution delay

        Internal variable:
        
        :param der_status_es:	Enter service criteria met
        :param der_status_trip:	Trip criteria met
        :param es_vf_crit:	Enter service voltage and frequency criteria met
        :param es_vft_crit:	Enter service voltage and frequency criteria met for the enter service delay
        :param es_p_crit:	DER output power is greater than the minimum output power
        :param es_crit:	Enter service criteria met
        :param es_randomized_delay_time:	Enter service randomized delay time (initiated by 0)
        :param es_crit_delay:	Enter service criteria after randomized delay
        :param uv1_trip:	DER trip criteria met due to under voltage must trip setting 1 (UV1)
        :param uv2_trip:	DER trip criteria met due to under voltage must trip setting 2 (UV2)
        :param ov1_trip:	DER trip criteria met due to over voltage must trip setting 1 (OV1)
        :param ov2_trip:	DER trip criteria met due to over voltage must trip setting 2 (OV2)
        :param uf1_trip:	DER trip criteria met due to under frequency must trip setting 1 (UF1)
        :param uf2_trip:	DER trip criteria met due to under frequency must trip setting 2 (UF2)
        :param of1_trip:	DER trip criteria met due to over frequency must trip setting 1 (OF1)
        :param of2_trip:	DER trip criteria met due to over frequency must trip setting 2 (OF2)

        Output:
        
        :param der_status:	Status of DER, ON (1) or OFF (0)
        """


        # Eq 9, enter service logic of voltage and frequency checks
        es_vf_crit = (der_input.v_low_pu >= exec_delay.es_v_low_exec) and (der_input.v_high_pu <= exec_delay.es_v_high_exec) \
            and (der_input.freq_hz >= exec_delay.es_f_low_exec) and (der_input.freq_hz <= exec_delay.es_f_high_exec) and exec_delay.es_permit_service_exec

        # Eq 10, conditional delayed enable that voltage and frequency checks must be satisfied for a time delay period
        es_vft_crit = self.vft_delay.con_del_enable(es_vf_crit, exec_delay.es_delay_exec)

        # Eq 11, available DC power must be greater than DER minimum output
        es_p_crit = der_input.p_dc_pu >= der_file.NP_P_MIN_PU

        # Eq 12, Enter service criterion met
        es_crit = es_vft_crit and es_p_crit

        # Eq 13, generate the additional enter service randomized delay. The value is 0 if enter service ramp is used.
        if self.der_status:
            # if DER is on, reset randomized delay to 0 for next time use.
            self.es_randomized_delay_time = 0
        else:
            if der_file.ES_RANDOMIZED_DELAY_ACTUAL > 0 and es_crit:
                self.es_randomized_delay_time = der_file.ES_RANDOMIZED_DELAY_ACTUAL
            elif (exec_delay.es_ramp_rate_exec == 0) and (exec_delay.es_randomized_delay_exec > 0) and (der_file.NP_VA_MAX < 500):
                if self.es_randomized_delay_time == 0:
                    # If enabled, create a new randomized delay when enter service criterion made
                    self.es_randomized_delay_time = np.random.random() * exec_delay.es_randomized_delay_exec
            else:
                self.es_randomized_delay_time = 0


        # Eq 14, apply the randomized delay
        es_crit_delay = self.rand_delay.tdelay(es_crit,self.es_randomized_delay_time)
        der_status_es = es_crit_delay

        # Eq 15, under- and over-voltage, under- and over-frequency trip criterion using conditional delayed enable
        uv1_trip = self.uv1_delay.con_del_enable(der_input.v_low_pu < exec_delay.uv1_trip_v_exec, exec_delay.uv1_trip_t_exec)
        ov1_trip = self.ov1_delay.con_del_enable(der_input.v_high_pu > exec_delay.ov1_trip_v_exec, exec_delay.ov1_trip_t_exec)
        uv2_trip = self.uv2_delay.con_del_enable(der_input.v_low_pu < exec_delay.uv2_trip_v_exec, exec_delay.uv2_trip_t_exec)
        ov2_trip = self.ov2_delay.con_del_enable(der_input.v_high_pu > exec_delay.ov2_trip_v_exec, exec_delay.ov2_trip_t_exec)
        uf1_trip = self.uf1_delay.con_del_enable(der_input.freq_hz < exec_delay.uf1_trip_f_exec, exec_delay.uf1_trip_t_exec)
        of1_trip = self.of1_delay.con_del_enable(der_input.freq_hz > exec_delay.of1_trip_f_exec, exec_delay.of1_trip_t_exec)
        uf2_trip = self.uf2_delay.con_del_enable(der_input.freq_hz < exec_delay.uf2_trip_f_exec, exec_delay.uf2_trip_t_exec)
        of2_trip = self.of2_delay.con_del_enable(der_input.freq_hz > exec_delay.of2_trip_f_exec, exec_delay.of2_trip_t_exec)

        # Eq 16, if available DC power is lower than minimum DER output, trip DER
        p_min_trip = der_input.p_dc_pu < der_file.NP_P_MIN_PU

        # Eq 17, final trip decision based on all trip conditions
        der_status_trip = uv1_trip or ov1_trip or uv2_trip or ov2_trip \
            or uf1_trip or of1_trip or uf2_trip or of2_trip or p_min_trip or not exec_delay.es_permit_service_exec
        der_status_trip = der_status_trip

        # Eq 18 generate DER ON/OFF status based on flip-flop logic
        self.der_status = self.der_status_flipflop.flipflop(int(der_status_es), int(der_status_trip))

        # return der_status output
        return self.der_status
        


        
        
        
    
