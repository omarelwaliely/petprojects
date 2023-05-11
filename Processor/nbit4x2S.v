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


module Mulfour#(parameter n=32)(input [n-1:0]D1,input [n-1:0]D0,input [n-1:0]D2,input [n-1:0]D3,input s0,s1, output [n-1:0]Y);
    assign Y = s1 ? (s0 ? D3 : D2) : (s0 ? D1 : D0); 
endmodule