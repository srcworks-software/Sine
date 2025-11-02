import sys
import math
import random
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import GLib, Gtk, Adw
Adw.init()

class app(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.srcworks.sine")
        GLib.set_application_name("Sine")
        self.prev = None

    def do_activate(self):
        # declare main window
        window = Adw.ApplicationWindow(application=self, title="Sine")
        # header bar
        window.set_title("Sine")
        # box for widgets
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        # field widget
        self.entry = Gtk.Entry()
        vbox.append(self.entry)
        # grid layout
        grid = Gtk.Grid(column_homogeneous=True, row_homogeneous=True, column_spacing=6, row_spacing=6)
        keys = [
            ["Round", "Abs", "Bksp", "Clear"],
            ["Sin", "Cos", "Tan", "^"],
            ["Sin⁻¹", "Cos⁻¹", "Tan⁻¹", "√x"],
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["Ans", "(", ")", "π"],
        ]

        # attach to the grid 
        for r, row in enumerate(keys):
            for c, label in enumerate(row):
                button = Gtk.Button(label=label)
                button.connect("clicked", lambda b, l=label: self.key_parse(l))
                grid.attach(button, c, r, 1, 1)

        # append and what not
        vbox.append(grid)
        window.set_content(vbox)
        window.present()

    def key_parse(self, key):
        current = self.entry.get_text()
        if key == "Clear":
            self.entry.set_text("")
        elif key == "=":
            try:
                expr = current.replace("÷", "/").replace("×", "*").replace("^", "**")
                result = str(eval(expr))
                self.entry.set_text(result)
                self.prev = result
            except Exception as e:
                self.entry.set_text(f"Exception: {e}")
        elif key in ["0","1","2","3","4","5","6","7","8","9",".", "+", "-", "*", "/", "(", ")"]:
            self.entry.set_text(current + key)
        elif key == "^":
            self.entry.set_text(current + "**")
        elif key == "Ans":
            if self.prev is not None:
                self.entry.set_text(current + str(self.prev))
        elif key == "π":
            self.entry.set_text(current + "3.14159")
        elif key == "√x":
            self.entry.set_text(str(math.sqrt(float(current))))
        elif key == "Sin":
            self.entry.set_text(str(math.sin(math.radians(float(current)))))
        elif key == "Cos":
            self.entry.set_text(str(math.cos(math.radians(float(current)))))
        elif key == "Tan":
            self.entry.set_text(str(math.tan(math.radians(float(current)))))
        elif key == "Sin⁻¹":
            self.entry.set_text(str(math.degrees(math.asin(float(current)))))
        elif key == "Cos⁻¹":
            self.entry.set_text(str(math.degrees(math.acos(float(current)))))
        elif key == "Tan⁻¹":
            self.entry.set_text(str(math.degrees(math.atan(float(current)))))
        elif key == "Abs":
            self.entry.set_text(str(abs(float(current))))
        elif key == "Round":
            self.entry.set_text(str(int(round(float(current), 0))))
        elif key == "Bksp":
            self.entry.set_text(current[:-1])
        else:
            pass # do nothing for unrecognized keys

app = app()
exit_status = app.run(sys.argv)
sys.exit(exit_status)