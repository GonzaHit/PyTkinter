import tkinter as tk
from tkinter import messagebox
from pytube import YouTube


    
def download_video():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()
        messagebox.showinfo("Éxito", "Video descargado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo descargar el video. \n{str(e)}")

def download_audio():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()
        audio.download()
        messagebox.showinfo("Éxito", "Audio descargado con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo descargar el audio. \n{str(e)}")

# Configuración de la ventana
root = tk.Tk()
root.title("Downloader de YouTube")
root.geometry("400x200")

# Etiqueta y caja de texto para URL
url_label = tk.Label(root, text="Ingrese la URL del video de YouTube:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Botones para descargar video y audio
download_video_button = tk.Button(root, text="Descargar Video", command=download_video)
download_video_button.pack(pady=10)

download_audio_button = tk.Button(root, text="Descargar Audio", command=download_audio)
download_audio_button.pack(pady=10)

# Iniciar el bucle de la interfaz
root.mainloop()
