module encrypt_function_4 (Clk,data_1,outEnc,rand_11,rand_6);
    input Clk;
    input [59:0]data_1;
    input [10:0]rand_11;
    input [5:0]rand_6;
    output [77:0]outEnc;
    reg [77:0]outEnc;
    reg [59:0]b;
    reg [60:0]x;
    always @(posedge Clk) begin
        b[10:0]=rand_11;
        b[21:11]=~rand_11;
        b[32:22]=~rand_11;
        b[43:33]=rand_11;
        b[54:44]=~rand_11;
        b[59:55]=rand_11[4:0];
        x=data_1+b;
        outEnc[66:6]=x;
        outEnc[77:67]=rand_11;
        outEnc[5:0]=rand_6;
    end
endmodule

