`include "defines.v"
`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/28/2023 05:47:49 PM
// Design Name: 
// Module Name: ControlUnit
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

//Inst[6-2] random, jalr, lsbit1, lsbit2, lsbit3, Branch MemRead MemtoReg ALUOp MemWrite ALUSrc RegWrite jumpwrite
module ControlUnit(input [31:0] instruction, output reg[14:0] out);
    always@(*)begin
        if(instruction[6:2] == `OPCODE_Arith_R) out = 14'b00000000100010;
        else if(instruction[6:2] == `OPCODE_Load) begin
            if (instruction[14:12]==3'b010)//lw
               out = 14'b00000011000110; //000
            else if (instruction[14:12]==3'b000)//lb
                out = 14'b00001011000110; //001
            else if (instruction[14:12]==3'b001)//lh
                out = 14'b00010011000110; //010
            else if (instruction[14:12]==3'b100)//lbu
                out = 14'b00011011000110; //011
            else if (instruction[14:12]==3'b101)//lhu
                out = 14'b00100011000110; //100
        end
        else if(instruction[6:2] == `OPCODE_Store) begin
        if (instruction[14:12]==3'b010)//sw
                out = 14'b00000000001100; //000
        else if (instruction[14:12]==3'b000)//sb
                out = 14'b00001000001100; //001
        else if (instruction[14:12]==3'b001)//sh
                out = 14'b00010000001100; //010
        
        end
        else if(instruction[6:2] == `OPCODE_Branch) out = 14'b00000100010000;
        else if(instruction[6:2] == `OPCODE_Arith_I) out = 14'b00000000100110;
        else if(instruction[6:2] == `OPCODE_JAL) out = 14'b00000101000011; //changed  from 10
  else if(instruction[6:2] == `OPCODE_JALR) out = 14'b01000101000111;
        else if(instruction[6:2] == `OPCODE_LUI) out = 14'b00000000110110;
        else if(instruction[6:2] == `OPCODE_AUIPC) out = 14'b00000000000111; //jumpwrite is 1 so that the writemux chooses d2
        else if(instruction[6:2] == `OPCODE_HALT) out = 14'b00000100000000; //jumpwrite is 1 so that the writemux chooses d2
        else if(instruction[6:2] == `OPCODE_FENCE) out = 14'b010001000000100; //jumpwrite is 1 so that the writemux chooses d2
        else out = 0;
    end
endmodule
