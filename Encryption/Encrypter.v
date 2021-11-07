module Encrypter (Clk,data_to_be_encrpt,output_encrypted);
    input Clk;
    input [59:0] data_to_be_encrpt;
    output [77:0] output_encrypted;
    wire [77:0] output_encrypted_INTERNAL_1;
    wire [77:0] output_encrypted_INTERNAL_2;
    wire [77:0] output_encrypted_INTERNAL_3;
    wire [77:0] output_encrypted_INTERNAL_4;
    reg [5:0] Random_6;
    reg [10:0] Random_11;

    bit_rand_6 RAND6((Random_6));
    bit_rand_11 RAND11((Random_11));

    encrypt_function_1 FNC1(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_9(Random_9),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_1));
    encrypt_function_2 FNC2(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_9(Random_9),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_2));
    encrypt_function_3 FNC3(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_9(Random_9),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_3));
    encrypt_function_4 FNC4(.Clk(Clk),.data_1(data_to_be_encrpt),.rand_9(Random_9),.rand_6(Random_6),.outEnc(output_encrypted_INTERNAL_4));

    always @(posedge Clk) 
    begin    
        if(/*Something*/)
            output_encrypted=output_encrypted_INTERNAL_1;
        else if(/*Something*/)
            output_encrypted=output_encrypted_INTERNAL_2;
        else if(/*Something*/)
            output_encrypted=output_encrypted_INTERNAL_3;
        else if(/*Something*/)
            output_encrypted=output_encrypted_INTERNAL_4;

    end
endmodule