`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/28/2023 04:20:13 PM
// Design Name: 
// Module Name: RegisterFile
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module RegisterFile#(parameter n = 32 , m = 5 )(input clock, input reset, input Regwrite,
    input [m-1:0]readRegOne,input [m-1:0]readRegTwo, input [m-1:0]writeReg,
    input [n-1:0]writeData, output [n-1:0]readDataOne, output [n-1:0] readDataTwo);
    genvar i;
    wire [n-1:0] Q [n-1:0];
    reg [n-1:0]load ;
    always @(*)
    begin
        load =32'd0 ;
        if (Regwrite && writeReg!=0)  load [writeReg]= 1;
    end
    assign readDataTwo= Q[readRegTwo];
    assign readDataOne= Q[readRegOne];
    generate
        for (i = 0; i<32; i=i+1)begin
            nbitRegister x1(.clk(clock), .rst(reset),.load(load[i]) ,.D(writeData), .Q(Q[i]));
        end
    endgenerate
endmodule





