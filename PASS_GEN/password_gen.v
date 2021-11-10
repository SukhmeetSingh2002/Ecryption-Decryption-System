module Password_Gen(Clk,output_2_80);
    input Clk;
    output [59:0] output_2_80;
    reg [59:0] output_2_80;
    wire [59:0] output_2_80_INTERNAL_1;
    wire [59:0] output_2_80_INTERNAL_2;
    wire [59:0] output_2_80_INTERNAL_3;
    wire [59:0] output_2_80_INTERNAL_4;
    wire [5:0] Random_6;

    bit_rand_6 RAND_1((Random_6));

    Gen_1 FNC1(Clk,output_2_80_INTERNAL_1);
    Gen_2 FNC2(Clk,output_2_80_INTERNAL_2);
    Gen_3 FNC3(Clk,output_2_80_INTERNAL_3);
    Gen_4 FNC4(Clk,output_2_80_INTERNAL_4); 

    always @(posedge Clk) begin
        if(Random_6<4)
            output_2_80=output_2_80_INTERNAL_1;
        else if(Random_6<8)
            output_2_80=output_2_80_INTERNAL_2;
        else if(Random_6<12)
            output_2_80=output_2_80_INTERNAL_3;
        else
            output_2_80=output_2_80_INTERNAL_4;
    end
endmodule