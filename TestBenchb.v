`include "./Solver.v"
`include "./PASS_GEN/password_gen.v"
`include "./Decryption/Decrypter.v"
`include "./Encryption/Encrypter.v"
`include "./PASS_GEN/hello.v"
`include "./PASS_GEN/hai.v"

module TestBench ();
    reg [59:0] InputDataRaw;
    reg [75:0] InputDataEnc;
    reg [75:0] OutputDataEnc;
    reg [59:0] OutputDataRaw;

    Solver SOL(.Clk(Clk),.data_1_80(InputDataRaw),.data_2_96(InputDataEnc),.output_1_96(OutputDataEnc),output_2_80(OutputDataRaw))
endmodule