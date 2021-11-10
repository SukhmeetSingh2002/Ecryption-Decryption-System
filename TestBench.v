`include "./Solver.v"
`include "./PASS_GEN/password_gen.v"
`include "./PASS_GEN/Gen_1.v"
`include "./PASS_GEN/Gen_2.v"
`include "./PASS_GEN/Gen_3.v"
`include "./PASS_GEN/Gen_4.v"
`include "./Decryption/Decrypter.v"
`include "./Encryption/Encrypter.v"
`include "./Encryption/encfunction1.v"
`include "./Encryption/encfunction2.v"
`include "./Encryption/encfunction3.v"
`include "./Encryption/encfunction4.v"
`include "6_bit_rand.v"
`include "11_bit_rand.v"
`include "./Decryption/dfunction4.v"
`include "./Decryption/dfunction3.v"
`include "./Decryption/dfunction2.v"
`include "./Decryption/dfunction1.v"
module TestBench ();
    reg [59:0] InputDataRaw;
    reg [77:0] InputDataEnc;
    wire [77:0] OutputDataEnc;
    wire [59:0] OutputDataRaw;

    Solver SOL(.Clk(Clk),.data_1_80(InputDataRaw),.data_2_96(InputDataEnc),.output_1_96(OutputDataEnc),.output_2_80(OutputDataRaw));
endmodule