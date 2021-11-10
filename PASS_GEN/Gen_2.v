module Gen_2(Clk,output_2_80_INTERNAL_1);
    input Clk;
    output [59:0]output_2_80_INTERNAL_1;
    reg [59:0]output_2_80_INTERNAL_1;
    wire [10:0]Random_11;
    bit_rand_11 RAND11(.rand_11(Random_11));
    always @(posedge Clk) begin
        output_2_80_INTERNAL_1[10:0]=Random_11;
        output_2_80_INTERNAL_1[21:11]=Random_11;
        output_2_80_INTERNAL_1[32:22]=~Random_11;
        output_2_80_INTERNAL_1[43:33]=~Random_11;
        output_2_80_INTERNAL_1[54:44]=Random_11;
        output_2_80_INTERNAL_1[59:55]=Random_11[4:0];
    end
endmodule