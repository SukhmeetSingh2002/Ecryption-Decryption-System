module TestBench ();
    reg [79:0] InputDataRaw;
    reg [95:0] InputDataEnc;
    reg [95:0] OutputDataEnc;
    reg [79:0] OutputDataRaw;

    Solver SOL(.Clk(Clk),.data_1_80(InputDataRaw),.data_2_96(InputDataEnc),.output_1_96(OutputDataEnc),output_2_80(OutputDataRaw))
endmodule