module bit_rand_11 (rand_11);
    output [10:0]rand_11;
    reg [10:0]rand_11;
    reg [10:0] next_11;
    wire xorConnection ;
    reg clk;

    integer ans;
    integer fd;

    assign xorConnection= rand_11[0]^rand_11[2];

    always @(posedge clk ) begin
        next_11={xorConnection,rand_11[10:1]};
        rand_11=next_11;
    end

    initial begin
        clk=1'b0;
        // reading seed 
        fd = $fopen("seed_11.txt", "r");
        ans = $fscanf(fd, "%b\n",rand_11);
        $fclose(fd);  

        #35
        // saving final value 
        fd = $fopen("seed_11.txt", "w");
        $fdisplay(fd,"%b",rand_11);
        $fclose(fd);  
    end

    always
        #4 clk=~clk;
endmodule