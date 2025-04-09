import tkinter as tk
import math

def draw_heart(canvas, width, height):
    center_x = width // 2
    center_y = height // 2
    scale = 10  # Fattore di scala per ingrandire il cuore

    points = []
    for t in range(0, 360, 1):  # Genera punti lungo il contorno del cuore
        angle = math.radians(t)
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)

        # Scala e trasla per centrare il cuore
        scaled_x = x * scale + center_x  
        scaled_y = -y * scale + center_y  
        points.append((scaled_x, scaled_y))
    
    # Disegna un cuore riempito
    canvas.create_polygon(points, fill="red", outline="black")

root = tk.Tk()
root.title("Cuore con Tkinter")

canvas_width = 500
canvas_height = 500
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

draw_heart(canvas, canvas_width, canvas_height)

root.mainloop()