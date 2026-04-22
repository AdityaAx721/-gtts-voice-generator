import pyttsx3
import os
import sys

def main() -> None:
    try:
         #create output directory if not exsist
         output_dir = "output"
         os.makedirs(output_dir,exist_ok=True)

         #initialize the engine
         engine = pyttsx3.init()

         #Get availiable voices 
         voices = engine.getProperty("voices")

         #select voice(0 = Hazel UK, 1 = Zira US)
         if len (voices) > 1:
            engine.setProperty("voice", voices[1].id)
         else:
            engine.setProperty("voice", voices[0].id)

        #Set Speech rate(default ~200)
         engine.setProperty("rate", 170)

         #Set Volume (0.0 to 1.0)
         engine.setProperty("volume", 1.0)

         #Text to speech
         text = "hello sir, jarvis at your service what can i do for you"

         #save audio to file
         file_path = os.path.join(output_dir,"output_pytts.aiff")
         engine.save_to_file(text,file_path)

         #wait for speech to complete
         engine.runAndWait()

         print("Audio generated sucessfully :",file_path)

    except Exception as e:
        print("Error :",e)
        sys.exit(1)

if __name__ == "__main__":
    main()


         