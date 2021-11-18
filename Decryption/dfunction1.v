module decrypt_function_1 (Clk,data_1,outDec);
    input Clk;
    input [77:0]data_1;
    reg  [10:0]rand_9;
    output [59:0]outDec;
    reg [59:0]outDec;
    reg [59:0]b;
    reg [60:0]y;
    reg [60:0]x;
    always @(posedge Clk) begin
        rand_9=data_1[16:6];
        b[10:0]=rand_9;
        b[21:11]=~rand_9;
        b[32:22]=~rand_9;
        b[43:33]=rand_9;
        b[54:44]=~rand_9;
        b[59:55]=rand_9[4:0];
        y=data_1[77:17];
        x=y-b;
        outDec=x[59:0];
    end
endmodule

