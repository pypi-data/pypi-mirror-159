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

import numpy as np


#%%
def intercep_piecewise_circle(mag, xp, yp, k = 0.9, err = 1.e-3):
    """
    Find out the interception point of piece-wise function defined by xp and yp at given magnitude

    Input argument:
    
    :param xp: list or array on x axis (increasing from left to right)
    :param yp: list or array on y axis
    :param mag: magnitude of (x, y) that will intercept on the right side of xp and yp
    :param k: convergence factor (<1 slows convergence with increased robustness)
    :param err: error threshold

    Output:
    
    :param x: interception point on x axis
    :param y: interception point on y axis
    """
    # step 1: extend the list/array to the right to at least cover the requested mag
    xn = max(mag, xp[-1]+mag)
    yn = (yp[-1]-yp[-2])/(xp[-1]-xp[-2])*(xn-xp[-2])+yp[-2]
    xnew = np.append(xp, xn)
    ynew = np.append(yp, yn)
    # step 2: iterate until an intersection point is found
    x = mag
    imax = 50
    for ii in range(imax):
        y = np.interp(x, xnew, ynew)
        m = np.sqrt(x**2+y**2)
        if abs(m-mag) < err:
            break
        else:
            x = x+k*(mag/m*x-x)
    # print warning if not converge
    if ii == imax-1:
        print('Warning: search did not converge!')
    return x, y

# def piecewise_intercept(xp1, yp1, xp2, yp2, x, step:float=0.01):
#     """
#     Find out the intercept point of two piecewise curve defined by (xp1, yp1) and (xp2, yp2), which is smaller than x
#     If there is no intercept point, return x and y point defined by (xp2, yp2).
#     For volt-var or constant Q - (xp2, yp2) should be horizontal.
#     For const PF - (xp2, yp2) should be defined by const PF setpoint.
#     For watt-var - (xp2, yp2) should be the watt-var curve.
#
#     xp1,2: list or array on x axis
#     yp1,2: list or array on y axis
#     x: starting point
#     step: step size to search intercept point
#     """
#     if step < 1.e-5:
#         return x, np.interp(x,xp2, yp2)
#     else:
#         x_iter = x-step
#         while np.interp(x_iter, xp1, yp1)<np.interp(x_iter,xp2,yp2) and x_iter>0:
#             x_iter = x_iter - step
#         if x_iter <= 0:
#             return x, np.interp(x,xp1, yp1)
#         else:
#             x_intercept, y = piecewise_intercept(xp1, yp1,xp2, yp2, x_iter+step, step/10)
#
#     return x_intercept, np.interp(x_intercept,xp2, yp2)


