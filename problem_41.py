"""
Daily_Problem_41

This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one.
All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and
starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller."""

from copy import copy


def find_itinerary(flights_data, start_airport):
    if not flights_data:
        return [start_airport]
    stops = [stop for stop in flights_data if stop[0] is start_airport]
    for stop in sorted(stops):
        temp_data = copy(flights_data)
        temp_data.remove(stop)
        itinerary = find_itinerary(temp_data, stop[1])
        if itinerary:
            return [start_airport] + itinerary
    return None


input_list = [([('A', 'C'), ('A', 'B'), ('C', 'D'), ('D', 'A')], 'A'),
              ([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'),
              ([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')]
for itinerary_list, start_location in input_list:
    print(find_itinerary(itinerary_list, start_location))
    print('*' * 15)
