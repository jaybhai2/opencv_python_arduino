

#define CYCLES_PER_INTERRUPT 5000
unsigned long lastDeltaTime = 0;
unsigned long deltaTime = 0;

boolean firstInterrupt = true;
unsigned long storedDeltaTime = 0;
int storedTimeDeltaDifference = 0;
unsigned long freq = 0 ;
// This signal is called whenever OCR1A reaches 0
// (Note: OCR1A is decremented on every external clock cycle)



SIGNAL(TIMER1_COMPA_vect)
{
  unsigned long currentTime = micros();  //return time that arduino is running in micro second
  
  deltaTime =  currentTime - lastDeltaTime; //  
  lastDeltaTime = currentTime; //store currentTime for next interrupt

  if (firstInterrupt)                      //make the first interupt invalid
  {
    firstInterrupt = false;
  }
  else if (storedDeltaTime == 0)      //sample storedDeltaTime as base delta time
  {
    storedDeltaTime = deltaTime;      //
  }
  // Reset OCR1A
  OCR1A += CYCLES_PER_INTERRUPT;         //OCR1A = OCR1A + 5000
  
}



void setup() {
  Serial.begin(9600);                    // connect to the serial port
  //Serial.println("Frequency Counter");

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





void loop() {


  //Serial.println(OCR1A);
  Serial.println(deltaTime);
  delay(200);
  //storedTimeDeltaDifference = (storedDeltaTime - deltaTime);
  
  //Serial.println(deltaTime);
  //Serial.println(int(5000 / deltaTime));
  //Serial.println(storedDeltaTime);
  //Serial.println(storedTimeDeltaDifference);                // print result
  //delay(100);

  



















//if (digitalRead(TRIGGER_BTN_PIN) == LOW)
//  {
//    float sensitivity = mapFloat(analogRead(SENSITIVITY_POT_APIN), 0, 1023, 0.5, 10.0);
//    int storedTimeDeltaDifference = (storedTimeDelta - signalTimeDelta) * sensitivity;
//    tone(SPEAKER_PIN, BASE_TONE_FREQUENCY + storedTimeDeltaDifference);
//
//    if (storedTimeDeltaDifference > SPINNER_THRESHOLD)
//    {
//      digitalWrite(SPINNER_PIN, HIGH);
//    }
//    else
//    {
//      digitalWrite(SPINNER_PIN, LOW);
//    }
//  }
//  else
//  {
//    noTone(SPEAKER_PIN);
//    digitalWrite(SPINNER_PIN, LOW);
//  }

//  if (digitalRead(RESET_BTN_PIN) == LOW)
//  {
//    storedDeltaTime = 0;
//  }
//  

}



//float mapFloat(int input, int inMin, int inMax, float outMin, float outMax)
//{
//  float scale = (float)(input - inMin) / (inMax - inMin);
//  return ((outMax - outMin) * scale) + outMin;
//}










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
