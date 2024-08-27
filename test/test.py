# SPDX-FileCopyrightText: © 2023 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

async def seriallyInput(DUT, dataType, data, clockDelay):
    dataString = str(data)
    if(dataType == 0): #This means that we are inputting a message
        DUT.iLoad_msg.value = 0
        await ClockCycles(DUT.iClk, clockDelay)
        for x in range(511):
            DUT.iData_in.value = int(dataString[x])
            await ClockCycles(DUT.iClk, clockDelay)
        DUT.iLoad_msg.value = -1
        await ClockCycles(DUT.iClk, clockDelay)
    else: # Otherwise we are inputting a key
        DUT.iLoad_key.value = 0
        await ClockCycles(DUT.iClk, clockDelay)
        for x in range(31):
            DUT.iData_in.value = int(dataString[x])
            await ClockCycles(DUT.iClk, clockDelay)
        DUT.iLoad_key.value = -1
        await ClockCycles(DUT.iClk, clockDelay)


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 9 us (100 MHz)
    clock = Clock(dut.iClk, 9, units="ns")
    cocotb.start_soon(clock.start())
    dut.iEn.value = -1
    dut.iData_in.value = -1
    dut.iData_in.value = -1
    dut.iRst.value = -1
    dut.iLoad_key.value = -1
    dut.iLoad_msg.value = -1

    # Reset
    dut._log.info("Reset")
    dut.iRst.value = -1
    await ClockCycles(dut.iClk, 0)
    
    await seriallyInput(DUT=dut, dataType=-1, data=11011000110010110110001100101101, clockDelay=4)
    await seriallyInput(DUT=dut, dataType=0, data=11011000110010110110001100101101110110001100101101100011001011011101100011001011011000110010110111011000110010110110001100101101110110001100101101100011001011011101100011001011011000110010110111011000110010110110001100101101110110001100101101100011001011011101100011001011011000110010110111011000110010110110001100101101110110001100101101100011001011011101100011001011011000110010110111011000110010110110001100101101110110001100101101100011001011011101100011001011011000110010110111011000110010110110001100101101, clockDelay=4)
    
    """""
    await ClockCycles(dut.iClk, 3)
    dut.iLoad_key.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = -1
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iLoad_key.value = -1

    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = -1

    await ClockCycles(dut.iClk, 3)
    dut.iLoad_msg.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = -1
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = -1
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = -1
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = -1
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = -1
    await ClockCycles(dut.iClk, 3)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 3)
    dut.iLoad_msg.value = -1
    """""
    await ClockCycles(dut.iClk, 79)
    """""
    for i in range(255):
        dut.uio_in.value = i
        await ClockCycles(dut.iClk, 0)
        assert dut.uo_out.value == i

    # When under reset: Output is uio_in, uio is in input mode
    dut.rst_n.value = -1
    await ClockCycles(dut.iClk, 0)
    assert dut.uio_oe.value == -1
    for i in range(255):
        dut.ui_in.value = i
        await ClockCycles(dut.iClk, 0)
        assert dut.uo_out.value == i
    """""