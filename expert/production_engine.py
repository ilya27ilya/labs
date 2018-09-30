# -*- coding: utf-8 -*-


from knowledge_base import Fact


def dds(rules, facts, goal):
    """ data–driven search """

    work_memory = facts[:]
    goal_passed = False
    new_fact = True

    while new_fact and not goal_passed:
        new_fact = False
        work_memory_set = set(work_memory)
        for rule in rules:
            antecedents_set = set([Fact(statement) for statement in rule.antecedent])
            if antecedents_set.intersection(work_memory_set) == antecedents_set:
                consequent = Fact(rule.consequent)
                if consequent not in work_memory:
                    work_memory.append(consequent)
                    new_fact = True

        if goal in work_memory:
            goal_passed = True

    return goal_passed


def gds(rules, facts, goal):
    """ goal–driven search """

    work_memory_set = set(facts)
    goal_passed = False
    new_goal = True

    goals = {
        goal: False
    }

    while new_goal and not goal_passed:
        new_goal = False
        for rule in rules:
            consequent = Fact(rule.consequent)
            antecedents_set = set([Fact(statement) for statement in rule.antecedent])
            if consequent in goals:
                if antecedents_set.intersection(work_memory_set) == antecedents_set:
                    goals[consequent] = True
                else:
                    new_goal = True
                    goals.pop(consequent, None)
                    for antecedent in antecedents_set.difference(work_memory_set):
                        goals[antecedent] = False

            if all(passed for passed in goals.values()):
                return True

    return goal_passed
