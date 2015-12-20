module contador #(
        parameter N = 26  //-- Numero de bits del contador
  )(
        input wire clk,
        output wire [4:0] leds);

reg [N-1:0] cont;
reg rstn = 0;

always @(posedge clk)
  rstn <= 1;

always @(posedge clk)
  if (!rstn)
    cont <= 0;
  else
    cont <= cont + 1;

assign leds = cont[N-1: N-6];

endmodule
