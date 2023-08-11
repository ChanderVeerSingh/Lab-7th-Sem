import numpy as np

def is_consistent(hypothesis, instance):
    for i in range(len(hypothesis)):
        if hypothesis[i] != '?' and hypothesis[i] != instance[i]:
            return False
    return True

def generalize(hypothesis, instance):
    new_hypothesis = list(hypothesis)
    for i in range(len(hypothesis)):
        if hypothesis[i] == '?':
            new_hypothesis[i] = instance[i]
    return tuple(new_hypothesis)

def specialize(hypothesis, instance):
    new_hypotheses = []
    for i in range(len(hypothesis)):
        if hypothesis[i] != instance[i]:
            new_hypothesis = list(hypothesis)
            new_hypothesis[i] = '?'
            new_hypotheses.append(tuple(new_hypothesis))
    return new_hypotheses

def candidate_elimination(training_data):
    attributes = len(training_data[0]) - 1
    S = [('?',) * attributes]
    G = [('',) * attributes]

    for instance in training_data:
        if instance[-1] == 'Y':
            for i in range(len(S)):
                if not is_consistent(S[i], instance):
                    del S[i]
                    S.insert(i, generalize(S[i], instance))
                    for j in range(len(S)):
                        if i != j and is_consistent(S[j], instance):
                            del S[j]

        else:
            G_temp = []
            for i in range(len(G)):
                if not is_consistent(G[i], instance):
                    del G[i]
                    G_temp.extend(specialize(G[i], instance))
            G.extend(G_temp)
            for i in range(len(G)):
                for j in range(len(G)):
                    if i != j and is_consistent(G[j], instance):
                        del G[j]

    return S, G

# Example training data: Each instance has attributes followed by the target concept (Y/N)
training_data = [
    ('Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Y'),
    ('Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Y'),
    ('Cloudy', 'Cold', 'High', 'Weak', 'Cold', 'N'),
    ('Sunny', 'Warm', 'High', 'Strong', 'Cold', 'Y')
]

S, G = candidate_elimination(training_data)

print("Final Specific Hypotheses (S):", S)
print("Final General Hypotheses (G):", G)