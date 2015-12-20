`timescale 100 ns / 10 ns
`default_nettype none

module contador_tb;

localparam N = 6;  //-- Numero de bits del contador

reg clk = 0;

wire [4:0] leds;

//-- Clock generator
always
  # 0.5 clk <= ~clk;

  contador #(
             .N(N)
  )  CONT0 (
             .clk(clk),
             .leds(leds)
  );

initial begin

      //-- File where to store the simulation
      $dumpfile("contador_tb.vcd");
      $dumpvars(0, contador_tb);

      #200 $display("END of the simulation");
      $finish;
    end


endmodule
