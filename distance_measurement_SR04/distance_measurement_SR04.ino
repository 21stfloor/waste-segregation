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

long duration1, duration2, cm1, cm2, inches1, inches2;
int distance1, distance2;

void ultrasonic1()
{
    digitalWrite(trigPin1, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin1, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin1, LOW);
    duration1 = pulseIn(echoPin1, HIGH);
    distance1 = duration1 * 0.034 / 2; // formula to calculate the distance for ultrasonic sensor 1
    Serial.print("Distance 1: ");
    Serial.println(distance1);
    cm1 = (duration1 / 2) / 29.1;
    inches1 = (duration1 / 2) / 74;
    Serial.print(inches1);
    Serial.print("in, ");
    Serial.print(cm1);
    Serial.print("cm");
    Serial.println();

    int mappedValue1 = map(inches1, 0, 19, 100, 0);
    Blynk.virtualWrite(V1, mappedValue1);
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
    Serial.print("Distance 2: ");
    Serial.println(distance2);
    cm2 = (duration2 / 2) / 29.1;
    inches2 = (duration2 / 2) / 74;
    Serial.print(inches2);
    Serial.print("in, ");
    Serial.print(cm2);
    Serial.print("cm");
    Serial.println();

    int mappedValue2 = map(inches2, 0, 19, 100, 0);
    Blynk.virtualWrite(V2, mappedValue2); // Use V2 for the second ultrasonic sensor
    delay(500);
}

void setup()
{
    Serial.begin(115200);
    pinMode(trigPin1, OUTPUT);
    pinMode(echoPin1, INPUT);

    pinMode(trigPin2, OUTPUT);
    pinMode(echoPin2, INPUT);

    BlynkEdgent.begin();
    delay(2000);
}

void loop()
{
    BlynkEdgent.run();
    ultrasonic1();
    ultrasonic2();
}
