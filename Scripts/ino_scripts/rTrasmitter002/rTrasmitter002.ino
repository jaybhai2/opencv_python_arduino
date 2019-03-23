
#include <RH_ASK.h>
#include <SPI.h> // Not actually used but needed to compile

#define CYCLES_PER_INTERRUPT 5000
unsigned long lastDeltaTime = 0;
unsigned long deltaTime = 0;

boolean firstInterrupt = true;
unsigned long storedDeltaTime = 0;
int storedTimeDeltaDifference = 0;
unsigned long freq = 0 ;

RH_ASK driver(2000,"",3,10); // ESP8266: do not use pin 11

SIGNAL(TIMER1_COMPA_vect)
{
  unsigned long currentTime = micros();  //return arduino running time
  
  deltaTime =  currentTime - lastDeltaTime; //  
  lastDeltaTime = currentTime; //store currentTime for next interrupt

  if (firstInterrupt)                      //make the first interupt invalid
  {
    firstInterrupt = false;
  }
  else if (storedDeltaTime == 0)      //sample storedDeltaTime as base delta time
  {
    storedDeltaTime = deltaTime;      
  }
  // Reset OCR1A
  OCR1A += CYCLES_PER_INTERRUPT;         //OCR1A = OCR1A + 5000
  //Serial.println(deltaTime);
}

void setup()
{
    
    pinMode(13,OUTPUT);
    Serial.begin(9600);    // Debugging only
    if (!driver.init())
         Serial.println("init failed");


             // Set Waveform Generation Mode to 0 (Normal)
  TCCR1A = 0b00000000;
  
  // Set CSS(Clock Speed Selection) to 0b111 (External clock source on T0 pin
  // (ie, pin 5 on UNO). Clock on rising edge.)
  TCCR1B = 0b00000111;

  // Enable timer compare interrupt A (ie, SIGNAL(TIMER1_COMPA_VECT))
  TIMSK1 |= (1 << OCIE1A);

  // Set OCR1A (timer A counter) to trigger interrupt on next cycle
  OCR1A = CYCLES_PER_INTERRUPT;
 
  //pinMode(13, OUTPUT);
}

void loop()
{
   String pStr = String(deltaTime);
    
   char pChar[sizeof(pStr)+1];
   pStr.toCharArray(pChar, sizeof(pChar));
   
   delay(100);
   //Serial.println(pChar); 
    
   driver.send((uint8_t *)pChar, strlen(pChar));
   driver.waitPacketSent();
    
}




