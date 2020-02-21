from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# UNCOMMENT TO VIEW MAP
# UNCOMMENT TO VIEW MAP
world.print_rooms()

player = Player(world.starting_room)

# Fill this out
traversalPath = []
def find_path():
    # Large Graph and medium
    visited = {
      0: {'w': '?', 's': '?', 'n': '?', 'e': '?' }
    }
    s = Stack()
    prev_room = 0
    direction_traveled = ''
    # Initialize Stack
    s.push(0)
    while s.size() > 0:
        cur_room = s.pop()
        # print("------------")
        # print("Visited:", visited)
        # print(f'Current room: {cur_room}')
        # print(f'Previous Room: {prev_room}')
        # print("Current Traverse List:", traversalPath)
        mark_visiting(player.current_room.id, prev_room, visited, direction_traveled)
        if '?' in visited[cur_room].values():
        # Pick direction from possible directions in visited object that is a '?'
            for key, value in visited[cur_room].items():
        # Travel to first direction with '?' direction
                if value == '?':
                    player.travel(key)
                    # print("Direction Traveled", direction_traveled)
                    s.push(player.current_room.id)
                    direction_traveled = key
                    traversalPath.append(direction_traveled)
                    # Mark Visited
                    prev_room = cur_room
                    break
        else:
            # Check if there are any nodes with ?'s
            if bfs(cur_room, visited) is None:
                # print("No nodes left with ?'s")
                return
            # Find nearest node with '?'s
            path_to_exit = bfs(cur_room, visited)
            new_traverse = []
            # Convert array of paths to directions
            for index, room in enumerate(path_to_exit):
                if index < len(path_to_exit) - 1 and path_to_exit[index + 1] in visited[room].values():
                    for key, value in visited[room].items():
                        if value == path_to_exit[index + 1]:
                            new_traverse.append(key)
            # Move there
            for move in new_traverse:
                prev_room = player.current_room.id
                player.travel(move)
                direction_traveled = move
                traversalPath.append(move)
            if '?' in visited[player.current_room.id].values():
                s.push(player.current_room.id)



def mark_visiting(cur_room, prev_room, visited, direction_traveled):
    # print(f"In Mark Visiting--- Current Room: {cur_room}, Prev Room: {prev_room}, direction traveled: {direction_traveled}")
    if cur_room not in visited:
        # Get all exits of current room, add as values of current visited key
        exits_array = player.current_room.get_exits()
        new_room_exits = {}

        for direction in exits_array:
            new_room_exits[direction] = '?'
        # If direction_traveled was south, then direction for north will be previous node
        if direction_traveled == 's':
            new_room_exits['n'] = prev_room
        # If direction_traveled was north, then direction for south will be previous node
        if direction_traveled == 'n':
            new_room_exits['s'] = prev_room
        # If direction_traveled was east, then direction for west will be previous node
        if direction_traveled == 'e':
            new_room_exits['w'] = prev_room
        # If direction_traveled was west, then direction for east will be previous node
        if direction_traveled == 'w':
            new_room_exits['e'] = prev_room
        # finally add new room to visited
        visited[cur_room] = new_room_exits
        # Add id of current room to visited[prev_room][direction_traveled]
        visited[prev_room][direction_traveled] = cur_room
        # print("FInal Visited", visited)

    else:
        # take the opposite of the direction_traveled
        # in visited, set current room's opposite of direction_traveled as prev_room
        if direction_traveled == 's':
            visited[cur_room]['n'] = prev_room
        # If direction_traveled was north, then direction for south will be previous node
        if direction_traveled == 'n':
            visited[cur_room]['s'] = prev_room
        # If direction_traveled was east, then direction for west will be previous node
        if direction_traveled == 'e':
            visited[cur_room]['w'] = prev_room
        # If direction_traveled was west, then direction for east will be previous node
        if direction_traveled == 'w':
            visited[cur_room]['e'] = prev_room

def bfs(starting_vertex, visited):
    # Create an empty queue and enqueue the starting Vertex ID
    q = Queue()
    q.enqueue([starting_vertex])
    # Create and empty set to store visited vertices
    visited_rooms = set()
    # While the queue is not empty..
    while q.size() > 0:
        # Dequeue the first vertex
        path = q.dequeue()
        # If that vertex has not been visited
        v = path[-1]
        if v not in visited_rooms:

            # Mark it as visited
            if '?' in visited[v].values():
                return path
            visited_rooms.add(v)
            # Then add all of its neighbors to the back of the queue
            for key, value in visited[v].items():
                path_copy = path.copy()
                path_copy.append(value)
                q.enqueue(path_copy)



# TRAVERSAL TEST
find_path()
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversalPath:
    # print("Move:", move)
    # print("Current:", player.current_room)
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    #  uncomment to see path
    print(traversalPath)
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# ######
# UNCOMMENT TO WALK AROUND
# ######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    else:
        print("I did not understand that command.")