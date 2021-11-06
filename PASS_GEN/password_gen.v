module Password_Gen(Clk,output_2_80);
    input Clk;
    output [59:0] output_2_80;
    reg [59:0] output_2_80;
    wire [5:0] Random_6;
    bit_rand_6 RAND_1((Random_6));
    always @(posedge Clk) begin
        if(Random_6<4)
            Gen_1 FNC1(Clk,output_2_80);
        else if(Random_6<8)
            Gen_2 FNC2(Clk,output_2_80);
        else if(Random_6<12)
            Gen_3 FNC3(Clk,output_2_80);
        else
            Gen_4 FNC4(Clk,output_2_80); 
    end
endmodule