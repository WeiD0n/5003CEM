class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_user(self, person):
        name = person.name.lower()
        if name not in self.adjacency_list:
            self.adjacency_list[name] = {'person': person, 'following': []}
            return True
        return False

    def add_following(self, follower, followee):
        follower = follower.lower()
        followee = followee.lower()
        if follower in self.adjacency_list and followee in self.adjacency_list:
            if followee not in self.adjacency_list[follower]['following']:
                self.adjacency_list[follower]['following'].append(followee)
                return True
        return False

    def remove_following(self, follower, followee):
        follower = follower.lower()
        followee = followee.lower()
        if follower in self.adjacency_list:
            if followee in self.adjacency_list[follower]['following']:
                self.adjacency_list[follower]['following'].remove(followee)
                return True
        return False

    def get_following(self, user_name):
        return self.adjacency_list.get(user_name.lower(), {}).get('following', [])

    def get_followers(self, user_name):
        user_name = user_name.lower()
        return [name for name, data in self.adjacency_list.items() if user_name in data['following']]

    def get_all_users(self):
        return [data['person'].name for data in self.adjacency_list.values()]

    def get_user(self, name):
        return self.adjacency_list.get(name.lower(), {}).get('person', None)


class Person:
    def __init__(self, name, gender, biography, privacy='public'):
        self.name = name
        self.gender = gender
        self.biography = biography
        self.privacy = privacy

    def display_profile(self):
        print(f"Name: {self.name}")
        if self.privacy == 'private':
            print("(Private profile – details hidden)")
        else:
            print(f"Gender: {self.gender}")
            print(f"Bio: {self.biography}")


def main():
    graph = Graph()

    initial_users = [
        Person("Alice", "Female", "Love art and books", "public"),
        Person("Bob", "Male", "Foodie & traveler", "private"),
        Person("Charlie", "Male", "Tech geek", "public"),
        Person("Diana", "Female", "Photographer", "public"),
        Person("Eva", "Female", "Nature lover", "private"),
    ]

    for user in initial_users:
        graph.add_user(user)

    graph.add_following("Alice", "Bob")
    graph.add_following("Bob", "Charlie")
    graph.add_following("Charlie", "Diana")
    graph.add_following("Diana", "Eva")
    graph.add_following("Eva", "Alice")
    
    while True:
        print("\n--- Social Media Graph Menu ---")
        print("1. Display all user names")
        print("2. View profile details")
        print("3. View followed accounts")
        print("4. View followers")
        print("5. Add user")
        print("6. Follow user")
        print("7. Unfollow user")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            print("\nAll users:")
            for name in graph.get_all_users():
                print(f"- {name}")

        elif choice == '2':
            name = input("Enter user name to view profile: ")
            person = graph.get_user(name)
            if person:
                person.display_profile()
            else:
                print("User not found.")

        elif choice == '3':
            name = input("Enter user name to view following: ")
            person = graph.get_user(name)
            if person:
                following_usernames = graph.get_following(name)
                if following_usernames:
                    following_names = [graph.get_user(u).name for u in following_usernames]
                    print(f"{person.name} follows: {', '.join(following_names)}")
                else:
                    print(f"{person.name} follows: No one")
            else:
                print("User not found.")

        elif choice == '4':
            name = input("Enter user name to view followers: ")
            person = graph.get_user(name)
            if person:
                follower_usernames = graph.get_followers(name)
                if follower_usernames:
                    follower_names = [graph.get_user(u).name for u in follower_usernames]
                    print(f"{person.name} is followed by: {', '.join(follower_names)}")
                else:
                    print(f"{person.name} is followed by: No followers")
            else:
                print("User not found.")

        elif choice == '5':
            name = input("Enter new user's name: ")
            if name.lower() in graph.adjacency_list:
                print("A user with that name already exists.")
            else:
                gender = input("Enter gender: ")
                bio = input("Enter bio: ")
                privacy = input("Privacy (public/private): ").lower()
                person = Person(name, gender, bio, privacy)
                if graph.add_user(person):
                    print(f"User {name} added.")
                else:
                    print("Failed to add user.")

        elif choice == '6':
            follower = input("Who wants to follow? ")
            followee = input("Who to follow? ")
            if follower.lower() in graph.adjacency_list and followee.lower() in graph.adjacency_list:
                success = graph.add_following(follower, followee)
                if success:
                    print(f"{graph.get_user(follower).name} now follows {graph.get_user(followee).name}")
                else:
                    print(f"{graph.get_user(follower).name} is already following {graph.get_user(followee).name}")
            else:
                print("One or both users not found.")

        elif choice == '7':
            follower = input("Who wants to unfollow? ")
            followee = input("Who to unfollow? ")
            if follower.lower() in graph.adjacency_list and followee.lower() in graph.adjacency_list:
                success = graph.remove_following(follower, followee)
                if success:
                    print(f"{graph.get_user(follower).name} has unfollowed {graph.get_user(followee).name}")
                else:
                    print(f"{graph.get_user(follower).name} is not following {graph.get_user(followee).name}")
            else:
                print("One or both users not found.")

        elif choice == '8':
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
