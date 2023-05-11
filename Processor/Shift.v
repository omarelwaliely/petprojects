`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/21/2023 04:36:20 PM
// Design Name: 
// Module Name: Shift
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

module Shift#(parameter n= 32,m=5)(input [n-1:0]a, input [m-1:0] shamt,input [1:0] type ,output reg [n-1:0]r);
    always@(*) begin
        case(type)
            2'b00: r = a >>shamt;//maybe needs to be signed
            2'b01: r = a<<shamt;
            2'b10: r = $signed(a)>>>shamt;
            default: r = a;
        endcase
    end
endmodule
