#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Class representing a Hall
class Hall {
public:
    int hallID;
    string hallName;
    int capacity;
    string location;
    bool availabilityStatus;

    Hall(int id, string name, int cap, string loc)
        : hallID(id), hallName(name), capacity(cap), location(loc), availabilityStatus(true) {}

    void bookHall() {
        if (availabilityStatus) {
            availabilityStatus = false;
            cout << hallName << " has been booked successfully.\n";
        } else {
            cout << hallName << " is already booked.\n";
        }
    }

    void checkAvailability() const {
        cout << hallName << " is " << (availabilityStatus ? "available." : "booked.") << endl;
    }
};

// Class representing an Event
class Event {
public:
    int eventID;
    string eventName;
    string eventDate;
    string eventTime;
    int duration;
    string eventOrganizer;

    Event(int id, string name, string date, string time, int dur, string organizer)
        : eventID(id), eventName(name), eventDate(date), eventTime(time), duration(dur), eventOrganizer(organizer) {}

    void displayEventDetails() const {
        cout << "Event: " << eventName << "\nDate: " << eventDate << "\nTime: " << eventTime
             << "\nDuration: " << duration << " hours\nOrganizer: " << eventOrganizer << endl;
    }
};

// Class representing a Booking
class Booking {
public:
    int bookingID;
    Event event;
    Hall hall;
    int numberOfAttendees;
    string bookingStatus;

    Booking(int id, Event ev, Hall hl, int attendees)
        : bookingID(id), event(ev), hall(hl), numberOfAttendees(attendees), bookingStatus("Confirmed") {}

    void cancelBooking() {
        bookingStatus = "Cancelled";
        hall.availabilityStatus = true; // Free up the hall
        cout << "Booking ID " << bookingID << " has been cancelled.\n";
    }

    void displayBookingDetails() const {
        cout << "Booking ID: " << bookingID << "\nStatus: " << bookingStatus << "\nAttendees: " << numberOfAttendees << endl;
        event.displayEventDetails();
    }
};

// Class representing the Hall Booking System
class HallBookingSystem {
private:
    vector<Hall> halls;
    vector<Event> events;
    vector<Booking> bookings;

public:
    void addHall(Hall h) {
        halls.push_back(h);
    }

    void listAvailableHalls() const {
        cout << "Available Halls:\n";
        for (const auto& h : halls) {
            if (h.availabilityStatus) {
                cout << h.hallID << ". " << h.hallName << " - " << h.location << ", Capacity: " << h.capacity << endl;
            }
        }
    }

    void bookHallForEvent(int hallID, Event e, int attendees) {
        for (auto& h : halls) {
            if (h.hallID == hallID && h.availabilityStatus) {
                h.bookHall();
                bookings.emplace_back(bookings.size() + 1, e, h, attendees);
                events.push_back(e);
                return;
            }
        }
        cout << "Hall ID " << hallID << " is not available.\n";
    }

    void cancelBooking(int bookingID) {
        for (auto& b : bookings) {
            if (b.bookingID == bookingID) {
                b.cancelBooking();
                return;
            }
        }
        cout << "Booking ID " << bookingID << " not found.\n";
    }

    void viewEventDetails(int eventID) const {
        for (const auto& e : events) {
            if (e.eventID == eventID) {
                e.displayEventDetails();
                return;
            }
        }
        cout << "Event ID " << eventID << " not found.\n";
    }
};

int main() {
    HallBookingSystem system;

    // Adding halls to the system
    system.addHall(Hall(1, "Grand Hall", 200, "Downtown"));
    system.addHall(Hall(2, "Conference Room", 50, "City Center"));

    system.listAvailableHalls();

    // Creating an event
    Event event(101, "Tech Seminar", "2025-05-15", "10:00 AM", 3, "TechCorp");

    // Booking a hall for the event
    system.bookHallForEvent(1, event, 150);

    // Viewing event details
    system.viewEventDetails(101);

    // Canceling a booking
    system.cancelBooking(1);

    return 0;
}