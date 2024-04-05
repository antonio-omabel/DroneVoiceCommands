#include "AudioTools.h"
#include "WiFi.h"


I2SStream i2sStream;    // Access I2S as stream


WiFiClient client;                  
MeasuringStream clientTimed(client);

StreamCopy copier(clientTimed, i2sStream, 2048);  
const char* ssid = "";      //Set your Wifi ssid
const char* password = "";  //Set your Wifi password
const char *client_address = "192.168.1.67"; // update based on your receive ip
uint16_t port = 5006;




void setup(){
  Serial.begin(115200);
  AudioLogger::instance().begin(Serial, AudioLogger::Info);
  connectWifi();


  // start i2s input with default configuration
  Serial.println("starting I2S...");
  auto config = i2sStream.defaultConfig(RX_MODE);
  config.i2s_format = I2S_STD_FORMAT; 
  config.sample_rate = 22050;
  config.pin_ws=21;   //25
  config.pin_bck=9;    //22
  config.pin_data=8;     ///21
  config.channels = 2;
  config.port_no = 0;
  config.bits_per_sample = 32;
  i2sStream.begin(config);
  Serial.println("I2S started");

 
}

// Arduino loop  
void loop() {
  connectIP();  // e.g if client is shut down we try to reconnect
  copier.copy();
}


  void connectWifi() {
    // connect to WIFI
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println();
    Serial.println(WiFi. localIP());

    // Performance Hack              
    client.setNoDelay(true);
    esp_wifi_set_ps(WIFI_PS_NONE);
  }

  void connectIP() {
    if (!client.connected()){
      while (!client.connect(client_address, port)) {
        Serial.println("trying to connect...");
        delay(5000);
      }    
    }
  }