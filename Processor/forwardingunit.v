module forwardingUnit(
    input [4:0] ID_EX_R1, ID_EX_R2, EX_MEM_Rd, MEM_WB_Rd, 
    input EX_MEM_RegWrite, MEM_WB_RegWrite, 
    output reg forwardA, forwardB);
    
    always@(*) begin
    
//        if(EX_MEM_RegWrite!=0 && EX_MEM_Rd!=0 && EX_MEM_Rd==ID_EX_R1)
//            forwardA = 2'b10;
        if(MEM_WB_RegWrite && MEM_WB_Rd!=0 && MEM_WB_Rd == ID_EX_R1)
            forwardA = 1'b1;
        else 
            forwardA = 1'b0;
            
            
//        if(EX_MEM_RegWrite!=0 && EX_MEM_Rd!=0 && EX_MEM_Rd==ID_EX_R2)
//            forwardB = 2'b10;
        if(MEM_WB_RegWrite && MEM_WB_Rd!=0 && MEM_WB_Rd == ID_EX_R2)
            forwardB = 1'b1;
        else 
            forwardB = 1'b0;
            
    end
endmodule