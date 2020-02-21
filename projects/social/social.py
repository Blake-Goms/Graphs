import random
from util import Stack, Queue

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # Create friendships
        # create a list with all possible friendships
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))


        # Shuffle the list
        random.shuffle(possible_friendships)
        print("----")
        # print(possible_friendships)
        print("----")
        # Grab the first N pairs from the list and create those friendships
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        # avg_friendships = total_friendships / num_users
        # total_friendships = avg_friendships * num_users
        # N = avg_friendships * num_users // 2

    
    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        friendships_to_create = avg_friendships * num_users
        friendships = 0
        collisions = 0
        # 2. while the result of that is < the required average
        while friendships < friendships_to_create:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            # 3. pick two users at random - if they are not already friends, make them friends
            if self.add_friendship(user_id, friend_id):
                friendships += 2
            else:
                # 4. if they are already friends, try again
                collisions += 1
        print(f"COLLISIONS: {collisions}")

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME\
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting user_id to the queue
        q.enqueue([user_id])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            # GRAB THE LAST VERTEX FROM THE PATH
            path = q.dequeue()
            p = path[-1]
            if p not in visited:
                # Mark it as visited
                visited[p] = path
                
                for friend_id in self.friendships[p]:
                    # (Make a copy of the path before adding)
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('Users', sg.users, '\n')
    print('Friendships', sg.friendships, '\n')
    connections = sg.get_all_social_paths(1)
    print('Connections', connections, '\n')
    print(len(connections))
    total = 0
    for connection in connections:
        total+= len(connections[connection])
    print(total / len(connections) -1)

# import time

# if __name__ == '__main__':

#     num_users = 1000
#     avg_friendships = 999


#     sg = SocialGraph()
#     start_time = time.time()
#     sg.populate_graph(num_users, avg_friendships)
#     end_time = time.time()
#     print (f"\nQuadratic runtime: {end_time - start_time} seconds")

#     sg = SocialGraph()
#     start_time = time.time()
#     sg.populate_graph_linear(num_users, avg_friendships)
#     end_time = time.time()
#     print (f"\nLinear runtime: {end_time - start_time} seconds")