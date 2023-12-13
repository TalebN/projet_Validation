from hanoi import HanoiRG
from bfs import bfs_search

hanoi_rg = HanoiRG(nbStacks=3, nbDisks=3)

result_states = bfs_search(hanoi_rg, hanoi_rg.is_final_state)
hanoi_rg.print_results(result_states)