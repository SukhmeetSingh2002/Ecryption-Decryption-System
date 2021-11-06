module decrypt_function_3 (Clk,data_1,outEnc);
    input Clk;
    input [77:0]data_1;
    reg  [10:0]rand_9;
    output outEnc;
    reg outEnc;
    reg [59:0]b;
    reg [60:0]y;
    always @(data_1) begin
        rand_9=data_1[6:16];
        b[0:10]=~rand_9;
        b[11:21]=rand_9;
        b[22:32]=rand_9;
        b[33:43]=~rand_9;
        b[44:54]=rand_9;
        b[55:59]=rand_9[0:4];
        y=data_1[17:77];
        outEnc=y-x;
    end
endmodule

