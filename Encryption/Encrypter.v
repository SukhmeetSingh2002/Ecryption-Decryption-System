module Encrypter (Clk,data_to_be_encrpt,output_encrypted);
    input Clk;
    input [59:0] data_to_be_encrpt;
    output [75:0] output_encrypted;
    reg [5:0] Random_6;
    reg [8:0] Random_9;

    6_bit_rand 6RAND((Random_6));
    9_bit_rand 9RAND((Random_9));

    always @(posedge Clk) 
    begin    
        if(/*Something*/)
            encrypt_function_1 FNC1(.Clk(Clk),.data_1(data_to_be_encrpt),.9_rand(Random_9),.6_rand(Random_6),.outEnc(output_encrypted));
        else if(/*Something*/)
            encrypt_function_2 FNC2(.Clk(Clk),.data_1(data_to_be_encrpt),.9_rand(Random_9),.6_rand(Random_6),.outEnc(output_encrypted));

        else if(/*Something*/)
            encrypt_function_3 FNC3(.Clk(Clk),.data_1(data_to_be_encrpt),.9_rand(Random_9),.6_rand(Random_6),.outEnc(output_encrypted));

        else if(/*Something*/)
            encrypt_function_4 FNC4(.Clk(Clk),.data_1(data_to_be_encrpt),.9_rand(Random_9),.6_rand(Random_6),.outEnc(output_encrypted));

    end
endmodule