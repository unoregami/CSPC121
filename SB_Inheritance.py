class ClubMembers:
    def __init__(self, name, birthday, age, favoritefood, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favoritefood = favoritefood
        self.goal = goal

    def displayMembers(self):
        print(f"Name: {self.name}\nBirthday: {self.birthday}\nAge: {self.age}\nFavorite Food: {self.favoritefood}"
              f"\nGoal: {self.goal}\n")


class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, favoritefood, goal, position):
        super().__init__(name, birthday, age, favoritefood, goal)
        self.position = position

    def displayOfficers(self):
        print(f"Name: {self.name}\nBirthday: {self.birthday}\nAge: {self.age}\nFavorite Food: {self.favoritefood}"
              f"\nGoal: {self.goal}\nPosition: {self.position}\n")


m_1 = ClubMembers("Tom", "January 16", 14, "Ice Cream", "To be happy")
o_4 = ClubOfficers("Vera", "June 22", 16, "Beef stroganoff", "To be the world's greatest chef", "Treasurer")
m_1.displayMembers()
o_4.displayOfficers()