class CapabilityPriority:
    """
    Calculate active and reactive power power output limited by DER ratings, according to the priority of responses.
    EPRI Report Reference: Section 3.9 in Report #3002021694: IEEE 1547-2018 DER Model
    """

    def calculate_limited_pq(self, der_file, exec_delay, p_desired_kw, q_desired_kvar):
        """
        Calculate limited DER output P and Q based on DER ratings and priority of responses.

        Variables used in this function:
        
        :param p_desired_kw:	Desired output active power considering DER enter service performance
        :param q_desired_kvar:	Desired output reactive power from reactive power support functions
        :param const_pf_mode_enable_exec:	Constant Power Factor Mode Enable (CONST_PF_MODE_ENABLE) after execution delay
        :param qv_mode_enable_exec:	Voltage-Reactive Power Mode Enable (QV_MODE_ENABLE) after execution delay
        :param qp_mode_enable_exec:	Active Power Reactive Power Mode Enable (QP_MODE_ENABLE) after execution delay
        :param const_q_mode_enable_exec:	Constant Reactive Power Mode Enable (CONST_Q_MODE_ENABLE) after execution delay
        :param WattVar_Curve: Watt-var settings
              ('P_PU' = [qp_curve_p1_gen_exec, qp_curve_p2_gen_exec, qp_curve_p3_gen_exec]
              'Q_PU' = [qp_curve_q1_gen_exec, qp_curve_q2_gen_exec, qp_curve_q3_gen_exec])

        Internal variables:
        
        :param q_requirement_inj:	Reactive power injection capability required by IEEE 1547-2018 (constant, 0.44 of DER VA rating)
        :param q_requirement_abs:	Reactive power absorption capability required by IEEE 1547-2018 (constant, 0.25 of DER VA rating if CAT_A, 0.44 of DER VA rating if CAT_B)
        :param q_max_inj:	Maximum reactive power injection at the desired active power output, defined by the capability curve NP_Q_CAPABILITY_BY_P_CURVE
        :param q_max_abs:	Maximum reactive power absorption at the desired active power output, defined by the capability curve NP_Q_CAPABILITY_BY_P_CURVE
        :param p_itcp_kw:  Intercept point active power of DER apparent power capability circle and a piecewise curve
        :param q_itcp_kvar:    Intercept point active power of DER apparent power capability circle and a piecewise curve
        :param q_limited_by_p_kvar:	Desired output reactive power after considering DER reactive power capability curve in volt-var or constant reactive power mode.
        :param q_limited_pf_kvar:	Desired output reactive power after considering DER apparent power capability circle in constant power factor mode
        :param q_limited_qp_kvar:	Desired output reactive power after considering DER apparent power capability circle in watt-var mode

        Outputs:
        
        :param p_limited_kw:	DER output active power after considering DER apparent power limits
        :param q_limited_kvar:	DER output reactive power after considering DER apparent power limits
        """

        self.q_requirement_abs = (0.25 if der_file.NP_NORMAL_OP_CAT == 'CAT_A' else 0.44) * der_file.NP_VA_MAX
        self.q_requirement_inj = 0.44 * der_file.NP_VA_MAX
        
        if exec_delay.const_q_mode_enable_exec or exec_delay.qv_mode_enable_exec:
            # Constant-Q or Volt-Var
            # Eq. 58, find the range of DER output Q with given desired P
            q_max_inj = der_file.NP_VA_MAX * np.interp(p_desired_kw/der_file.NP_P_MAX, der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_INJ_PU'], der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_INJ_PU'])
            q_max_abs = der_file.NP_VA_MAX * np.interp(p_desired_kw/der_file.NP_P_MAX, der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_ABS_PU'], der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_ABS_PU'])
            # Eq. 59, limit q_desired_kvar according to limit (+injection / -absorption)
            q_limited_by_p_kvar = min(q_max_inj, max(-q_max_abs, q_desired_kvar))

            if p_desired_kw**2+q_limited_by_p_kvar**2 < der_file.NP_VA_MAX**2:
                # Eq. 60, if within DER max apparent power rating, no changes need to be made
                p_limited_kw = p_desired_kw
                q_limited_kvar = q_limited_by_p_kvar
            elif der_file.NP_PRIO_OUTSIDE_MIN_Q_REQ == 'ACTIVE':
                # Eq. 61 reserve Q capability to the table 7 requirement and give the rest to P
                q_limited_kvar = min(self.q_requirement_inj, max(-self.q_requirement_abs, q_limited_by_p_kvar))
                p_limited_kw = np.sqrt(der_file.NP_VA_MAX**2-q_limited_kvar**2)

            else:
                # Eq. 62, Reactive power priority, reduce P to match apparent power limit
                q_limited_kvar = q_limited_by_p_kvar
                p_limited_kw = np.sqrt(der_file.NP_VA_MAX**2-q_limited_by_p_kvar**2)

        elif exec_delay.const_pf_mode_enable_exec:
            # Constant-PF
            if p_desired_kw ** 2 + q_desired_kvar ** 2 < der_file.NP_VA_MAX ** 2:
                # Eq. 63, no changes to be made
                p_limited_pf_kw = p_desired_kw
                q_limited_pf_kvar = q_desired_kvar
            else:
                # Eq. 64, reduce P & Q proportionally to maintain constant power factor
                k = min(1., der_file.NP_VA_MAX/max(1.e-9, np.sqrt(p_desired_kw**2+q_desired_kvar**2)))
                p_limited_pf_kw = p_desired_kw*k
                q_limited_pf_kvar = q_desired_kvar*k

            # Eq. 65, reduce Q if outside of DER Q capability range
            if q_limited_pf_kvar > 0:
                xp = [x*der_file.NP_P_MAX for x in der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_INJ_PU']]
                yp = [y*der_file.NP_VA_MAX for y in der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_INJ_PU']]
                p_itcp_kw, q_itcp_kvar = intercep_piecewise_circle(der_file.NP_VA_MAX, xp, yp)
            else:
                xp = [x*der_file.NP_P_MAX for x in der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_ABS_PU']]
                yp = [y*der_file.NP_VA_MAX for y in der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_ABS_PU']]
                p_itcp_kw, q_itcp_kvar = intercep_piecewise_circle(der_file.NP_VA_MAX, xp, yp)

            if abs(q_limited_pf_kvar) > q_itcp_kvar:
                p_limited_kw = min(p_itcp_kw, p_desired_kw)
            else:
                p_limited_kw = p_limited_pf_kw

            q_max_inj = der_file.NP_VA_MAX * np.interp(p_limited_kw/der_file.NP_P_MAX, der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_INJ_PU'], der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_INJ_PU'])
            q_max_abs = der_file.NP_VA_MAX * np.interp(p_limited_kw/der_file.NP_P_MAX, der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_ABS_PU'], der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_ABS_PU'])
            q_limited_kvar = min(q_max_inj, max(-q_max_abs, q_limited_pf_kvar))

        elif exec_delay.qp_mode_enable_exec:
            # Watt-Var
            if p_desired_kw**2+q_desired_kvar**2 < der_file.NP_VA_MAX**2:
                # Eq. 66, no changes to be made
                p_limited_kw = p_desired_kw
                q_limited_qp_kvar = q_desired_kvar
            else:
                # Eq. 67, find intercept point of VA limit circle and watt-var curve
                WattVar_Curve = {'P_PU': [exec_delay.qp_curve_p1_gen_exec, exec_delay.qp_curve_p2_gen_exec, exec_delay.qp_curve_p3_gen_exec],
                                 'Q_PU': [exec_delay.qp_curve_q1_gen_exec, exec_delay.qp_curve_q2_gen_exec, exec_delay.qp_curve_q3_gen_exec]},
                xp = [x*der_file.NP_P_MAX for x in WattVar_Curve['P_PU']]
                yp = [y*der_file.NP_VA_MAX for y in WattVar_Curve['Q_PU']]
                p_itcp_kw, q_itcp_kvar = intercep_piecewise_circle(der_file.NP_VA_MAX, xp, yp)
                p_limited_kw = min(p_itcp_kw, p_desired_kw)
                q_limited_qp_kvar = min(abs(q_itcp_kvar), abs(q_desired_kvar))*np.sign(q_desired_kvar)

            # Eq. 68, reduce Q if outside of DER Q capability range
            q_max_inj = der_file.NP_VA_MAX * np.interp(p_desired_kw/der_file.NP_P_MAX, der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_INJ_PU'], der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_INJ_PU'])
            q_max_abs = der_file.NP_VA_MAX * np.interp(p_desired_kw/der_file.NP_P_MAX, der_file.NP_Q_CAPABILITY_BY_P_CURVE['P_Q_ABS_PU'], der_file.NP_Q_CAPABILITY_BY_P_CURVE['Q_MAX_ABS_PU'])
            q_limited_kvar = min(q_max_inj, max(-q_max_abs, q_limited_qp_kvar))

        else:
            # undefined Q control mode
            p_limited_kw = p_desired_kw
            q_limited_kvar = 0
        return p_limited_kw, q_limited_kvar




