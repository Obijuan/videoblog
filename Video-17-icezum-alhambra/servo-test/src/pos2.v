`default_nettype none
`include "divider.vh"

module pos1(input wire clk,
            input wire open,
            output wire servo1);

localparam SERVO_T = `T_20ms;

wire timer_ena = 1'b1;
wire [17:0] pos;

assign pos = (din == 1) ? `POS_OPEN : `POS_CLOSE;

dividerp1 #(SERVO_T)
  TIMER0 (  
    .clk(clk),
    .clk_out(servo1),
    .pos(pos),
    .timer_ena(timer_ena)
  );


wire din, dout, outen;

SB_IO #(
    .PIN_TYPE(6'b 1010_01),
    .PULLUP(1'b 1)
) io_pin (
    .PACKAGE_PIN(open),
    .OUTPUT_ENABLE(outen),
    .D_OUT_0(dout),
    .D_IN_0(din)
);

endmodule
