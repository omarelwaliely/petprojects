`timescale 1ns / 1ps
`include "defines.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/01/2023 12:55:40 PM
// Design Name: 
// Module Name: ALUControl
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


`timescale 1ns / 1ps
`include "defines.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/01/2023 12:55:40 PM
// Design Name: 
// Module Name: ALUControl
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


module ALUControl(
    input [31:0] inst, 
    input [1:0]op, 
    output reg[4:0]selection);
    
    wire [5:0] concat = {op, inst[14:12],inst[30]};
    always@(*)begin
       //load and branch
        if (op == 2'b00) selection = `ALU_ADD; //lw maybe wrong
        else if (op == 2'b01) selection = `ALU_SUB; //branch maybe wrong
        else if (op == 2'b11) selection = `ALU_ADD;

        //r-type

        else if (op == 2'b10 && inst[14:12] == 3'b000 && inst[30] == 1'b0) selection = `ALU_ADD;
        else if (op == 2'b10 && inst[14:12] == 3'b000 && inst[30] == 1'b1) selection = `ALU_SUB;
        else if (op == 2'b10 && inst[14:12] == 3'b111 && inst[30] == 1'b0) selection = `ALU_AND;
        else if (op == 2'b10 && inst[14:12] == 3'b110 && inst[30] == 1'b0) selection = `ALU_OR;
        else if (op == 2'b10 && inst[14:12] == 3'b100 && inst[30] == 1'b0) selection = `ALU_XOR;
        else if (op == 2'b10 && inst[14:12] == 3'b001 && inst[30] == 1'b0) selection = `ALU_SLL;
        else if (op == 2'b10 && inst[14:12] == 3'b101 && inst[30] == 1'b0) selection = `ALU_SRL;
        else if (op == 2'b10 && inst[14:12] == 3'b101 && inst[30] == 1'b1) selection = `ALU_SRA;
        else if (op == 2'b10 && inst[14:12] == 3'b010 && inst[30] == 1'b0) selection = `ALU_SLT;
        else if (op == 2'b10 && inst[14:12] == 3'b011 && inst[30] == 1'b0) selection = `ALU_SLTU;
        else if (op == 2'b10 && inst[14:12] == 3'b000 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_MUL; //
        else if (op == 2'b10 && inst[14:12] == 3'b001 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_MULH; //
        else if (op == 2'b10 && inst[14:12] == 3'b010 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_MULHSU; //
        else if (op == 2'b10 && inst[14:12] == 3'b011 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_MULHU; //
        else if (op == 2'b10 && inst[14:12] == 3'b100 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_DIV; //
        else if (op == 2'b10 && inst[14:12] == 3'b101 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_DIVU; //
        else if (op == 2'b10 && inst[14:12] == 3'b110 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_REM; //
        else if (op == 2'b10 && inst[14:12] == 3'b111 && inst[25] == 1'b1 && inst[30] == 1'b0) selection = `ALU_REMU; //



        
        else selection =4'b1111; // else set to 15 we can probably change this later but for now its the default if a user puts anything else
    end
endmodule


