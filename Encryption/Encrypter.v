module Encrypter (Clk,data_to_be_encrpt,output_encrypted);
    input Clk;
    input [59:0] data_to_be_encrpt;
    output [77:0] output_encrypted;
    reg [77:0] output_encrypted;
    wire [77:0] output_encrypted_INTERNAL_1;
    wire [77:0] output_encrypted_INTERNAL_2;
    wire [77:0] output_encrypted_INTERNAL_3;
    wire [77:0] output_encrypted_INTERNAL_4;
    wire [5:0] Random_6;
    wire [10:0] Random_11;

    bit_rand_6 RAND6((Random_6));
    bit_rand_11 RAND11((Random_11));

    encrypt_function_1 FNC1(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_11(Random_11),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_1));
    encrypt_function_2 FNC2(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_11(Random_11),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_2));
    encrypt_function_3 FNC3(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_11(Random_11),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_3));
    encrypt_function_4 FNC4(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_11(Random_11),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_4));

    always @(posedge Clk) 
    begin    
        if(Random_6<16)
            output_encrypted=output_encrypted_INTERNAL_1;
        else if(Random_6<32)
            output_encrypted=output_encrypted_INTERNAL_2;
        else if(Random_6<48)
            output_encrypted=output_encrypted_INTERNAL_3;
        else if(Random_6<64)
            output_encrypted=output_encrypted_INTERNAL_4;

    end
endmodule