module Password_Gen(Clk,output_2_80);
    input Clk;
    output [79:0] output_2_80;
    reg [79:0] output_2_80;
    wire [5:0] Random_6;
    6_bit_rand RAND1(Clk,.6_rand(Random_6));
    always @(posedge Clk) begin
        if(/*Something*/)
            Gen_1 FNC1(Clk,output_2_80);
        else if(/*Something*/)
            Gen_2 FNC2(Clk,output_2_80);
        else if(/*Something*/)
            Gen_3 FNC3(Clk,output_2_80);
        else
            Gen_4 FNC4(Clk,output_2_80); 
    end
endmodule