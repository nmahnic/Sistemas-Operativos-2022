#  To install nasm package
#  sudo apt install nasm
#  sudo apt install build-essential
#  sudo apt install git

SRC_FILE    = hello
OUTPUT_BIN  = bin/hello.bin
ODFLAGS		= -CprsSx --prefix-addresses

all: folder hello link documentation

folder: 
	@echo Generando $@.asm...
	mkdir -p bin
	mkdir -p sup
	mkdir -p obj
	mkdir -p doc

hello:
	nasm -f elf64 $(SRC_FILE).asm -o obj/$(SRC_FILE).elf -l sup/$(SRC_FILE).lst

link:
	ld obj/$(SRC_FILE).elf -o $(OUTPUT_BIN)

clean:
	rm -R bin
	rm -R obj
	rm -R sup
	rm -R doc

run:
	./$(OUTPUT_BIN)

documentation:
	hexdump -C obj/$(SRC_FILE).elf > doc/$(SRC_FILE)_hexdump.txt
	objdump $(ODFLAGS) obj/$(SRC_FILE).elf > doc/$(SRC_FILE)_objdump.txt
	readelf -a obj/$(SRC_FILE).elf > doc/$(SRC_FILE)_readelf.txt