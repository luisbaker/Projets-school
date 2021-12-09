# Create by Luis
import lcddriver
import time
lcd=lcddriver.lcd()
def Clign_Texte(texte,ligne):
    lcd.lcd_clear()
    time.sleep(.4)
    lcd.lcd_display_string(texte,ligne)
    time.sleep(.4)
try:
    while True:
        print
        lcd.lcd_display_string("Bonjour :D",1)
        lcd.lcd_display_string("ca va?",2)
        time.sleep(2)
        lcd.lcd_display_string("Date: %s" %time.strftime("%d/%m/%y"),1)
        lcd.lcd_display_string("Heure: %s" %time.strftime("%H:%M:%S"),2)
        time.sleep(2)
        lcd.lcd_clear()
        time.sleep(2)
        lcd.lcd_display_string("Vive la France Vive la Republique",1)
        time.sleep(2)
except KeyboardInterrupt:
    lcd.lcd_clear()
    lcd.lcd_display_string("Bye, bye ....",1)
    time.sleep(2)
    lcd.lcd_clear()
