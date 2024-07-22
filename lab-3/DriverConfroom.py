import sys
from antlr4 import *
from ConfRoomSchedulerLexer import ConfRoomSchedulerLexer
from ConfRoomSchedulerParser import ConfRoomSchedulerParser
from ConfRoomSchedulerListener import ConfRoomSchedulerListener

class ConfRoomSchedulerSemanticChecker(ConfRoomSchedulerListener):

    def __init__(self):
        self.reservations = {}
    
    def validate_time(self, time_str):
        hours, minutes = map(int, time_str.split(':'))
        return 0 <= hours < 24 and 0 <= minutes < 60

    def enterReserveStat(self, ctx: ConfRoomSchedulerParser.ReserveStatContext):
        reserve_ctx = ctx.reserve()
        room_id = reserve_ctx.ID().getText()
        date = reserve_ctx.DATE().getText()
        start_time = reserve_ctx.TIME(0).getText()
        end_time = reserve_ctx.TIME(1).getText()
        
        name = reserve_ctx.NAME().getText() if reserve_ctx.NAME() else "unknown"
        
        if not self.validate_time(start_time) or not self.validate_time(end_time):
            print(f"Error: Invalid time format for reservation by {name}.")
            return
        
        key = (room_id, date, start_time, end_time)
        
        if key in self.reservations:
            print(f"Error: Room {room_id} is already reserved on {date} from {start_time} to {end_time} by {self.reservations[key]}.")
        else:
            self.reservations[key] = name
            print(f"Reserved Room {room_id} on {date} from {start_time} to {end_time} by {name}.")
            print(f"Current Reservations: {self.reservations}")

    def enterCancelStat(self, ctx: ConfRoomSchedulerParser.CancelStatContext):
        cancel_ctx = ctx.cancel()
        room_id = cancel_ctx.ID().getText()
        date = cancel_ctx.DATE().getText()
        start_time = cancel_ctx.TIME(0).getText()
        end_time = cancel_ctx.TIME(1).getText()
        
        if not self.validate_time(start_time) or not self.validate_time(end_time):
            print(f"Error: Invalid time format for cancellation.")
            return

        key = (room_id, date, start_time, end_time)
        
        if key in self.reservations:
            print(f"Cancelled reservation for Room {room_id} on {date} from {start_time} to {end_time} by {self.reservations[key]}.")
            del self.reservations[key]
            print(f"Current Reservations: {self.reservations}")
        else:
            print(f"Error: No reservation found for Room {room_id} on {date} from {start_time} to {end_time}.")
    
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ConfRoomSchedulerLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ConfRoomSchedulerParser(stream)
    tree = parser.prog()  # We are using 'prog' since this is the starting rule based on our ConfRoomScheduler grammar, yay!
    print(tree.toStringTree(recog=parser))

    semantic_checker = ConfRoomSchedulerSemanticChecker()
    walker = ParseTreeWalker()
    walker.walk(semantic_checker, tree)

if __name__ == '__main__':
    main(sys.argv)