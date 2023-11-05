/*
 * This program is property of SME Dehradun. For any query related to this program, 
 * contact us at www.smedehradn.com
 * If you want any solution related to any IoT Customized Boards and Sensor, 
 * then contact www.nuttyengineer.com 
 */

#define BLYNK_DEVICE_NAME "IoT Waste Segregator" 

#define BLYNK_TEMPLATE_ID "TMPL6aihqsadr"
#define BLYNK_TEMPLATE_NAME "IoT Waste Segregator"
#define BLYNK_FIRMWARE_VERSION "0.1.0"
#define BLYNK_PRINT Serial
#include "BlynkEdgent.h"

#define echoPin1 32
#define trigPin1 33

#define echoPin2 25
#define trigPin2 26

const int PIN_RED1   = 23;
const int PIN_GREEN1 = 22;
const int PIN_BLUE1  = 21;

const int PIN_RED2   = 14;
const int PIN_GREEN2 = 13;
const int PIN_BLUE2  = 12;

long duration1, duration2, cm1, cm2, inches1, inches2;
int distance1, distance2;


void setColor1(int R, int G, int B) {
  digitalWrite(PIN_RED1,   R);
  digitalWrite(PIN_GREEN1, G);
  digitalWrite(PIN_BLUE1,  B);
}

void setColor2(int R, int G, int B) {
  digitalWrite(PIN_RED2,   R);
  digitalWrite(PIN_GREEN2, G);
  digitalWrite(PIN_BLUE2,  B);
}

void ultrasonic1()
{
    digitalWrite(trigPin1, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin1, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin1, LOW);
    duration1 = pulseIn(echoPin1, HIGH);
    distance1 = duration1 * 0.034 / 2; // formula to calculate the distance for ultrasonic sensor 1
    // Serial.print("Distance 1: ");
    // Serial.println(distance1);
    cm1 = (duration1 / 2) / 29.1;
    inches1 = (duration1 / 2) / 74;
    // Serial.print(inches1);
    // Serial.print("in, ");
    // Serial.print(cm1);
    // Serial.print("cm");
    // Serial.println();

    // int mappedValue1 = map(inches1, 19.29, 7.08, 0, 100);
    int mappedValue1 = map(inches1, 26.378, 7.08, 0, 100);
    Blynk.virtualWrite(V1, mappedValue1);

    if (mappedValue1 <= 33) {
      // Low distance, light up the LED in green
      setColor1(LOW, HIGH, LOW);
    } else if (mappedValue1 <= 66) {
      // Middle distance, light up the LED in blue
      setColor1(LOW, LOW, HIGH);
    } else {
      // High distance, light up the LED in red
      setColor1(HIGH, LOW, LOW);
    }

    delay(500);
}

void ultrasonic2()
{
    digitalWrite(trigPin2, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin2, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin2, LOW);
    duration2 = pulseIn(echoPin2, HIGH);
    distance2 = duration2 * 0.034 / 2; // formula to calculate the distance for ultrasonic sensor 2
    // Serial.print("Distance 2: ");
    // Serial.println(distance2);
    cm2 = (duration2 / 2) / 29.1;
    inches2 = (duration2 / 2) / 74;
    // Serial.print(inches2);
    // Serial.print("in, ");
    // Serial.print(cm2);
    // Serial.print("cm");
    // Serial.println();

    int mappedValue2 = map(inches2, 26.378, 7.08, 0, 100);
    Blynk.virtualWrite(V2, mappedValue2); // Use V2 for the second ultrasonic sensor

    if (mappedValue2 <= 33) {
      // Low distance, light up the LED in green
      setColor2(LOW, HIGH, LOW);
    } else if (mappedValue2 <= 66) {
      // Middle distance, light up the LED in blue
      setColor2(LOW, LOW, HIGH);
    } else {
      // High distance, light up the LED in red
      setColor2(HIGH, LOW, LOW);
    }

    delay(500);
}

void setup()
{
    Serial.begin(115200);

    

    pinMode(trigPin1, OUTPUT);
    pinMode(echoPin1, INPUT);

    pinMode(trigPin2, OUTPUT);
    pinMode(echoPin2, INPUT);

    pinMode(PIN_RED1,   OUTPUT);
    pinMode(PIN_GREEN1, OUTPUT);
    pinMode(PIN_BLUE1,  OUTPUT);

    pinMode(PIN_RED2,   OUTPUT);
    pinMode(PIN_GREEN2, OUTPUT);
    pinMode(PIN_BLUE2,  OUTPUT);

    BlynkEdgent.begin();
    delay(2000);
    // int inches1 = 26.378;
    // int mappedValue1 = map(inches1, 26.378, 7.08, 0, 100);
    // Serial.print("mappedValue1 = ");
    // Serial.print(mappedValue1);
    Serial.println("");
}

void loop()
{
    BlynkEdgent.run();
    ultrasonic1();
    ultrasonic2();
}
