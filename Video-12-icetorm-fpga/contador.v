module contador (input wire clk,
                 output wire [4:0] leds);

reg [26:0] cont;
reg rstn = 0;

always @(posedge clk)
  rstn <= 1;

always @(posedge clk)
  if (!rstn)
    cont <= 0;
  else
    cont <= cont + 1;

assign leds = cont[26:21];

endmodule
