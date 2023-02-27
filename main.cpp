// Arduino Bad Apple
// Author: Caio Rigues (aka caiow²)

#include <LedControl.h> // https://github.com/wayoda/LedControl
#include <SD.h>

int size = 8;
int side = size * 8;

File arquivo;
String linha;

// DIN, CLK, CS
LedControl ledControls[] = {
  LedControl(0, 1, 2, size),
  LedControl(3, 4, 5, size),
  LedControl(6, 7, 8, size),
  LedControl(9, 10, 11, size),
  LedControl(22, 23, 24, size),
  LedControl(25, 26, 27, size),
};

void setup() {
  // put your setup code here, to run once:
  arquivo = SD.open("rgb_data.csv", FILE_READ);
}

void loop() {
  // put your main code here, to run repeatedly:s
  if (arquivo){
    while(arquivo.available()){
      linha = arquivo.readStringUntil('\n');

    }

  }else{

  }
}
