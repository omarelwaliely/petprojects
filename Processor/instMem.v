module instMem (
    input [5:0] addr, 
    output [31:0] data_out);
    
    reg [31:0] mem [0:63];
    initial begin
      $readmemh("C:/Users/omarelwaliely/milestone3/testfiles/test2.hex",mem);
    end

    assign data_out = mem[addr];
endmodule