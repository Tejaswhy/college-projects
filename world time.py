import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime, time, timedelta
import requests
from tkinter import Canvas, messagebox

root = tk.Tk()
root.title("World digital clock")
root.geometry("1500x900")

# Background canvas
main_canvas = tk.Canvas(root, width=1500, height=900)
main_canvas.pack(fill="both", expand=True)

# Background image
bg_image = Image.open('/Users/tejasy/Desktop/world/wo.png').resize((1400,850))
bg = ImageTk.PhotoImage(bg_image)
main_canvas.create_image(0, 0, image=bg, anchor="nw")

# Function called on button click
def show_text(lat, lon, place):
    # Get time data from API
    
    url = f"https://timeapi.io/api/Time/current/coordinate?latitude={lat}&longitude={lon}"
   
    response = requests.get(url)
    data = response.json()

    time_display = data.get("time", "")[:5] 
    date = data.get("date", "N/A")
    day_of_week = data.get("dayOfWeek", "N/A")
    hour = int(time_display.split(":")[0])

    beng_canvas = tk.Canvas(main_canvas, width=400, height=400)
    canvas_window =main_canvas.create_window(500, 300, window=beng_canvas, anchor="nw")

    bg_morning = ImageTk.PhotoImage(Image.open("/Users/tejasy/Desktop/world/morn.png").resize((400, 400)))
    bg_evening = ImageTk.PhotoImage(Image.open("/Users/tejasy/Desktop/world/dawn.png").resize((400, 400)))
    bg_night = ImageTk.PhotoImage(Image.open("/Users/tejasy/Desktop/world/night.png").resize((400, 400)))
    def close_canvas():
        main_canvas.delete(canvas_window)
    bg_image_item = beng_canvas.create_image(0, 0, anchor="nw", image=bg_morning)

    if 5 <= hour < 12:
            beng_canvas.itemconfig(bg_image_item, image=bg_morning)
            beng_canvas.image = bg_morning # Prevent garbage collection
            beng_canvas.create_text(200, 100, text=time_display, font=("times new roman", 45), fill="black")
            beng_canvas.create_text(200, 150, text=date, font=("times new roman", 45), fill="black")
            beng_canvas.create_text(200, 195, text=day_of_week, font=("times new roman", 45), fill="black")
            beng_canvas.create_text(200, 30, text=place.upper(), font=("times new roman",40),fill="black")
    elif 12 <= hour < 18:
            beng_canvas.itemconfig(bg_image_item, image=bg_evening)
            beng_canvas.image = bg_evening
            beng_canvas.create_text(200, 100, text=time_display, font=("times new roman", 45), fill="white")
            beng_canvas.create_text(200, 150, text=date, font=("times new roman", 45), fill="white")
            beng_canvas.create_text(200, 195, text=day_of_week, font=("times new roman", 45), fill="white")
            beng_canvas.create_text(200, 30, text=place.upper(), font=("times new roman", 40), fill="white")
    else:
            beng_canvas.itemconfig(bg_image_item, image=bg_night)
            beng_canvas.image = bg_night
            beng_canvas.create_text(200, 100, text=time_display, font=("times new roman", 45), fill="white")
            beng_canvas.create_text(200, 150, text=date, font=("times new roman", 45), fill="white")
            beng_canvas.create_text(200, 195, text=day_of_week, font=("times new roman", 45), fill="white")
            beng_canvas.create_text(200, 30, text=place.upper(), font=("times new roman", 40), fill="white")

    close_btn = tk.Button(beng_canvas, text="Close", command=close_canvas)
    beng_canvas.create_window(200, 360, window=close_btn)



