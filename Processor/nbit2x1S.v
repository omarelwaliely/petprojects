`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/21/2023 04:09:48 PM
// Design Name: 
// Module Name: nbit2x1S
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


module Mul#(parameter n=32)(input [n-1:0]D1,input [n-1:0]D0,input S, output [n-1:0]Y);
    assign Y= (S)? D1: D0;
endmodule