#!/usr/bin/env python3
import hazwaz


class World(hazwaz.Command):
    """
    Greet the whole world.
    """

    def main(self):
        print("Hello world!")


class Individual(hazwaz.Command):
    """
    Greet an individual.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "gretee",
            help="The person to be greeted",
        )

    def main(self):
        print("Hello {}".format(self.args.gretee))


class Greet(hazwaz.MainCommand):
    """
    Greet people in different ways.
    """
    commands = (
        World(),
        Individual(),
    )


if __name__ == "__main__":
    Greet().run()
