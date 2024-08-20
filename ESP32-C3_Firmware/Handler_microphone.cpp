/**
*   @file   Handler_microphone.cpp		Implementation file I2S Microphone
*   @author Antonio Omabel Longhitano
*/

#include "Config.h"


#ifdef USE_MICRO
/**
*   @brief I2S microphone setup
*/
void microphoneSetup() {
  /// Start I2S input with default configuration
  Serial.println("starting I2S...");
  auto config = i2sStream.defaultConfig(RX_MODE);
  config.i2s_format = I2S_STD_FORMAT; 
  config.sample_rate = 20000;
  config.pin_ws=21;
  config.pin_bck=9; 
  config.pin_data=8;
  config.channels = 2;
  config.port_no = 0;
  config.bits_per_sample = 32;
  i2sStream.begin(config);
  Serial.println("I2S started");
}
#endif //USE_MICRO