/**
*   @file   Config.h		Configuration file for TTS project
*   @author Antonio Omabel Longhitano
*/
#pragma once

#undef USE_MICRO
#define USE_MICRO

#undef USE_WIFI
#define USE_WIFI

//Microphone section
#ifdef USE_MICRO
  #include "AudioTools.h"
  extern I2SStream i2sStream;
  void microphoneSetup();
#endif //USE_MICRO

//WIFI section
#ifdef USE_WIFI
  #include "WiFi.h"
  extern WiFiClient client;
  extern unsigned long lastReadTime;
  extern bool isConnectionOpen;
  void connectWifi();
  void connectIP();
#endif //USE_WIFI

////////////////////////// PIN configuration ///////////////////

/// ESP32 pin Number associated with LED 
const int LED = 0;
/// ESP32 pin Number associated with Button
const int BUTTON = 1;
