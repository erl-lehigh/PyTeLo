import sys
import logging
from lomap import Ts
from visualization import show_environment
from swarm_planning import swarm_planning


def setup_logging(logfile='cs1.log', loglevel=logging.DEBUG,
                  fs='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
                  dfs='%m/%d/%Y %I:%M:%S %p'):
    if logfile is not None:
        logging.basicConfig(filename=logfile, level=loglevel,
                            format=fs, datefmt=dfs)

    root = logging.getLogger()
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(loglevel)
    ch.setFormatter(logging.Formatter(fs, dfs))
    root.addHandler(ch)


def case_simple(ts_filename='case_study_1.yaml'):
    '''TODO:
    '''
    setup_logging()

    ts = Ts.load(ts_filename)
    for u, v in ts.g.edges():
        print(v, u)
        # assert ts.g.has_edge(v, u)
    # show_environment(ts)

    for u in ts.g:
        logging.debug('State: %s, Data: %s', u, str(ts.g.node[u]))

    initial_state = 'q0'
    split_bound = 14

    #    '(G[5,6] green)||(F[4,6](blue||red))||(G[5,7](yellow||blue))'
    # specification = '(G[1,4] blue) && (G[2,4] red) && (G[6,7] cyan) && (G[6,7] red)\
    #                 # && (G[6,7] gray) && ((G[8,9] green))'


    # specification = '(F[0,5] A)' # 1
    # specification = '(G[0,3] A) || (G[1,4] A) || (G[2,5] A)' # 2
    # specification = '(F[0,2] (G[0,3]A))' # 2

    # specification = '((G[0,2] J) && (G[0,3] B)) || ((G[1,3] J) && (G[1,4] B))' \
    #                 ' || ((G[2,5] J) && (G[2,6] B)) || ((G[3,6] J) && (G[3,7] B))' # 3
    # specification = '(G[1,5] L) || (G[1,7] I) || (G[2,6] L) '

    specification = '((G[0,2] D) || (G[1,3] D) || (G[2,4] D) || (G[3,5] D)) ' \
                    '&& ((G[7,9] K) || (G[8,10] K) || (G[9,11] K) || (G[10,12] K) || (G[11,13] K) || (G[12,14] K)'
    m, obj = swarm_planning(ts, initial_state, specification, split_bound)
    print(m, obj)

if __name__ == '__main__':
    case_simple()

