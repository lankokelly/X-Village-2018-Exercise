def maker(n):
    def action(x): # Generate and return action
        return n ** x # action retains N from enclosing scope return action
    return action

f = maker(9)
print(f(5)) #59049