module contador #(
        parameter N = 26  //-- Numero de bits del contador
  )(
        input wire clk,           //-- Reloj del sistema
        output wire [4:0] leds    //-- Leds de la icestick
);

reg [N-1:0] cont;
reg rstn = 0;

//-- Inicialización
always @(posedge clk)
  rstn <= 1;

//-- Contador, con reset síncrono
always @(posedge clk)
  if (!rstn)
    cont <= 0;
  else
    cont <= cont + 1;

//-- Conectar los 5 bits más significativos del contador a los leds
assign leds = cont[N-1: N-6];

endmodule
