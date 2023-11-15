from machine import Pin, ADC
import utime
import Test

led = Pin(25, Pin.OUT)
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
def runControl():
    while True:
        xValue = xAxis.read_u16()
        yValue = yAxis.read_u16()
        buttonValue1 = button1.value()
        buttonStatus1 = "not pressed"
        buttonValue2 = button2.value()
        buttonStatus2 = "not pressed"

        if buttonValue1 == 1:
            buttonStatus1 = "pressed"
        if buttonValue2 == 1:
            buttonStatus2 = "pressed"
        if xValue > 6500:
            Test.prueba = "arriba"

        print(
            "X: " + str(xValue) + ", Y: " + str(yValue) + " -- button 1 value: " + str(buttonValue1) + " button 1 status: "
            + buttonStatus1 + " -- button 2 value: " + str(buttonValue2) + " button 2 status: " + buttonStatus2)
        utime.sleep(0.2)

if __name__ == "__main__":
    runControl()

