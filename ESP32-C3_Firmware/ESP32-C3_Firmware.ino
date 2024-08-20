/**
*   @file   ESP32-C3_Firmware.ino    Main program for sending audio data
*   @author Antonio Omabel Longhitano
*/

#include "Config.h"

#ifdef USE_WIFI
  ///Generate WiFi client
  WiFiClient client;  
  ///IP connection last time
  unsigned long lastReadTime = 0;
  ///IP connection max time
  unsigned long timeoutInterval = 5000;
  ///IP connection check 
  bool isConnectionOpen = false;
#endif //USE_WIFI

#ifdef USE_MICRO
///Access I2S as stream
I2SStream i2sStream;
  #ifdef USE_WIFI 
  ///Thruput misurator  
  MeasuringStream clientTimed(client);
  ///Audio copier
  StreamCopy copier(clientTimed, i2sStream, 2048);
  #endif //USE_WIFI
#endif //USE_MICRO

///Choose your led pin
const int LED = 0;
///Choose your button pin
const int BUTTON = 1;
///Data sending check
bool isListeningLoop = false;

/**
*   @brief Arduino setup function
*/
void setup()
{
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  pinMode(BUTTON, INPUT_PULLUP);

  #ifdef USE_WIFI
    connectWifi();
  #endif  //USE_WIFI

  #ifdef USE_MICRO
    AudioLogger::instance().begin(Serial, AudioLogger::Info);
    microphoneSetup();
  #endif  //USE_MICRO
  
}

/**
*   @brief Arduino loop function
*/ 
void loop() 
{
  #ifdef USE_WIFI
    connectIP();
  #endif  //USE_WIFI

  ///Send data while button is pressed
  while(digitalRead(BUTTON) == LOW){
    analogWrite(LED, 10);
    #ifdef USE_MICRO
      #ifdef USE_WIFI
        copier.copy();
      #endif  //USE_WIFI
    #endif  //USE_MICRO
    isListeningLoop = true;
  }
  
  ///Close the connection if data is being sent
  if (isListeningLoop){
    analogWrite(LED, LOW);
    #ifdef USE_WIFI
      #ifdef USE_MICRO
        int i=0;
        while (i<15){
          copier.copy();
          i++;
        }
      #endif  //USE_MICRO
      client.stop();
      Serial.println("Connection closed.");
      isConnectionOpen = false;
    #endif  //USE_WIFI   
    isListeningLoop = false;
  }

  ///Close the connection after 5 seconds without sending data
  #ifdef USE_WIFI
    if (millis() - lastReadTime > timeoutInterval && isConnectionOpen) {
      client.stop();
      Serial.println("Connection closed.");
      isConnectionOpen = false;
    }
  #endif //USE_WIFI
}





