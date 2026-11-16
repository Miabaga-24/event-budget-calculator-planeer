#Muhammad Musa
def participant_cost(attendees, food_per_person, transport_per_person):
    total = attendees * (food_per_person + transport_per_person)
    return total

# Test cases
print(participant_cost(10, 1000, 500))  # 15000
print(participant_cost(0, 1000, 500))   # 0

            #Mustapha Ishaq
def event_total(attendees, food_per_person, transport_per_person, venue_cost):
    total = participant_cost(attendees, food_per_person, transport_per_person)
    total += venue_cost
    return total

# Test cases
print(event_total(10, 1000, 500, 5000))  # 20000
print(event_total(0, 1000, 500, 3000))   # 3000

          #Usman Ibrahim
def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"

# Test cases
print(budget_status(20000, 15000))  # Within budget
print(budget_status(20000, 20000))  # Within budget
print(budget_status(20000, 25000))  # Over budget



        #Usman Bello
def event_summary(event_name, total, status):
    return f"{event_name}: total {total} naira. {status}."


# Test cases
print(event_summary("Study Day", 15000, "Within budget"))
print(event_summary("Sports Day", 25000, "Over budget"))