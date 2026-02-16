import pyttsx3 # libreria de texto a voz

# inicializar la variable tipo objeto
engine = pyttsx3.init() 

text = "carrera por el faso" # texto que se desea reproducir
engine.say(text) # ordenar al motor que reproduzca el texto

engine.runAndWait()