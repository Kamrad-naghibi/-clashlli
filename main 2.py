import time

first_castle_health = 20
second_castle_health = 20

stat_dict = {"first castle health" : first_castle_health, "first castle soldiers" : [], "second castle health" : second_castle_health, "second castle health" : []}
coins_dict = {"first": 0, "second": 0}
events_dict = {}

def get_status():
    stat_dict = {"first castle health": first_castle_health, "first castle soldiers": [],"second castle health": second_castle_health, "second castle health": []}
    return(stat_dict)

def each(team_id, soldier_id):
    if int(soldier_id) <= coins_dict[team_id]:
        stat_dict[team_id, "castle soldiers"].append((str(int(soldier_id)-1), 0))
        return(True)
    else:
        return(False)

def add_event(call_back, event_id):
    events_dict[event_id] = call_back

while True:
    coins_dict["first"] += 1
    coins_dict["second"] += 1
    time.sleep(1)