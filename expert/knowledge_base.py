# -*- coding: utf-8 -*-


class Rule:
    def __init__(self, antecedent=None, consequent=None):
        self.antecedent = str(antecedent).split()
        self.consequent = str(consequent)

    def __eq__(self, other):
        return set(self.antecedent) == set(other.antecedent)\
               and self.consequent == other.consequent

    def __str__(self):
        return u"%s => %    s" % (str(self.antecedent), self.consequent)

    def product(self, fact):
        if all(antecedent == fact.antecedent for antecedent in self.antecedent):
            return Fact(self.consequent)
        return Fact()


class Fact(Rule):
    def __init__(self, consequent=None):
        super(Fact, self).__init__(None, consequent)

    def __hash__(self):
        return hash(self.consequent)

    def __str__(self):
        return u"%s" % str(self.consequent)


def rule_from_line(line):
    a, b = line.strip(" \n").split("=>")
    return Rule(a.strip(), b.strip())


def rules_from_file(filename):
    rules = []
    f = open(filename, "r")
    for line in f.readlines():
        new_rule = rule_from_line(line)
        rules.append(new_rule)
    f.close()
    return rules


def fact_from_line(line):
    a = line.strip(" \n")
    return Fact(a)


def facts_from_file(filename):
    facts = []
    f = open(filename, "r")
    for line in f.readlines():
        new_fact = fact_from_line(line)
        facts.append(new_fact)
    f.close()
    return facts


def goal_from_file(filename):
    f = open(filename, "r")
    goal = fact_from_line(f.readline())
    f.close()
    return goal
