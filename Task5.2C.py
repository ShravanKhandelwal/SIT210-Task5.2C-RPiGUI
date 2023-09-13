import tkinter as tk
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
LED_PINS = [17, 18, 27]  # GPIO pins for Red, Green, and Blue LEDs
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Create the GUI
def update_led_state(led_num):
    for i, pin in enumerate(LED_PINS):
        if i == led_num:
            GPIO.output(pin, GPIO.HIGH)
            canvas.itemconfig(led_shapes[i], fill=colors[i])
        else:
            GPIO.output(pin, GPIO.LOW)
            canvas.itemconfig(led_shapes[i], fill='white')

def exit_program():
    GPIO.cleanup()
    root.destroy()

root = tk.Tk()
root.title("LED Control")

colors = ['red', 'green', 'blue']

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

led_shapes = []
for i in range(3):
    led_shape = canvas.create_oval(50 + i * 100, 50, 150 + i * 100, 150, fill='white')
    led_shapes.append(led_shape)
    radio_button = tk.Radiobutton(root, text=f"{colors[i].title()} LED", variable=i, value=i, command=lambda i=i: update_led_state(i))
    radio_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

root.mainloop()