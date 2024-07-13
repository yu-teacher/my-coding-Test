def solution(a, b, g, s, w, t):
    def can_transport(time):
        total_gold = total_silver = total_mineral = 0
        for gold, silver, weight, trip_time in zip(g, s, w, t):
            round_trips = time // (2 * trip_time)
            if time % (2 * trip_time) >= trip_time:
                round_trips += 1
            
            max_transport = min(round_trips * weight, gold + silver)
            
            total_gold += min(max_transport, gold)
            total_silver += min(max_transport, silver)
            total_mineral += max_transport
        
        return total_gold >= a and total_silver >= b and total_mineral >= a + b

    left, right = 1, int(1e15)
    
    while left < right:
        mid = (left + right) // 2
        if can_transport(mid):
            right = mid
        else:
            left = mid + 1
    
    return left