class Device:
    def __init__(self):
          self.device_name = "computer"
          self.device_address = "198.4345.655.33"

    def turnon(self):
         print("Device is turned on")
        
    def turnoff(self):
         print("Device is turned off")

class Audio_device(Device):
     
    def __init__(self):
          super().__init__()
          self.name = "audio"

    def enable(self):
        print("audio device is enabled")

    def disable(self):
        print("audion is disabled")

class microphone(Device):
    
    def __init__(self):
        super().__init__()
        self.microphone_name = "micro"

    def on(self):
        print("microphone turned on")

    def start_recording(self):
        print("microphone has started recording")

    def stop_recording(self):
        print("microphone stopped")   

class Speaker(Audio_device,microphone):

    def __init__(self,vol):
        super().__init__()
        self.speaker_name ="JBL"
        self.type = "Dolby atoms" 
        self.vol = vol

    def speaker_on(self):
        print("speaker is on")

    def increasing_vol(self,vol):
        print("volume is increasing")
        self.vol += vol

    def decreasing_vol(self,vol):
        print("volume is decreasing")
        self.vol -= vol

    def current_vol(self):
        print("current volume",self.vol)

    def speaker_off(self):
        print("speaker is off")

s1 = Speaker(80)
s1.turnon()
s1.enable()
print("spear name ->",s1.speaker_name)
s1.speaker_on()
s1.current_vol()
s1.increasing_vol(10)
s1.decreasing_vol(50)
s1.current_vol()
s1.disable()
s1.speaker_off()

     
     