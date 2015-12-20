#-----------------------------------------------------
#-- Project 1
#-----------------------------------------------------
NAME = contador
DEPS =

#------------- Simulation of project 1 ---------
sim: contador_tb.vcd

contador_tb.vcd: contador.v contador_tb.v
	iverilog contador_tb.v contador.v -o contador_tb.out
	./contador_tb.out
	gtkwave contador_tb.vcd contador_tb.gtkw

sint: contador.bin


contador.bin: contador.v
	yosys -p "synth_ice40 -blif contador.blif" contador.v
	arachne-pnr -d 1k -p contador.pcf contador.blif -o contador.txt
	icepack contador.txt contador.bin

#---- Upload into FPGA of project 1 ------
prog: contador.bin
	iceprog contador.bin


#-- Clean the project
clean:
	rm -f *.bin *.txt *.blif *.out *.vcd *~

.PHONY: all clean
