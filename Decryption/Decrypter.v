module Decrypter (Clk,data_to_be_decrypt,output_decrypted);
    input Clk;
    input [77:0] data_to_be_decrypt;
    output [59:0] output_decrypted;
    reg [59:0] output_decrypted_INTERNAL_1;
    reg [59:0] output_decrypted_INTERNAL_2;
    reg [59:0] output_decrypted_INTERNAL_3;
    reg [59:0] output_decrypted_INTERNAL_4;
    decrypt_function_1 FNC1(.Clk(Clk),.data_1(data_to_be_decrypt),.outDec(output_decrypted_INTERNAL_1));
    decrypt_function_2 FNC2(.Clk(Clk),.data_1(data_to_be_decrypt),.outDec(output_decrypted_INTERNAL_2));
    decrypt_function_3 FNC3(.Clk(Clk),.data_1(data_to_be_decrypt),.outDec(output_decrypted_INTERNAL_3));
    decrypt_function_4 FNC4(.Clk(Clk),.data_1(data_to_be_decrypt),.outDec(output_decrypted_INTERNAL_4));

    always @(posedge Clk) 
    begin    
        if(/*Something*/)
            output_decrypted=output_decrypted_INTERNAL_1;
        else if(/*Something*/)
            output_decrypted=output_decrypted_INTERNAL_2;
        else if(/*Something*/)
            output_decrypted=output_decrypted_INTERNAL_3;
        else if(/*Something*/)
            output_decrypted=output_decrypted_INTERNAL_4;

    end
endmodule