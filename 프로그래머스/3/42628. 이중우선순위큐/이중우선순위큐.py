import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    number_set = set()

    for operation in operations:
        command, number = operation.split()
        number = int(number)

        if command == 'I':
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            number_set.add(number)
        elif number_set:
            if number == 1:
                while -max_heap[0] not in number_set:
                    heapq.heappop(max_heap)
                max_value = -heapq.heappop(max_heap)
                number_set.remove(max_value)
            else:
                while min_heap[0] not in number_set:
                    heapq.heappop(min_heap)
                min_value = heapq.heappop(min_heap)
                number_set.remove(min_value)

    if number_set:
        return [max(number_set), min(number_set)]
    else:
        return [0, 0]