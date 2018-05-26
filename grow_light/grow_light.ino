// load libs
#include <SoftwareSerial.h>

const int grow_relay = 7;

void setup() {
  // initialize grow lights
  initialize_grow_lights();
  
  // connect to serial
  connect_serial();
}

void loop() {
  // send data only when you receive data
  if (Serial.available() > 0) {
    // read incoming int
    const int command = read_incoming_data();

    // check the command instruction
    switch (command) {
      case 0:
        // grow lights on
        control_grow_relay(HIGH);
        Serial.println("Grow Lights: Off");
        break;
      case 1:
        // grow lights off
        control_grow_relay(LOW);   
        Serial.println("Grow Lights: On");
        break;
      default: 
        break;
    }
  }
}

// connect via serial to computer
void connect_serial() {
  // Open serial communcations and wait for port to open
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect.
  }

  Serial.println("Connected!");
}

// function to control grow relay
// byte state turn the relay on or off
void control_grow_relay(byte state) {
    digitalWrite(grow_relay, state);
}

// initialize grow lights
// sets it to output
// turns them off
void initialize_grow_lights() {
  pinMode(grow_relay, OUTPUT);
  control_grow_relay(HIGH);
}

// read incoming data and convert it into a command
int read_incoming_data() {
    // read the incoming byte
    const byte incomingByte = Serial.read();

    // convert it into an int
    const int incomingInt = incomingByte - '0';
    
    // say what we got
    Serial.print("Received: ");  
    Serial.println(incomingInt);

    return incomingInt;
}
