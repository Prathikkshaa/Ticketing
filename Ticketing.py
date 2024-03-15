import tkinter as tk

class Bus:
    def __init__(self, bus_id, seats=24):
        self.bus_id = bus_id
        self.seats = {str(i): "Available" for i in range(1, seats + 1)}

class BusTicketReservationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticketing-Bus Ticket Reservation System")
        self.buses = [Bus(f"Bus {i}") for i in range(1, 13)]  # Create 12 buses
        self.selected_bus = None
        self.create_ui()

    def create_ui(self):
        self.root.geometry("400x300")  # Set window size

        self.bus_label = tk.Label(self.root, text="Select Your Bus:")
        self.bus_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.bus_var = tk.StringVar(self.root)
        self.bus_dropdown = tk.OptionMenu(self.root, self.bus_var, *[bus.bus_id for bus in self.buses], command=self.select_bus)
        self.bus_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.seat_label = tk.Label(self.root, text="Select a Seat:")
        self.seat_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.seat_var = tk.StringVar(self.root)
        self.seat_dropdown = tk.OptionMenu(self.root, self.seat_var, "", command=self.select_seat)
        self.seat_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.book_button = tk.Button(self.root, text="Book Seat", command=self.book_seat)
        self.book_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.cancel_button = tk.Button(self.root, text="Cancel Booking", command=self.cancel_booking)
        self.cancel_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.show_booked_button = tk.Button(self.root, text="Show Booked Seats", command=self.show_booked_seats)
        self.show_booked_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.status_label = tk.Label(self.root, text="", wraplength=380, justify="left")
        self.status_label.grid(row=4, columnspan=2, padx=10, pady=10, sticky="w")

    def select_bus(self, selected_bus_id):
        self.selected_bus = next(bus for bus in self.buses if bus.bus_id == selected_bus_id)
        self.update_seat_dropdown()

    def update_seat_dropdown(self):
        if self.selected_bus:
            self.seat_dropdown['menu'].delete(0, 'end')
            for seat_number, status in self.selected_bus.seats.items():
                self.seat_dropdown['menu'].add_command(label=f"Seat {seat_number} - {status}", command=tk._setit(self.seat_var, seat_number))

    def select_seat(self, selected_seat_number):
        pass

    def book_seat(self):
        selected_seat_number = self.seat_var.get()
        if self.selected_bus and selected_seat_number:
            if self.selected_bus.seats[selected_seat_number] == "Available":
                self.selected_bus.seats[selected_seat_number] = "Booked"
                self.status_label.config(text=f"Seat {selected_seat_number} booked on {self.selected_bus.bus_id}")
                self.update_seat_dropdown()

    def cancel_booking(self):
        selected_seat_number = self.seat_var.get()
        if self.selected_bus and selected_seat_number:
            if self.selected_bus.seats[selected_seat_number] == "Booked":
                self.selected_bus.seats[selected_seat_number] = "Available"
                self.status_label.config(text=f"Booking canceled for Seat {selected_seat_number} on {self.selected_bus.bus_id}")
                self.update_seat_dropdown()

    def show_booked_seats(self):
        if self.selected_bus:
            booked_seats = [seat for seat, status in self.selected_bus.seats.items() if status == "Booked"]
            if booked_seats:
                self.status_label.config(text=f"Booked seats on {self.selected_bus.bus_id}: {', '.join(booked_seats)}")
            else:
                self.status_label.config(text="No seats booked on this bus.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BusTicketReservationSystem(root)
    root.mainloop()
