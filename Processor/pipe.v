`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/04/2023 12:45:16 PM
// Design Name: 
// Module Name: pipe
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
//Branch MemRead MemtoReg ALUOp MemWrite ALUSrc RegWrite

//input [1:0]ledSel, input [3:0]ssdSel, input SSDClock, output reg [15:0] LED, output [3:0] AN, output [6:0] ssd


//module Mulfour#(parameter n=32)(input [n-1:0]D1,input [n-1:0]D0,input [n-1:0]D2,input [n-1:0]D3,input s0,s1, output [n-1:0]Y);
//    assign Y = s1 ? (s0 ? D3 : D2) : (s0 ? D1 : D0); 
//endmodule

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

module pipe (input clock, input rst,input [1:0]ledSel, input [3:0]ssdSel, input SSDClock, 
             output reg [15:0] LED, output [3:0] AN, output [6:0] ssd);
wire [31:0] pcout;
wire [31:0] init = 0;
wire load = 1;
wire [31:0] imOut;
//Inst[6-2] random, jalr, lsbit1, lsbit2, lsbit3, Branch MemRead MemtoReg ALUOp MemWrite ALUSrc RegWrite jumpwrite
wire [4:0] inputReadReg1 = IF_ID_Inst[19:15];
wire [4:0] inputReadReg2 = IF_ID_Inst[24:20];
wire [4:0] inputWriteReg =  IF_ID_Inst[11:7];
wire regWrite = MEM_WB_Ctrl[1] ;
wire jalrSignal= EX_MEM_Ctrl[12];
wire [31:0]writeDataMux;
wire [31:0] readData1;
wire [31:0] readData2;
wire [31:0] igOut;
wire [14:0] controlOut;
wire ALUSrc = ID_EX_Ctrl[2];
wire [31:0] rFMuxOut;
wire [3:0] ALUControlOut;
wire [31:0] ALUOut;
wire ALUFlag;
wire [31:0] SLOut;
wire memRead= EX_MEM_Ctrl[7];
wire memWrite = EX_MEM_Ctrl[3];
wire MemtoReg= MEM_WB_Ctrl[6];
wire branch= EX_MEM_Ctrl[8];
wire lsbit3= EX_MEM_Ctrl[9];
wire lsbit2= EX_MEM_Ctrl[10];
wire lsbit1= EX_MEM_Ctrl[11];
wire [31:0] DMOut;
reg [12:0] boardout;
wire [31:0] ShiftAddOut;
wire [31:0] pcAddOut;
wire [31:0] branchMuxOut;
wire[31:0] MulFUAOut;
wire[31:0] MulFUBOut;
wire[14:0] idexctrlout;
wire andout = ALUFlag & branch;
wire [4:0] shiftAmount = rFMuxOut[4:0];
wire forwardA, forwardB;
wire cFlag, vFlag, sFlag,zFlag,ebranch,repeatbranch;
wire [31:0] ID_EX_PC,ID_EX_pcAddOut, ID_EX_RegR1, ID_EX_RegR2, ID_EX_Imm;
wire [14:0] ID_EX_Ctrl;
wire [31:0] ID_EX_Func;
wire [31:0] datain;
wire [4:0] ID_EX_Rs1, ID_EX_Rs2, ID_EX_Rd;
wire [31:0] IF_ID_pcAddOut, IF_ID_PC, IF_ID_Inst;
wire [31:0] EX_MEM_BranchAddOut, EX_MEM_ALU_out, EX_MEM_RegR2,EX_MEM_PC,EX_MEM_Func,EX_MEM_pcAddOut;
wire [14:0] EX_MEM_Ctrl;
wire [4:0] EX_MEM_Rd;
wire EX_MEM_Zero,EX_MEM_c,EX_MEM_s,EX_MEM_v;
wire [31:0] MEM_WB_Mem_out, MEM_WB_ALU_out, MEM_WB_PC,MEM_WB_BranchAddOut,MEM_WB_pcAddOut;
wire [14:0] MEM_WB_Ctrl;
wire [4:0] MEM_WB_Rd;
wire [1:0] Ex_AluOp = ID_EX_Ctrl [5:4]; 



RCA pcAdd(.cin(32'd0),.a(pcout),.b(32'd4),
          .sum(pcAddOut));

nbitRegister pc(.clk(clock), .rst(rst), .load(!repeatbranch), .D( branchMuxOut), .Q(pcout)); 


//IF/ID
nbitRegister #(400) IF_ID (.clk(!clock),.rst(rst),.load(1'b1),.D({pcout,pcAddOut, DMOut}),
                           .Q({IF_ID_PC,IF_ID_pcAddOut,IF_ID_Inst}) );

//Control Hazard MUX
Mul idexctrl(.D1(32'd0),.D0(controlOut),.S(andout || repeatbranch || ebranch), 
             .Y(idexctrlout));
             
RegisterFile rF(.clock(!clock), .reset(rst), .Regwrite(regWrite),
    .readRegOne(inputReadReg1),.readRegTwo(inputReadReg2), .writeReg(MEM_WB_Rd),
    .writeData(writeDataMux), .readDataOne(readData1), .readDataTwo(readData2));

rv32_ImmGen ig( .IR(IF_ID_Inst), 
                .Imm(igOut));

ControlUnit cu(.instruction(IF_ID_Inst ), 
               .out(controlOut)); 

//ID/EX
nbitRegister #(400) ID_EX (.clk(clock),.rst(rst),.load(1'b1),.D({idexctrlout, IF_ID_PC, IF_ID_pcAddOut, readData1, readData2, igOut, IF_ID_Inst,inputReadReg1, inputReadReg2, IF_ID_Inst[11:7]}), 
                            .Q({ID_EX_Ctrl,ID_EX_PC,ID_EX_pcAddOut,ID_EX_RegR1,ID_EX_RegR2,ID_EX_Imm, ID_EX_Func,ID_EX_Rs1, ID_EX_Rs2, ID_EX_Rd}) );
//MUX for ALU Input 1
Mul MulFUA(.D1(writeDataMux),.D0(ID_EX_RegR1),.S(forwardA), 
            .Y(MulFUAOut));
            
//MUX for ALU Input 2 (data hazard)
Mul MulFUB(.D1(writeDataMux),.D0(ID_EX_RegR2),.S(forwardB), 
            .Y(MulFUBOut));
            
//MUX for ALU Input 2
Mul rFMux(.D1(ID_EX_Imm),.D0(MulFUBOut),.S(ALUSrc ), 
            .Y(rFMuxOut));
            
ALUControl ALUcont(.inst(ID_EX_Func), .op(Ex_AluOp), 
                    .selection(ALUControlOut));
prv32_ALU ALUnew (.a($signed(MulFUAOut)), .b($signed(rFMuxOut)), .shamt(shiftAmount), .alufn(ALUControlOut), 
                    .r(ALUOut),.cf(cFlag), .zf(zFlag), .vf(vFlag), .sf(sFlag));
RCA shiftAdd(.cin(32'd0),.a(ID_EX_PC),.b(ID_EX_Imm), 
                .sum(ShiftAddOut));

//EX/MEM
nbitRegister #(400) EX_MEM (.clk(!clock),.rst(rst),.load(1'b1),
                            .D({ID_EX_PC,ID_EX_pcAddOut,ID_EX_Func,ID_EX_Ctrl,ShiftAddOut,zFlag, cFlag, sFlag, vFlag,ALUOut,ID_EX_RegR2,ID_EX_Rd}),
                            .Q({EX_MEM_PC,EX_MEM_pcAddOut,EX_MEM_Func,EX_MEM_Ctrl, EX_MEM_BranchAddOut, EX_MEM_Zero,EX_MEM_c,EX_MEM_s,EX_MEM_v,EX_MEM_ALU_out,EX_MEM_RegR2, EX_MEM_Rd}) );

BranchUnit BU(.inst(EX_MEM_Func), .zf(EX_MEM_Zero), .cf(EX_MEM_c), .vf(EX_MEM_v), .sf(EX_MEM_s), 
                .branch(ALUFlag),.ebranch(ebranch),.repeatbranch(repeatbranch));
mux8 branchmuxe(.Y(branchMuxOut), 
                .D0(pcAddOut), .D1(EX_MEM_BranchAddOut), .D2(EX_MEM_BranchAddOut), .D3(EX_MEM_ALU_out), .D4(pcout), .D5(32'd0), .D6(32'd0), .D7(pcout), .s0(andout), .s1(EX_MEM_Ctrl[12]), .s2(ebranch));

//MEM/WB
nbitRegister #(400) MEM_WB (.clk(clock),.rst(rst),.load(1'b1),
                             .D({EX_MEM_PC,EX_MEM_pcAddOut,EX_MEM_Ctrl,EX_MEM_BranchAddOut,DMOut, EX_MEM_ALU_out, EX_MEM_Rd}),
                                .Q({MEM_WB_PC,MEM_WB_pcAddOut,MEM_WB_Ctrl,MEM_WB_BranchAddOut,MEM_WB_Mem_out, MEM_WB_ALU_out,MEM_WB_Rd}) );

Mul dataorpc(.D1(pcout),.D0(EX_MEM_ALU_out),.S(clock), .Y(datain));

dataMem DM(.clk(clock), .MemRead(memRead), .MemWrite(memWrite),.addr(datain), .data_in(EX_MEM_RegR2),.lsbit1(lsbit1), .lsbit2(lsbit2), .lsbit3(lsbit3), 
                        .data_out(DMOut));
//MUX for writing to register
Mulfour writeMux(.D1(MEM_WB_Mem_out),.D0(MEM_WB_ALU_out),.D2(MEM_WB_BranchAddOut),.D3(MEM_WB_pcAddOut),.s0(MemtoReg),.s1(MEM_WB_Ctrl[0]), 
                    .Y(writeDataMux));

forwardingUnit FU(.ID_EX_R1(ID_EX_Rs1), .ID_EX_R2(ID_EX_Rs2), .MEM_WB_RegWrite(MEM_WB_Ctrl[1]), .MEM_WB_Rd(MEM_WB_Rd), .EX_MEM_RegWrite(EX_MEM_Ctrl[1]), .EX_MEM_Rd(EX_MEM_Rd), .forwardA(forwardA), .forwardB(forwardB));


Four_Digit_Seven_Segment_Driver FDSS(.clk(SSDClock),.num(boardout),.Anode(AN),.LED_out(ssd)
 );
 
always@(*)
case (ledSel) 
2'b00: LED = DMOut[15:0];
2'b01: LED = DMOut[31:16];
2'b10: LED = {controlOut,ALUControlOut,andout,ALUFlag};
endcase

always@(*)
case (ssdSel) 
4'b0000: boardout = pcout;
4'b0001: boardout = pcAddOut;
4'b0010: boardout = ShiftAddOut;
4'b0011: boardout = branchMuxOut;
4'b0100: boardout = readData1;
4'b0101: boardout = readData2;
4'b0110: boardout = writeDataMux;
4'b0111: boardout = igOut;
4'b1000: boardout = SLOut;
4'b1001: boardout = rFMuxOut;
4'b1010: boardout = ALUOut;
4'b1011: boardout = DMOut;
4'b1100: boardout = MEM_WB_Rd;
default: boardout = 1'd0;
endcase


endmodule
