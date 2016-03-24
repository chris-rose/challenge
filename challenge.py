# Allocation by title per month
cost = {'Manager': 300, 'Developer': 1000, 'QA Tester': 500, 'Subordinates': 0}

def getAllocation(department, allocation=cost['Manager']):
    
    '''Recursivley calls the subordinates of managers (including reporting managers) until a given manager no 
    no longer has any subordinates.  Aggregates allocation of all subordinates every recursion (Initial allocation
    set equal to one manager's allocation).'''
    
    subordinates = department['Subordinates']
    allocation = allocation + sum([cost[list(s.keys())[0]] for s in subordinates])
    try:
        return getAllocation(subordinates[len(subordinates)-1], allocation=allocation)
    except(KeyError):
        return allocation

def sliceDepartment(department, manager_name):
    
    '''Return a subset of a department as a new department, where the named manager is considered the 
    highest report.'''
    
    if department['Manager'] == manager_name:
        return department
    else:
        try:
            subordinates = department['Subordinates']
            return sliceDepartment(subordinates[len(subordinates)-1], manager_name=manager_name)
        except(KeyError): 
            print(manager_name, 'is not the name of a manager in the department.')