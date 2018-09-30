# -*- coding: utf-8 -*-


from knowledge_base import rules_from_file
from knowledge_base import facts_from_file
from knowledge_base import goal_from_file
from production_engine import dds
from production_engine import gds


def main():
    rules = rules_from_file("rules.txt")
    facts = facts_from_file("facts.txt")
    goal = goal_from_file("goal.txt")

    print(u"\nПРАВИЛА\n")
    for r in rules:
        print(r)

    print(u"\nФАКТЫ\n")
    for f in facts:
        print(f)

    print(u"\nЦЕЛЬ: %s" % goal)

    print(u"\nДОСТИЖИМОСТЬ ПРЯМОЙ ВЫВОД: %s" % dds(rules, facts, goal))

    print(u"\nДОСТИЖИМОСТЬ ОБРАТНЫЙ ВЫВОД: %s\n" % gds(rules, facts, goal))


if __name__ == "__main__":
    main()
