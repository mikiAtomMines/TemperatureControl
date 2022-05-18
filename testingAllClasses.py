"""
Created on Tuesday, April 19, 2022
@author: Sebastian Miki-Silva
"""
import time

import auxiliary
import device_models
import device_type
import simple_pid as pid
from mcculw import ul
from mcculw import enums
from mcculw.enums import InterfaceType


def main():
    # daq = device_models.E_Tc(ip4_address='10.176.42.200', board_number=0)
    # print(daq.temp_ch0)
    # print(daq.number_temp_channels)
    # print(daq.number_da_channels)
    # print(daq.number_ad_channels)
    # print(daq.number_io_channels)
    # daq.set_thermocuple_type(channel=0, new_tc_type='K')
    # print(daq.get_thermocouple_type(channel=0))
    # daq.set_thermocuple_type(channel=0, new_tc_type='K')
    # print(daq.get_thermocouple_type(channel=0))
    #
    # # daq.config_io_channel(0, 'out')
    # # daq.set_bit(chan=0, out=0)
    # # time.sleep(2)
    # # daq.set_bit(chan=0, out=1)
    # # time.sleep(5)
    # # daq.set_bit(chan=0, out=0)
    #
    # daq.config_io_byte(direction='out')
    # daq.set_byte(val=0)
    # print(daq.get_byte())

    # pico = device_models.Model8742(ip4_address='10.176.42.123')
    # auxiliary.testing_model8742(pico)

    # spd = device_models.SPD3303X(ip4_address='10.176.42.121')
    # auxiliary.testing_SPD3303X(spd)


    rga = device_models.SRS100(port='COM7')

    rga.flush_buffers()
    print(rga.idn)
    rga.flush_buffers()

    # print(rga._query_('EC?'))
    # print(rga._query_('EF?'))
    # print('0\n\r')
    # print(rga._query_('EM?'))
    # print(rga._query_('EQ?'))
    # print(rga._query_('ED?'))
    # print(rga._query_('EP?'))
    # print('0\n\r')

    # print('setting RGA filament on')
    # print(rga.set_ionizer_filament_state(state='on'))
    # print('RGA filament is on')
    # print('filament current:')
    # print(rga.get_ionizer_filament_current())
    # time.sleep(5)
    # print()
    #
    # print('setting RGA filament off')
    # print(rga.set_ionizer_filament_state(state='off'))
    # print('RGA filament is off')
    # print('filament current:')
    # print(rga.get_ionizer_filament_current())
    # print(rga.get_status())

    print(rga._command_(cmd='FL'))
    print(rga.status_byte)





    pass


if __name__ == '__main__':
    main()
