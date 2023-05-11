module prv32_ALU(
	input   wire [31:0] a, b,
	input   wire [4:0]  shamt,
	output  reg  [31:0] r,
	output  wire        cf, zf, vf, sf,
	input   wire [3:0]  alufn
);
    wire [31:0] as, bs;
    wire [31:0] add, sub, op_b, rem, remu;
    wire [63:0] mul, div, mulhsu, mulhu, divu;
    wire cfa, cfs;
    //remainder rm(.a(as), .b(bs), .rem(rem));
    //remainder rmu (.a(a), .b(b), .rem(remu));
    assign as = $signed(a);
    assign bs = $signed(b);
    assign mul = as*bs;
    assign mulhsu = as*b;
    assign mulhu = as*bs;
    assign div = as/bs;
    assign divu = a/b;
    assign op_b = (~b);
    
    assign {cf, add} = alufn[0] ? (a + op_b + 1'b1) : (a + b);
    
    assign zf = (add == 0);
    assign sf = add[31];
    assign vf = (a[31] ^ (op_b[31]) ^ add[31] ^ cf);
    
    wire[31:0] sh;
    Shift shifter0(.a(a), .shamt(shamt), .type(alufn[1:0]),  .r(sh));
    
    always @ * begin
        r = 0;
        (* parallel_case *)
        case (alufn)
            // arithmetic
            5'b000_00 : r = add;
            5'b000_01 : r = add;
            5'b000_11 : r = b;
            //logic
            5'b001_00:  r = a | b;
            5'b001_01:  r = a & b;
            5'b001_11:  r = a ^ b;
            //Shift
            5'b010_00:  r=sh;
            5'b010_01:  r=sh;
            5'b010_10:  r=sh;
            //slt & sltu
            5'b011_01:  r = {31'b0,(sf != vf)}; 
            5'b011_11:  r = {31'b0,(~cf)};  
            //mult
            `ALU_MUL : r = mul[31:0];         //MUL
            `ALU_MULH : r = mul[63:32];                 //MULH
            `ALU_MULHSU : r = mulhsu[63:32]  ;            //MULHSU
            `ALU_MULHU : r = mulhu [63:32];            //MULHU
            `ALU_DIV : r = div [31:0];
            `ALU_DIVU : r = divu [31:0];              //DIVU
            //`ALU_REM : r = rem;                 //REM
            //`ALU_REMU : r = remu;                //REMU         	
        endcase
    end
endmodule