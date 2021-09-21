import random
import collections
ORIGINAL_CLICKS = [
  ("Home",             "Home Cleaning"),
  ("Home Cleaning",    "Restaurants"),
  ("Home Cleaning", "Plumbers"),
  ("Restaurants",      "Delivery"),
  ("Delivery",         "Address Search"),
  ("Address Search",   "Burgers"),
  ("Burgers",          "Order Delivery"),
  ("Order Delivery",   "Start Order"),
  ("Start Order",      "Turkey Burger"),
  ("Start Order", "Cheese Burger"),
 ("Turkey Burger", "Home"),
 ("A", "B"),
 ("B", "C")
]


# Oh darn, now they're all mixed up!
CLICKS = ORIGINAL_CLICKS[:]
random.shuffle(CLICKS)

# Given the shuffled click data and an origin page, find the final destination page
# ex: input: 'Home' -> output: 'Turkey Burger'


#######   YOUR SOLUTION HERE   ############

def findLeaf(graph, root, color):
    if not graph[root]:
        return [root]
    
    color[root] = 1 # visiting    
    
    res = []
        
    for v in graph[root]:
        if color[v] == 0:
            leaves = findLeaf(graph, v, color)
            if leaves:
                res.extend(leaves)
        
        if color[v] == 1:
            raise Exception('cycle detected')
        
    color[root] = 2 # visited        
    
    return res


def solve(clicks, root):

    graph = collections.defaultdict(list)
    
    for u, v in clicks:
        graph[u].append(v)
    
    # 0: not visited
    # 1: visiting
    # 2: visited
    color = collections.defaultdict(int)
        
    print(findLeaf(graph, root, color))
    
solve(CLICKS, 'Home')
