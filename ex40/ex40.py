class Song(object):
    """
    Docstring
    """

    def __init__(self, lyrics):
        print("Here init")
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print("Here def func")
        for line in self.lyrics:
            print(line)

    def tryout(self):
        res = []
        for line in self.lyrics:
            res.append(line.split(" "))

        print(res)


happy_bday = Song(["Happy Birthday to you", "I don't want to get sued", "So I'll stop right there"])
bulls_on_parade = Song(['They rally around tha family', 'With pockets full of shells'])

happy_bday_spanish = ["Cumple años feliz", "Cumple años feliz", "Cumple años Jorge"]
cumple_anos = Song(happy_bday_spanish)
cumple_anos.tryout()

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
cumple_anos.sing_me_a_song()
