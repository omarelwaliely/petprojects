`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/21/2023 02:49:32 PM
// Design Name: 
// Module Name: nbitRegister
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

module nbitRegister#(parameter n=32)(input clk, input rst, input load, input [n-1:0] D, output [n-1:0] Q);
    genvar i;
    wire [n-1:0]oldQ;
    generate
        for (i=0; i<n; i=i+1) begin
            Mul #(1) x0(.D1(D[i]),.D0(Q[i]),.S(load),.Y(oldQ[i]));
            DFlipFlop x1(clk, rst,oldQ[i],Q[i]);
        end
    endgenerate
endmodule


module DFlipFlop(input clk, input rst, input D, output reg Q);
    always @ (posedge clk or posedge rst)
    if (rst) begin
        Q <= 1'b0;
    end else begin
        Q <= D;
    end
endmodule


//module Mul#(parameter n=32)(input [n-1:0]D1,input [n-1:0]D0,input S, output [n-1:0]Y);
//    assign Y= (S)? D1: D0;
//endmodule

