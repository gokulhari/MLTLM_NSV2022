from .AST import MODRED, BOOL, ATOM, Observer

# Stride dictionary uses tuples as keys to act as a 2 key index since they hash
# Using Gokul's table from the MLTLM branch, I could make this mor clever....
STRIDE = {
    ('a','b'): 2,
    ('a','c'): 6,
    ('a','d'): 24,

    ('b','c'): 3,
    ('b','d'): 12,

    ('c','d'): 4
}

def flow_down(root):
    children = [child for child in root.child if child is not None and not isinstance(child, BOOL)]
    if isinstance(root, Observer): # Statements and programs do not have timescales
        for child in children:
            if child.ts is None:
                child.ts = root.ts
    for child in children:
        flow_down(child)
        
def flow_down_semantics(root):
    children = [child for child in root.child]
    if ((root.sem_ts is None)):
        if (root.ts is None and (isinstance(root,Observer))):
            print(f"Warning: The root node does not have a type. We default to the biggest time scale as it has the least memory requirements. Please assign trace type to evaluate in by restating formula f as G[0,0,type](f).")
            root.ts = 'd'
            root.sem_ts = root.ts
        else:
            root.sem_ts = root.ts
    if isinstance(root, Observer): # Statements and programs do not have timescales
        # for propositional ops, they have no ts, assign sem_ts to them
        if root.ts is None:
                root.ts = root.sem_ts
        for child in children:          
            child.sem_ts = root.ts
    for child in children:
        flow_down_semantics(child)

def push_up(root):
    if root.ts is None:
        for child in [child for child in root.child if child is not None]:
            if not isinstance(child, (ATOM, BOOL)) and child.ts is None: # Skip leaves (Bools and Atoms)
                push_up(child)
        child_tses = [child.ts for child in root.child if child is not None and not isinstance(child, BOOL)]
        if child_tses.count(child_tses[0]) != len(child_tses): # Check for children consistency
            print(f"Warning: Ambigous mismatched binary time series - keeping first ({child_tses[0]})")
        if isinstance(root, Observer): # Statements and programs do not have timescales
            root.ts = child_tses[0]

def insert_projection2(root):
    children = [child for child in root.child if child is not None and not isinstance(child, BOOL)]
    for child in children:
        # Reusing children intentionally skips inserted projections
        insert_projection2(child)
        
    for child in children:
        if (child.ts != child.sem_ts) and isinstance(root, Observer):
            # insert Projection
            proj = MODRED(child, STRIDE[child.ts, child.sem_ts])
            # Replace child in root.child list - fixes left/right
            temp = list(map(lambda x: x if x is not child else proj, root.child))
            root.child = temp
            proj.pre = root

# Collect all time scales:


# This function just checks if at the leaves, the atomics are assigned 
# anything other than "a" as the time scale, then a projection in inserted 
# above the atomic and converts the atomic to time scale "a".
def insert_projection_at_leaves(root):
    children = [child for child in root.child if child is not None and not isinstance(child, BOOL)]
    
    
    for child in children:
        if (isinstance(child,(ATOM,BOOL ))):
            if (child.sem_ts != "a"):
                proj = MODRED(child, STRIDE["a", child.sem_ts])
                temp = list(map(lambda x: x if x is not child else proj, root.child))
                root.child = temp
                proj.pre = root
        else:
            insert_projection_at_leaves(child) 

    

def insert_projection(root):
    children = [child for child in root.child if child is not None and not isinstance(child, BOOL)]
    for child in children:
        if (child.ts != root.ts) and isinstance(root, Observer):
            # insert Projection
            proj = MODRED(child, STRIDE[child.ts, root.ts])
            # Replace child in root.child list - fixes left/right
            root.child = list(map(lambda x: x if x is not child else proj, root.child))
            proj.pre = root

    for child in children:
        # Reusing children intentionally skips inserted projections
        insert_projection(child)

def tree_print(root, depth=0):
    offset = '\t'*depth
    print(f"{offset}{root.name}_{root.ts}_{root.sem_ts}")
    children = [child for child in root.child if child is not None]
    for child in children:
        tree_print(child, depth=depth+1)

def collect(root, out):
    children = [child for child in root.child if child is not None and not isinstance(child, BOOL)]
    for child in children:
        if isinstance(child, Observer):
            out.add(child.ts)
        collect(child,out)
            
            

def project_timescales(root):
    # The root needs a time scale to define on what type is the trace being evaluated. If it lacks one, the we default to the biggest time scale as it has the least memory requirements.

    out = set()
    collect(root,out)
    if (None in out):
        out.remove(None)
    
    # Need projection only if formula is MLTLM, else just use AST as is.
    if not (len(out) == 0):
        if root.ts is None:     
            root.ts = 'd'
            
        print("\n\nInput Tree:")
        tree_print(root)

        flow_down_semantics(root)
        print("\n\nFlow Down:")
        tree_print(root)

        
        insert_projection2(root)
        print("\n\nProjected:")
        tree_print(root)
    
    
        insert_projection_at_leaves(root)
        print("\n\nProjected and leaves modified:")
        tree_print(root)

## TODO: In the leaves, check that each atomic in the AST has a single type assigned. For example (G[1,2,b] a0 & G[2,4,c] a0) is an invalid formula. If not, throw a warning saying that atomics cannot have different types.