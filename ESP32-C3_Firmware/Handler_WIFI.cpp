/**
*   @file   Handler_WIFI.cpp		Implementation file for WiFi and TCP/IP connection
*   @author Antonio Omabel Longhitano
*/

#include "Config.h"

#ifdef USE_WIFI
///Set your Wifi SSID
const char* ssid = "";      
///Set your Wifi password
const char* password = "";
///Set your Server IP
const char *server_address = "";
///Set your Server port
uint16_t port = 5005;

/**
*   @brief Wifi connection handler
*/
void connectWifi() {
  ///Connect to WIFI
  WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }
  Serial.println();
  Serial.println(WiFi. localIP());          
  client.setNoDelay(true);
  #ifdef USE_MICRO
    esp_wifi_set_ps(WIFI_PS_NONE);
  #endif //USE_MICRO
}

/**
*   @brief TCP/IP connection handler
*/
void connectIP() {
  if (!client.connected()){
    ///Try to establish a connection with the server while the connection is not open
    while (!client.connect(server_address, port)) {
      Serial.println("trying to connect...");
      delay(500);
    }
    if(!isConnectionOpen){
      Serial.println("Connection opened.");
    }
    isConnectionOpen = true;
    lastReadTime = millis();    
  }
}
#endif //USE_WIFI