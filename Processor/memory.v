`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 03/07/2023 03:41:05 PM
// Design Name: 
// Module Name: dataMem
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


module dataMem( input clk, input MemRead, input MemWrite, input lsbit1, input lsbit2, lsbit3, input [5:0] addr, input [31:0] data_in, output reg[31:0] data_out);
      //reg [31:0] mem [0:63];
    reg [7:0] mem [0:1024];
    localparam [5:0] datamem  = 6'd200;
    initial begin
    {mem[3],mem[2],mem[1],mem[0]}=32'd11;
    {mem[7],mem[6],mem[5],mem[4]}=32'd1;
    {mem[11],mem[10],mem[9],mem[8]}=32'd24;
    $readmemh("C:/Users/Reem Said/MS33/tests/test1.hex",mem);
    end
    always@(*) begin
    if(!clk) begin
        if (MemWrite == 1) begin
            if(lsbit1== 0 && lsbit2 == 0 && lsbit3 ==0)//sw
            {mem[datamem+3], mem[datamem+2], mem[datamem+1], mem[datamem]} = data_in;
            else if(lsbit1== 0 && lsbit2 == 0 && lsbit3 ==1)//sb
            mem[datamem]= data_in;
            else if(lsbit1== 0 && lsbit2 == 1 && lsbit3 ==0)//sh
                 {mem[datamem+1], mem[datamem]}= data_in;
        end
               
        if (MemRead == 1) begin
        if(lsbit1== 0 && lsbit2 == 0 && lsbit3 ==0)//lw
            data_out={mem[datamem+3],mem[datamem+2],mem[datamem+1],mem[datamem]};
        else if(lsbit1== 0 && lsbit2 == 0 && lsbit3 ==1)//lb
             data_out={{24{mem[datamem][7]}},mem[datamem][6:0]};
        else if(lsbit1== 0 && lsbit2 == 1 && lsbit3 ==0)//lh
             data_out= {{16{mem[datamem+1][7]}},mem[datamem+1][6:0],mem[datamem]};
        else if(lsbit1== 0 && lsbit2 == 1 && lsbit3 ==1)//lbu
            data_out=mem[datamem];
        else if(lsbit1== 1 && lsbit2 == 0 && lsbit3 ==0)//lhu
              data_out={mem[datamem+1],mem[datamem]};
        end
        else data_out= 32'dz;
    end
    else
    data_out={mem[addr],mem[addr+1],mem[addr+2],mem[addr+3]};
    end
endmodule