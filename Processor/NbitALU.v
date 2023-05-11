`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/28/2023 03:04:16 PM
// Design Name: 
// Module Name: NbitALU
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


module NbitALU #(parameter n=32)(input [n-1:0]A, input [n-1:0]B, input [3:0]select, output reg [n-1:0]C ,output flag);
    wire [n-1:0] out;

    RCA x(select[2],A,( select[2]? (~B):B)  ,out);


    always @(*) begin
        case(select)
            4'b0010: C= out;
            4'b0110: C= out;
            0: C = A & B;
            1: C = A | B;
            default C=0;
        endcase
    end

    assign flag = ~|C;

endmodule
