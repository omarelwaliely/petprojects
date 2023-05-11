`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/27/2023 08:33:21 PM
// Design Name: 
// Module Name: HazardDetectionUnit
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


module HazardDetectionUnit(
    input [4:0] IF_ID_RegRs1,IF_ID_RegRs2, ID_EX_RegRd, input ID_EX_MemRead,
    output reg stall);
    
    always@(*)begin
    
        if( ((IF_ID_RegRs1 == ID_EX_RegRd) || (IF_ID_RegRs2 == ID_EX_RegRd)) 
        && (ID_EX_MemRead != 0) && (ID_EX_RegRd != 0))
            stall = 1;
        else
            stall = 0;
    end
    
endmodule
