# 81/100
# import re
#
#
# tickets = input().split()
# tickets = ''.join(tickets)
# tickets = tickets.split(',')
# symbols = ['@', '#', '$', '^']
#
# for ticket in tickets:
#     if len(ticket) == 20:
#         for symbol in symbols:
#             if symbol in ticket:
#                 pattern = r"[a-z]|[A-Z]"
#                 left_side = max(re.split(pattern, ticket[0:10]))
#                 right_side = max(re.split(pattern, ticket[10:20]))
#                 repetition = 0
#                 if ticket.count(symbol) == 20:
#                     print(f'ticket "{ticket}" - {int(ticket.count(symbol)/2)}{symbol} Jackpot!')
#                     break
#                 if len(left_side) >= 6 and len(right_side) >= 6 and left_side[0] == right_side[0]:
#                     if left_side < right_side:
#                         repetition = len(left_side)
#                     else:
#                         repetition = len(right_side)
#                     print(f'ticket "{ticket}" - {repetition}{symbol}')
#                     break
#         else:
#             print(f'ticket "{ticket}" - no match')
#     else:
#         print("invalid ticket")

# 100/100
def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uninterrupted_match_length
            # We have winning ticket
            if winning_symbol_repetition in left_part \
                    and winning_symbol_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))
    