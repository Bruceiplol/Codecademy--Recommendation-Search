import animedata

class TreeNode:
  def __init__(self, value):
    self.value = value 
    self.children = []

  def add_child(self, child_node):
    self.children.append(child_node) 
    
  def remove_child(self, child_node):
    self.children = [child for child in self.children 
                     if child is not child_node]

  def traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0][4]
    equal = [x for x in lst if x[4] == pivot]
    lesser = [x for x in lst if x[4] < pivot]
    greater = [x for x in lst if x[4] > pivot]
    return quicksort(greater) + equal + quicksort(lesser)


def display_anime(lst):
    sorted_lst = quicksort(lst)
    for anime in sorted_lst:
        print("="*50 +"\n")
        print(f"English Title: {anime[2]}")
        print(f"Japanese Title: {anime[1]}")
        print(f"Genre: {anime[0]}")
        print(f"Year of Publication: {anime[3]}")
        print(f"Rating: {anime[4]} / 5")
        print(f"Description: {anime[5]}")
    print("="*50 +"\n")

def build_tree(anime_data):
    root = TreeNode("Genres")
    for anime in anime_data:
        genre = anime[0]
        anime_node = TreeNode(anime)
        genre_node = None
        for child in root.children:
            if child.value == genre:
                genre_node = child
                break
        if not genre_node:
            genre_node = TreeNode(genre)
            root.add_child(genre_node)
        genre_node.add_child(anime_node)
    return root