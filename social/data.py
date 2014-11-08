import social
class Perform:
    apiaccesscode = ""
    __graph = social.GraphAPI(apiaccesscode)
    def run(self):
        profile = self.__graph.get_object("me")
        friends = self.__graph.get_connections("me", "friends")
        print(friends)
        for friend in friends['data']:
            print(friend['name'])
        print(profile.get("birthday"))
        """__graph.put_object("me", "feed", message="I am writing on my wall!")"""

p = Perform()
p.run()