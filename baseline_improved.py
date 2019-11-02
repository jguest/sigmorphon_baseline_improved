import sys
import english
import german


# todo switch on english / german
def main(argv):
    english.apply_best_rule(0, 0, 0, 0)
    german.apply_best_rule(0, 0, 0, 0)


if __name__ == "__main__":
    main(sys.argv)
