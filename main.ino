#include "DHT.h"
#include <SPI.h>
#include <SD.h>

const int DHT_SENSOR_PIN[4] = {5, 6, 7, 8};
const int ULTRASONIC_TRIG_PIN = 10;
const int ULTRASONIC_ECHO_PIN = 9;
// const int SUCCEED_LED_PIN = 11; // test
const int ERROR_LED_PIN = 3;

const int MEASURE_TERM = 2; // minute

DHT *dht_sensor[4];

int number = 1;

void measure(float* temp_data, long* ultrasonic_data){
  temp_measure(temp_data);
  ultrasonic_measure(ultrasonic_data);
}
void temp_measure(float* temp_data){
  for(int i=0;i<4;i++){
    *(temp_data+i) = dht_sensor[i]->readTemperature();
    // Serial.println(dht_sensor[i]->readTemperature());
  }
}
void ultrasonic_measure(long* ultrasonic_data){
  digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(ULTRASONIC_TRIG_PIN, HIGH);
  delayMicroseconds(2);
  digitalWrite(ULTRASONIC_TRIG_PIN, LOW);
  
  *ultrasonic_data = pulseIn(ULTRASONIC_ECHO_PIN, HIGH); // microseconds
}
void save(float* temp_data, int ultrasonic_data){
  String s = "";
  s += "{'number':"+String(number);
  s += ",'time':"+String(number*MEASURE_TERM);
  s += ",'temp':["+String(temp_data[0])+","+String(temp_data[1])+","+String(temp_data[2])+","+String(temp_data[3])+"]";
  s += ",'ultrasonic':"+String(ultrasonic_data)+"}";
  Serial.println(s);
  File file = SD.open("result.txt", FILE_WRITE);
  if(file){
    file.println(s);
    file.close();
  }
}
void err_led(){
  digitalWrite(ERROR_LED_PIN, HIGH);
}

void setup() {
  // serial setup
  Serial.begin(9600);

  // HC-SR04 setup
  pinMode(ULTRASONIC_TRIG_PIN, OUTPUT);
  pinMode(ULTRASONIC_ECHO_PIN, INPUT);

  // LED setup
  // pinMode(SUCCEED_LED_PIN, OUTPUT)1;
  pinMode(ERROR_LED_PIN, OUTPUT);

  // sd module setup
  if(!SD.begin(4)){
    Serial.println("SD module initialization fail");
    err_led();
  }

  // DHT11 setup
  Serial.println("---");
  for(int i=0;i<4;i++){
    Serial.println("dht initializion");
    dht_sensor[i] = new DHT(DHT_SENSOR_PIN[i], DHT11);
    dht_sensor[i]->begin();
  }
}

void loop() {
  float temp_data[4];
  long ultrasonic_data;

  measure(temp_data, &ultrasonic_data);
  save(temp_data, ultrasonic_data);

  // test
  /*Serial.println("---");
  for(int i=0;i<4;i++){
    Serial.print("t: ");
    Serial.println(temp_data[i]);
  }
  Serial.print("u: ");
  Serial.println(ultrasonic_data);
  */

  delay(MEASURE_TERM * 60 * 1000);
  // delay(1000); // test
  number++;
}
