## Nop Obfuscation

Method to obfuscate assembly of C/C++ PE file 

* Add large nop macro to file ```#define OBF __asm("nop\n nop\n nop\n nop\n nop\n nop\n nop\n...")```
* Paste macro next to all instruction i wrote
[python file]("https://github.com/Jacques-Vianney/Nop_Obfuscation/blob/main/obf.py") for this
* Enjoy your obfuscated file
[nop]("https://en.wikipedia.org/wiki/NOP_(code)") instruction do not effect on file except size
![nop](https://github.com/prkx/Nop_Obfuscation/blob/main/nop.png)
