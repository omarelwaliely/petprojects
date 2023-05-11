`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/26/2023 10:11:53 AM
// Design Name: 
// Module Name: ImmGen
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


module ImmGen (output reg [31:0] gen_out, input [31:0] inst);
    wire [6:0] opcode = inst[6:0];
    wire [4:0] rd_Imm = inst[11:7]; //rd or imm0:4 or imm 11 4:1
    wire [2:0] func3 = inst[14:12];
    wire [4:0] rsOne = inst[19:15];
    wire [4:0] rsTwo_Imm = inst[24:20]; //rs2 or imm0:4
    wire [6:0] func7_Imm = inst[31:25]; //func7 or imm11:5 or imm 5:10 and 12



    always @* begin
        if ((opcode == 7'b0000011) && (func3 == 3'b010)) begin //we are in lw case
            gen_out = {{20{inst[31]}},func7_Imm, rsTwo_Imm};
        end else if ((opcode == 7'b0100011) && (func3 == 3'b010)) begin  //we are in sw case
            gen_out = {func7_Imm, rd_Imm};
        end else if ((opcode == 7'b1100011) && (func3 == 3'b000)) begin
            gen_out = {inst[31], inst[7], inst[30:25], inst[11:8]};
        end else begin
            gen_out = 0; //in case of a function that doesnt exist or one with no immediate we can default to 0;
        end
    end
endmodule 
