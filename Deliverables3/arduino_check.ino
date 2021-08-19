#define LEFT_SENSORPIN 4
#define CENTER_SENSORPIN 5
#define RIGHT_SENSORPIN 6

int steer = 7;
int throttle = 8;
unsigned long steer_duration;
unsigned long steer_overall_duration;
unsigned long throttle_duration;
unsigned long throttle_overall_duration;
 
void setup()
{
  Serial.begin(9600);
  pinMode(LEFT_SENSORPIN,INPUT);
  pinMode(CENTER_SENSORPIN,INPUT);
  pinMode(RIGHT_SENSORPIN,INPUT);

  pinMode(steer, INPUT);
  pinMode(throttle, INPUT);
}
 
void loop()
{
  // read input from sensors
  byte leftSensor=digitalRead(LEFT_SENSORPIN);
  byte centerSensor=digitalRead(CENTER_SENSORPIN);
  byte rightSensor=digitalRead(RIGHT_SENSORPIN);
  
  //조종기에서 들어오는 steer, throttle 값을 출력
  steer_duration = pulseInLong(steer, HIGH);
  steer_overall_duration = pulseIn(steer, LOW);
  steer_overall_duration += steer_duration;
  throttle_duration = pulseInLong(throttle, HIGH);
  throttle_overall_duration = pulseInLong(throttle, LOW);
  throttle_overall_duration += throttle_duration;

  Serial.print("steer_duration : ");
  Serial.print(steer_duration);
  Serial.print("/");
  Serial.print(steer_overall_duration);

  Serial.print("throttle_duration : ");
  Serial.print(throttle_duration);
  Serial.print("/");
  Serial.println(throttle_overall_duration);
  
  //적외선 센서 값 출력
  Serial.print(" Left : ");
  Serial.print(leftSensor);
  Serial.print(" Centre : ");
  Serial.print(centerSensor);
  Serial.print(" Right : ");
  Serial.print(rightSensor);
  Serial.println();
  delay(500);
}
