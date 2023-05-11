`timescale 1ns / 1ps
`include "defines.v"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/12/2023 01:18:06 PM
// Design Name: 
// Module Name: BranchUnit
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


module BranchUnit(input [31:0]inst, input zf, cf, vf,sf, output reg branch,output reg ebranch, output reg repeatbranch);
    reg test;
    initial begin
        test = 0;
    end
    wire [2:0] func3 = inst[14:12];
    wire [4:0] opcode = inst[6:2];
    always@(*) begin
        if(opcode == `OPCODE_Branch) begin
            case(func3)
                `BR_BEQ:if(zf)branch =1;else branch=0;
                `BR_BNE:if(~zf)branch =1;else branch=0;
                `BR_BLT:if(sf!=vf)branch =1;else branch=0;
                `BR_BGE:if(sf==vf)branch =1;else branch=0;
                `BR_BLTU:if(~cf)branch =1;else branch=0;
                `BR_BGE:if(cf)branch =1;else branch=0;
                default:branch =0;
            endcase
        end
        else if(opcode == `OPCODE_JAL || `OPCODE_JALR) branch =1;
        else branch =0;
        if(test ==0) begin
            if(opcode ==5'b11100 || opcode ==5'b00011) begin
                ebranch =1;
                if  (opcode ==5'b00011) begin repeatbranch =1;
                    test=1;
                end
                else begin
                    repeatbranch =0; end
            end
            else begin ebranch =0;
                repeatbranch =0;
            end
        end
        if(test==1) begin ebranch =1;
            repeatbranch =1;
        end
    end

endmodule
