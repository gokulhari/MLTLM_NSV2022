# Sample file for using the ACOW package

from ACOW import *

# User defined automaton


def define_automaton():
    a = automaton()
    #sg = StateGen(3,'s','a')
    a.INITIAL_STATE = 's2'
    a.DEST_STATE = 's3'
    #a.STATE, a.DELTA = sg.gen_aut()
    a.STATE = {
        's0': {'a0': 0, 'a1': 0},
        's1': {'a0': 0, 'a1': 1},
        's2': {'a0': 1, 'a1': 0},
        's3': {'a0': 1, 'a1': 1},
    }
    a.DELTA = {
        's0': {'s0', 's1', 's2', 's3'},
        's1': {'s0', 's1', 's2', 's3'},
        's2': {'s0', 's1', 's2', 's3'},
        's3': {'s0', 's1', 's2', 's3'},
    }
    print(a)
    return a


def main():
    # a = define_automaton()
    # a.init()
    # a.show()# show a .pdf figure of the state space model
    #MTL = '(G[4]a0) & (G[3]a1) & a0'
    MTL = 'a0 & b0 & G[1,3]'
    top_node = parser.parse(MTL)
    # comment this line if you don't want to optimze the AST
    cnt2observer = MTLparse.optimize()
    SCQ_size, _ = MTLparse.queue_size_assign()
    MTLparse.gen_assembly()
    print(MTLparse.gen_serialization())

    # solution = Search(a,cnt2observer,agent='DES')
    # solution.run(['s0','s0','s0','s1','s1','s1','s1','s1','s1','s1','s3','s2','s2','s3','s2','s3','s3','s3','s3','s2','s2','s3','s3','s3','s3','s0','s1','s1','s1','s0','s0'])


if __name__ == "__main__":
    main()
