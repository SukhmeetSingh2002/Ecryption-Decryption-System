module Solver (Clk,data_1_80,data_2_96,work_2,output_1_96,output_2_80);
    input Clk;
    input [79:0] data_1_80;
    input [95:0] data_1_96;
    input [1:0] work_2;
    output [95:0] output_1_96
    output [79:0] output_2_80
    reg [95:0] output_1_96
    reg [79:0] output_2_80


    always @(posedge Clk) 
    begin 
        if(work_2==2'b00)
            Encryptor ENC(.Clk(Clk),.data_to_be_encrpt(data_1_80),.output_encrypted(output_1_96));
        else if(work_2==2'b01)
            Decryptor DEC(/*tobe done*/)
        else if(work_2==2'b10)
            Password_Gen PASSGEN(.Clk(Clk),.output_2_80(output_2_80))
    end
endmodule