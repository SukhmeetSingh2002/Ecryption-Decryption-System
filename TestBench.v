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
    reg Clk;
    reg [15:0]n;
    reg [15:0]i;
    reg [1:0]w;
    integer ans;
    integer fd;
    integer fw;
    Solver SOL(.Clk(Clk),.data_1_80(InputDataRaw),.data_2_96(InputDataEnc),.work_2(w),.output_1_96(OutputDataEnc),.output_2_80(OutputDataRaw));
    initial begin   
        fd = $fopen("my_file.txt", "r");
        fw = $fopen("out_file.txt", "w"); 
          ans = $fscanf(fd, "%d\n",n);
          for(i=0;i<n;i=i+1)
          begin  
            ans = $fscanf(fd, "%d\n",w); 
            if(w==0)begin
              ans = $fscanf(fd, "%b\n",InputDataRaw); 
              $display("%d",InputDataRaw);
              #30
              $fdisplay(fw,"%b",OutputDataEnc);
            end
            else if (w==1) begin
              ans = $fscanf(fd, "%b\n",InputDataEnc); 
              $display("%d",InputDataEnc);
              #20
              $fdisplay(fw,"%b",OutputDataRaw);
            end
            else if (w==2) begin
              #20
              $fdisplay(fw,"%b",OutputDataRaw);
            end
          end
          #10 $finish;
        $fclose(fd);  
    end
    initial begin
        Clk=1'b0;
    end
    always
        #5 Clk=~Clk;
    initial 
	  begin 
	    $dumpfile("ha.vcd");
	    $dumpvars;
	  end
endmodule