`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/18/2022 01:18:07 PM
// Design Name: 
// Module Name: sources
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

module refresh(input refresh_clock, output reg[1:0] refreshcount = 0);
always@(posedge refresh_clock)
refreshcount <= refreshcount +1;
endmodule


module bcd(input[13:0]bcd,input cond, output [7:0]out);
reg[7:0] out;
always @(bcd)
begin
    if (~cond) begin
        case(bcd)
            4'd0:out = 8'b00000011;
            4'd1:out = 8'b10011111;
            4'd2:out = 8'b00100101;
            4'd3:out = 8'b00001101;
            4'd4:out = 8'b10011001;
            4'd5:out = 8'b01001001;
            4'd6:out = 8'b01000001;
            4'd7:out = 8'b00011111;
            4'd8:out = 8'b00000001;
            4'd9:out = 8'b00001001;
            4'd10:out = 8'b11111101;
            default: out = 8'b11111111;
        endcase
    end
    else begin
    case(bcd)
                4'd0:out = 8'b00000010;
                4'd1:out = 8'b10011110;
                4'd2:out = 8'b00100100;
                4'd3:out = 8'b00001100;
                4'd4:out = 8'b10011000;
                4'd5:out = 8'b01001000;
                4'd6:out = 8'b01000000;
                4'd7:out = 8'b00011110;
                4'd8:out = 8'b00000000;
                4'd9:out = 8'b00001000;
                default: out = 8'b11111110;
            endcase
            end
end
endmodule

module anodec(input [1:0] refreshcount, output reg [3:0] anode = 0);
always @(refreshcount)
begin
    case(refreshcount)
        2'b00: anode = 4'b1110;
        2'b01: anode = 4'b1101;
        2'b10: anode = 4'b1011;
        2'b11: anode = 4'b0111;
        endcase
        end
  endmodule
  
module  clockdivider#(parameter n = 50000)(input clk, rst, output reg clk_out = 0);
reg [31:0] count = 0; // Big enough to hold the maximum possible value
// Increment count
initial begin
 count = 0;
end
    always @ (posedge(clk)) begin // Asynchronous Reset
           
        if (count == n-1)
            count <= 32'b0;
        else
            count <= count + 1;
        end
always @(posedge(clk)) begin
if(count == n-1)
clk_out <= ~clk_out;
else
clk_out <= clk_out;
end
endmodule

module dflip(input DFF_CLOCK, D, output reg Q);

    always @ (posedge DFF_CLOCK) begin
        Q <= D;
    end

endmodule

module debounce(input pb_1,clk,output pb_out);
wire Q1,Q2,Q2_bar,Q0;
dflip d0(clk, pb_1,Q0 );
dflip d1(clk, Q0,Q1 );
dflip d2(clk, Q1,Q2 );
assign Q2_bar = ~Q2;
assign pb_out = Q1 & Q2_bar;
endmodule



module board(a,b,c,d, clock, add, sub, mul, div, reset, out, enable);
    wire [1:0]counter,clockdivided;
    reg [13:0] num1,org1 =0,num2,num3,num4,org2 = 0,org3 = 0,org4 = 0,num;
    integer cond =0, condin =0, condf =0;
    wire da,db,dc,dd;
    integer i = 0, isn=0;
    initial num1 =0;
    wire [13:0] adl,adr,adg; 
    reg[13:0] adf;
    reg[13:0] addedf = 0,addeds,subdf,subs,multif=0,multis,divf,divs;
    input a,b,c,d,reset,add,sub,mul,div,clock;
    output [7:0] out; 
    output[3:0] enable; 
    clockdivider g(clock, reset, clockdivided);
    refresh d3(clockdivided, counter);
    anodec as(counter, enable);
    debounce bingbong(a,clockdivided,da);
    debounce wahoo(b,clockdivided,db);
    debounce bbg(c,clockdivided,dc);
    debounce eyo(d,clockdivided,dd);
    assign adl = (num4*10 + num3) + (num2*10 + num1);
    assign adr = (num4*10 + num3) * (num2*10 + num1);
    assign adg = (num4*10 + num3) / (num2*10 + num1);
    always@(*)begin
    if((num4*10 + num3) > (num2*10+num1))begin
    adf <= (num4*10 + num3) - (num2*10 + num1);
    isn<=0;
    end
    else begin
    adf <= (num2*10 + num1)-(num4*10 + num3);
    isn<=1;
    end
    end
   always@(posedge (clockdivided))begin

       if (reset)begin
       condin<=1;
       num1 <= 0;
       num2 <= 0;
       num3 <= 0;
       num4 <= 0;
       org1 <= 0;
       org2 <= 0;
       org3 <= 0;
       org4 <= 0;
       i<=0;
       condin<=0;
       
       end
    
    
    if(da==1) begin
        if(num1 !=9)begin
            num1 <= num1+1;
            org1 <= num1+1; 
        end
        else begin
            num1<= 0;
            org1<= 0;
        end
    end
    if(db==1) begin
        if(num2 !=9)begin
            num2 <= num2+1;
            org2<= num2+1;
        end
        else begin
            num2<= 0;
            org2 <= 0;
        end
    end
    if(dc==1) begin
        if(num3 !=9)begin
            num3 <= num3+1;
            org3 <=num3 +1;
        end
        else begin
            num3<= 0;
            org3 <= 0;
        end
    end
    if(dd==1) begin
         if(num4 !=9)begin
            num4 <= num4+1;
            org4 <= num4+1;
         end
         else begin
            num4<= 0;
            org4<= 0;
         end
    end
    if(add & ~mul & ~div & ~sub) begin
        condin =0;
        if(i==0)begin
            addedf = adl;
            num1 = addedf%10;
            num2 = addedf/10%10;
            num3 = (addedf/100)%10;
            num4 = (addedf/1000)%10;
            i=1;
       end
    end
//    else begin
//    condin =1;
//        i=0;
//        num1 =org1;
//        num2 = org2;
//        num3 = org3;
//        num4 = org4;
//    end
    
    else if(mul & ~add & ~div & ~sub) begin
     condin =0;
        if(i==0)begin
            multif = adr;
            num1 = multif%10;
            num2 = multif/10%10;
            num3 = (multif/100)%10;
            num4 = (multif/1000)%10;
            i=1;
        end
    end
    else if(div & ~add & ~mul & ~sub) begin
         condin =0;
            if(i==0)begin
                divf = adg;
                num1 = divf%10;
                num2 = divf/10%10;
                num3 = (divf/100)%10;
                num4 = (divf/1000)%10;
                i=1;
            end
        end
         else if(sub & ~add & ~mul & ~div) begin
                condin =0;
                   if(i==0)begin
                       subdf = adf;
                       num1 = subdf%10;
                       num2 = subdf/10%10;
                       if(isn)begin
                       num3 = 10;
                       end
                       else
                       num3 = (subdf/100)%10;
                       num4 = 1000;
                       i=1;
                   end
               end
               
        
    else begin
        i=0;
        num1 =org1;
        num2 = org2;
        num3 = org3;
        num4 = org4;
        condin = 1; 
    end
end
   always@(counter)begin
        case(counter)

           2'b00: begin
           num = num1; //first ones
           cond =0;
           end //last ones
           2'b01: begin
           num = num2; //first ones
           cond =0;
           end// last tens
           2'b10: begin
           num = num3; //first ones
           cond =1;
           end
           2'b11: begin
           num = num4; //first ones
           cond =0;
           end//first tens
           default: num = num1;

        endcase
    end
    
    always@(*)begin
if(condin ==1&cond==1)begin
condf = 1;
end
else
condf =0;

end
bcd lk(num,condf,out);
    
endmodule