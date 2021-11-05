module Solver (Clk,data_1_80,data_2_96,work_2,output_1_96,output_2_80);
    input Clk;
    input [59:0] data_1_80;
    input [75:0] data_1_96;
    input [1:0] work_2;
    output [75:0] output_1_96;
    output [59:0] output_2_80;
    reg [75:0] output_1_96;
    reg [59:0] output_2_80;


    always @(posedge Clk) 
    begin 
        if(work_2==2'b00)
            Encrypter ENC(.Clk(Clk),.data_to_be_encrpt(data_1_80),.output_encrypted(output_1_96));
        else if(work_2==2'b01)
            Decrypter DEC(/*tobe done*/)
        else if(work_2==2'b10)
            Password_Gen PASSGEN(.Clk(Clk),.output_2_80(output_2_80))
    end
endmodule