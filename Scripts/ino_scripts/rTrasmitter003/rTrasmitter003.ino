

#include <FreqCounter.h>

long int frqInt;

void setup()
{
     Serial.begin(9600);

}

void loop()
{
    
    FreqCounter::f_comp= 30;             // Set compensation to 12
    FreqCounter::start(200);            // Start counting with gatetime of 100ms
    
    while (FreqCounter::f_ready == 0)         // wait until counter ready
    frqInt=FreqCounter::f_freq;            // read result
    Serial.println(FreqCounter::f_freq);
    

   
    delay(100);
    
    //digitalWrite(13,LOW);

}
