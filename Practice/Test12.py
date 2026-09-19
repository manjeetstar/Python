from enum import Enum, unique,IntEnum, StrEnum

class FlightTime(Enum):
    ONTIME="On time"
    DELAYED="Delayed"
    CANCELLED="Cancelled"

    @property
    def description(self):
        return {
            FlightTime.ONTIME: "Flight is scheduled for 9PM",
            FlightTime.DELAYED: "Flight is DELAYED",
            FlightTime.CANCELLED: "Flight is CANCELLED for today"
        }[self]
    

   
print(FlightTime.DELAYED.description)