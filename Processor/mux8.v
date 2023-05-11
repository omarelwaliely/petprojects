`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 05/02/2023 11:21:09 AM
// Design Name: 
// Module Name: mux8
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

module mux8 #(parameter n=32)(output reg [n-1:0] Y, input [n-1:0] D0, D1, D2, D3, D4, D5, D6, D7, input S0, S1, S2);

 always @(*) begin
     if (S0 == 0 && S1 == 0 && S2 == 0)
       Y = D0;
     else if (S0 == 0 && S1 == 0 && S2 == 1)
       Y = D1;
     else if (S0 == 0 && S1 == 1 && S2 == 0)
       Y = D2;
     else if (S0 == 0 && S1 == 1 && S2 == 1)
       Y = D3;
     else if (S0 == 1 && S1 == 0 && S2 == 0)
       Y = D4;
     else if (S0 == 1 && S1 == 0 && S2 == 1)
       Y = D5;
     else if (S0 == 1 && S1 == 1 && S2 == 0)
       Y = D6;
     else
       Y = D7;
end
endmodule