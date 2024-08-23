`default_nettype none
`timescale 1ns / 1ps

module tb();

    
     // Dump the signals to a VCD file. You can view it with gtkwave.
    initial begin
      $dumpfile("tb.vcd");
      $dumpvars(0, tb);
      #1;
    end

    // Testbench signals
    reg iEn;
    reg iData_in;
    reg iClk;
    reg iRst;
    reg iLoad_key;
    reg iLoad_msg;
    wire oClk_slow;
    wire oData_out;
    wire oDone_flag;

    // Instantiate the top module
    tt_um_franco_xor_top uut (

      `ifdef GL_TEST
        .VPWR(1'b1),
        .VGND(1'b0),
      `endif

        .iEn(iEn),
        .iData_in(iData_in),
        .iClk(iClk),
        .iRst(iRst),
        .iLoad_key(iLoad_key),
        .iLoad_msg(iLoad_msg),
        .oClk_slow(oClk_slow),
        .oData_out(oData_out),
        .oDone_flag(oDone_flag)
    );

/*
// Clock generation
initial begin
    iEn = 0;
    iData_in = 0;
    iRst = 0;
    iLoad_key = 0;
    iLoad_msg = 0;
    iClk = 0;
    forever #10 iClk = ~iClk; // 100MHz clock with a period of 10ns
end

// Test stimulus
initial begin
        // Initialize reset
    iRst = 0;
    #10; 
    iRst = 1;
    iEn = 1;
     
    //load a 4 bit key.
    #40 iLoad_key = 1;
    #40 iData_in = 1;
    #40 iData_in = 0;
    #40 iData_in = 1;
    #40 iData_in = 1;
    #40 iLoad_key = 0;
    
    #40 iData_in = 0;
    
    #40 iLoad_msg = 1;
    #40 iData_in = 1;
    #40 iData_in = 0;
    #40 iData_in = 0;
    #40 iData_in = 0;
    #40 iData_in = 1;
    #40 iData_in = 0;
    #40 iData_in = 0;
    #40 iData_in = 1;
    #40 iLoad_msg = 0;
     
    
    
    //Run simulation for some time
    #800;

    // Finish simulation
    $finish;
    end

initial begin
    $monitor("Time: %0t | Key: %b || Message: %b", $time, oData_out, oDone_flag);
end
yuh
*/

endmodule


/*
`timescale 1ns / 1ps

module tb_xor_top();

    // Testbench signals
    reg iEn;
    reg iData_in;
    reg iClk;
    reg iRst;
    reg iLoad_key;
    reg iLoad_msg;
    wire oClk_slow;
    wire oData_out;
    wire oDone_flag;

    // Instantiate the top module
    xor_top uut (
        .iEn(iEn),
        .iData_in(iData_in),
        .iClk(iClk),
        .iRst(iRst),
        .iLoad_key(iLoad_key),
        .iLoad_msg(iLoad_msg),
        .oClk_slow(oClk_slow),
        .oData_out(oData_out),
        .oDone_flag(oDone_flag)
    );


    // Clock generation
initial begin
    iEn = 0;
    iData_in = 0;
    iRst = 0;
    iLoad_key = 0;
    iLoad_msg = 0;
    iClk = 0;
    forever #10 iClk = ~iClk; // 100MHz clock with a period of 10ns
end

// Test stimulus
initial begin
        // Initialize reset
    iRst = 0;
    #10; 
    iRst = 1;
    iEn = 1;
     
    //load a 4 bit key.
    #40 iLoad_key = 1;
    #40 iData_in = 1;
    #40 iData_in = 0;
    #40 iData_in = 1;
    #40 iData_in = 1;
    #40 iLoad_key = 0;
    
    #40 iData_in = 0;
    
    #40 iLoad_msg = 1;
    #40 iData_in = 1;
    #40 iData_in = 0;
    #40 iData_in = 0;
    #40 iData_in = 0;
    #40 iData_in = 1;
    #40 iData_in = 0;
    #40 iData_in = 0;
    #40 iData_in = 1;
    #40 iLoad_msg = 0;
     
    
    
    //Run simulation for some time
    #800;

    // Finish simulation
    $finish;
    end

initial begin
    $monitor("Time: %0t | Key: %b || Message: %b", $time, oData_out, oDone_flag);
end

endmodule
*/