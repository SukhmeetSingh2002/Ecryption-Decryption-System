module decrypt_function_4 (Clk,data_1,outDec);
    input Clk;
    input [77:0]data_1;
    reg  [10:0]rand_9;
    output [60:0]outDec;
    reg [60:0]outDec;
    reg [59:0]b;
    reg [60:0]y;
    reg [60:0]x;
    always @(data_1) begin
        rand_9=data_1[67:77];
        b[0:4]=rand_9[0:4];
        b[5:15]=~rand_9;
        b[16:26]=~rand_9;
        b[27:37]=rand_9;
        b[38:48]=~rand_9;
        b[49:59]=rand_9;
        y=data_1[6:66];
        x=y-b;
        outDec=x[1:60];
    end
endmodule

