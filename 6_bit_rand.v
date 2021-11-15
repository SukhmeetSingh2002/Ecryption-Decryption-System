module bit_rand_6 (rand_6);
    output [5:0]rand_6;
    reg [5:0]rand_6;
    reg [5:0] next_6;
    wire xorConnection ;
    reg clk;

    integer ans;
    integer fd;

    assign xorConnection= rand_6[0]^rand_6[1];

    always @(posedge clk ) begin
        next_6={xorConnection,rand_6[5:1]};
        rand_6=next_6;
    end

    initial begin
        clk=1'b0;
        // reading seed 
        fd = $fopen("seed_6.txt", "r");
        ans = $fscanf(fd, "%b\n",rand_6);
        $fclose(fd);  

        #100
        // saving final value 
        fd = $fopen("seed_6.txt", "w");
        $fdisplay(fd,"%b",rand_6);
        $fclose(fd);  
    end

    always
        #4 clk=~clk;
endmodule