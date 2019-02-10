
#include <FreqCounter.h>

void setup() {
  Serial.begin(9600);                    // connect to the serial port
  Serial.println("Frequency Counter");
}

long int frq;
void loop() {

 FreqCounter::f_comp= 8;             // Set compensation to 12
 FreqCounter::start(100);            // Start counting with gatetime of 100ms
 while (FreqCounter::f_ready == 0)         // wait until counter ready
 
 frq=FreqCounter::f_freq;            // read result

 
 Serial.println(frq);                // print result
 delay(500);


}













//
//int data = 0;
//int pin = 7;
//unsigned long duration;
//
//
//void setup() {
//  // put your setup code here, to run once:
//  Serial.begin(9600);
//  pinMode(pin, INPUT);
//
//}
//
//void loop() {
//  // put your main code here, t
//  duration = pulseIn(pin, HIGH);
//  Serial.println(duration);
//  //data = analogRead(3);
//  //Serial.println(data);
//  //delay(500);
//  
//}
