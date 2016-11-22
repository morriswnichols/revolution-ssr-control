#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 8 on the Arduino
#define ONE_WIRE_BUS 8
#define TEMPERATURE_PRECISION 9

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs)
OneWire oneWire(ONE_WIRE_BUS);

// Pass our oneWire reference to Dallas Temperature.
DallasTemperature sensors(&oneWire);

// arrays to hold device addresses
DeviceAddress tankAddress, headAddress;

void setup()
{
  // start serial port
  Serial.begin(9600);
  Serial.println("Dallas Temperature IC Control Library Demo");

  // Start up the library
  sensors.begin();

  // Search method to discover addresses of probes
  oneWire.reset_search();
  if (!sensors.getAddress(tankAddress, 0)) Serial.println("Unable to find address for Device 0");
  if (!sensors.getAddress(headAddress, 1)) Serial.println("Unable to find address for Device 1");
  // show the addresses we found on the bus
  Serial.print("Tank Address: ");
  printAddress(tankAddress);
  Serial.println();

  Serial.print("Head Address: ");
  printAddress(headAddress);
  Serial.println();
  
}


    // function to print a device address
    void printAddress(DeviceAddress deviceAddress)
    {
      for (uint8_t i = 0; i < 8; i++)
      {
       // zero pad the address if necessary
       if (deviceAddress[i] < 16) Serial.print("0");
       Serial.print(deviceAddress[i], HEX);
      }
    }



    // function to print the temperature for a device
    void printTemperature(DeviceAddress deviceAddress)
    {
      float tempC = sensors.getTempC(deviceAddress);
      //  Serial.print("Temp C: ");
      //  Serial.print(tempC);
      //Serial.print(" Temp F: ");
      Serial.println(DallasTemperature::toFahrenheit(tempC));
    }

void loop() {
  // put your main code here, to run repeatedly:
 
  // request to the headtemp address on the bus
    sensors.requestTemperatures();
    double headTemp = sensors.getTempC(headAddress);
    Serial.print("Head Temp = ");
    Serial.println(DallasTemperature::toFahrenheit(headTemp));
    


}
