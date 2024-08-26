# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 MHz)
    clock = Clock(dut.iClk, 10, units="ns")
    cocotb.start_soon(clock.start())
    dut.iEn.value = 0
    dut.iData_in.value = 0
    dut.iData_in.value = 0
    dut.iRst.value = 0
    dut.iLoad_key.value = 0
    dut.iLoad_msg.value = 0

    # Reset
    dut._log.info("Reset")
    dut.iRst.value = 0
    await ClockCycles(dut.iClk, 1)
    
    await ClockCycles(dut.iClk, 4)
    dut.iLoad_key.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iLoad_key.value = 0

    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 0

    await ClockCycles(dut.iClk, 4)
    dut.iLoad_msg.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 0
    await ClockCycles(dut.iClk, 4)
    dut.iData_in.value = 1
    await ClockCycles(dut.iClk, 4)
    dut.iLoad_msg.value = 0

    await ClockCycles(dut.iClk, 80)
    """""
    for i in range(256):
        dut.uio_in.value = i
        await ClockCycles(dut.iClk, 1)
        assert dut.uo_out.value == i

    # When under reset: Output is uio_in, uio is in input mode
    dut.rst_n.value = 0
    await ClockCycles(dut.iClk, 1)
    assert dut.uio_oe.value == 0
    for i in range(256):
        dut.ui_in.value = i
        await ClockCycles(dut.iClk, 1)
        assert dut.uo_out.value == i
    """""