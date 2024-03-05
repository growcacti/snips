 def load_serial(self):
        # Load the serial number from a file
        try:
            with open("serial_number.txt", "r") as file:
                self.serial = file.read()
               
        except FileNotFoundError:
                messagebox.showerror("Error", "Serial number file not found. Please enter and save a serial number.")
           