# --------------------------------#delhi
bg_image = Image.open('/Users/tejasy/Desktop/world/bgbg.png').resize((20,20))
pin_image = Image.open('/Users/tejasy/Desktop/world/pin.png').resize((33,33))  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place1="delhi"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(28.6139, 77.2390,place1),
    bd=2,
    highlightthickness=1,
     highlightbackground="red",
     highlightcolor="red",
     relief='flat'
)
search_button.image = composite
search_button.place(x=940, y=405)
#---------------------------------#baker island
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place2="Baker Island"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(0.1936,-176.4769,place2),
    bd=2,
    highlightthickness=1,
     highlightbackground="red",
     highlightcolor="red",
     relief='flat'
)
search_button.image = composite
search_button.place(x=20, y=575)
#---------------------------------#pago pago
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place3="Pago Pago"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(-14.2756,-170.7020,place3),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1360, y=635)

#---------------------------------#Honolulu
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place4="Honolulu"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(21.31,157.86,place4),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=68, y=430)
#---------------------------------#alaska 

 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place5="Anchorage"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(61.2181,-149.9003,place5),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=95, y=154)
#---------------------------------#los angeles
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place6="Los Angeles"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(34.0522,-118.2437,place6),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=210, y=320)
#---------------------------------#denver
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place7="Denver"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(39.7392,-104.9903,place7),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=255, y=295)
#---------------------------------#mexico city
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place8="Mexico City"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(19.4326,-99.1332,place8),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=285, y=415)
#---------------------------------#new york city
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place9="New York City"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(40.7128,-74.0060,place9),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=360, y=300)
#---------------------------------#Caracas
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place10="Caracas"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(10.4806,-66.9036,place10),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=400, y=465)
#---------------------------------# Buenos Aires
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place11=" Buenos Aires"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(-34.6037,-58.3816,place11),
     bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=435,y=680)
#---------------------------------# South Georgia
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place12="South Georgia"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(-54.4296,-36.5879,place12),
      bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=550, y=820)
#---------------------------------#Azores
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place13="Azores"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text( 37.7412,-25.6756,place13),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=575, y=315)
#---------------------------------#London

  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place14=" London"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(51.5074,-0.1278,place14),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=650, y=220)
#---------------------------------#Paris
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place15=" Paris"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(48.8566,2.3522,place15),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=660, y=250)
#---------------------------------#cairo

 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place16="Cairo"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(30.0444,31.2357,place16),
     bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=760, y=360)
#---------------------------------#Moscow
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place17="Moscow"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(55.7558,37.6173,place17),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=785, y=205)
#---------------------------------#Dubai

 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place18="Dubai"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(25.2048,55.2708,place18),
      bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=855, y=395)
#---------------------------------#karachi

# smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place19="Karachi"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(24.8607,67.0011,place19),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=898, y=378)
#---------------------------------#Dhaka
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place20="Dhaka"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(23.8103,90.4125,place20),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=998, y=390)
#---------------------------------#bangkok

 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place21="Bangkok"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(13.7563,100.5018,place21),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1025, y=460)
#---------------------------------#Beijing

  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place22="Beijing"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(39.9042,116.4074,place22),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1070, y=300)
#---------------------------------#Tokyo
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place23="Tokyo"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(35.6895,139.6917,place23),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1155, y=350)
#---------------------------------#Sydney

  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place24="Sydney"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(-33.8688,151.2093,place24),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1210, y=690)
#---------------------------------#Honiara
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place25="Honiara"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(-9.4456,159.9729,place25),
   bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1250, y=615)
#---------------------------------#Suva
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place26="Suva"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(-18.1248,178.4501,place26),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1310, y=580)
#---------------------------------#Nukuʻalofa:
  # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place27="Nuku'alofa"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(28.6100, 77.2300,place27),
     bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1410,y=610)

#---------------------------------#Kiritimati:
 # smaller pin
bg_image.paste(pin_image, (-3,-5), pin_image)  # use pin_image as mask if it has alpha
composite = ImageTk.PhotoImage(bg_image)
place28="Kiritimati"
search_button = tk.Button(
    main_canvas,
    image=composite,
    command=lambda: show_text(1.8721,-157.4278,place28),
    bd=2,
    highlightthickness=1,
    highlightbackground="red",
    highlightcolor="red",
    relief='flat'
)
search_button.image = composite
search_button.place(x=1385,y=505)
#---------------------------------#:


root.mainloop()