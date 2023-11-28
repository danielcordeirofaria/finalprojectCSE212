# CSE 212 – Programming with Data Structures
## W10 Prove – Response Document

**Name:** Daniel Cordeiro Faria  
**Date:** 18/11/2023  
**Teacher:** Ephraim Kunz


## I. Welcome
   - Introduction
     - At a time when information technology is undergoing significant advances all the time, it is essential to know the fundamental structures of data structures for problem solving. Below we will talk about three of them: the stack, set, and tree. We will discuss their main characteristics, how they can influence problem-solving, and provide application examples.

## II. Stack
   - What is a Stack?
     - Stacks are data structures that store elements in a sequential format, stacking one item on top of another (imagine a stack of plates, for example). These structures allow us to "push" items onto the stack for storage and "pop" these elements off the stack when we need to remove them. Whenever a new element is inserted (or pushed), it is referred to as the "top" because it is the first element we will have access to.
     It follows a pattern known as Last In, First Out (LIFO), where the last item to be inserted will be the first to be removed. Imagine a stack of plates; whenever a plate is "stacked" under another, this last stacked plate is the closest (or the top of the stack). If we need to remove a plate, it is the top plate that will be taken off the structure.

   - What is the performance of Stack?
     - The performance of a stack is generally efficient. Both push and pop operations, adding elements to the top of the stack and removing them from the top, respectively, have a constant time complexity of O(1). This is because these operations involve only the top element of the stack, and the size of the stack does not affect the time it takes to perform these basic operations.
   - Problems that can be solved with a Stack
     - Examples of using a stack in a system include navigation between web pages or the undo/redo mechanism in text editors.
   - Applied example
     - There is a bank, called Nubank that the count pays you fees for you put your money there. But, there is a tax to pay, according to how much days the money has been there. The bank will consider your deposits as a stack. The last deposit to enter will be the first to leave. This way, it will deduct income tax in the best way for the account owner. Let's give an example:

    # Example of usage:

    class BankStatement:
        def __init__(self):
            self.balance = 0
            self.deposits = []

        def invest(self, amount, term):
            annual_interest_rate = 0.12
            period_interest_rate = (1 + annual_interest_rate) ** (term / 365) - 1
            interest_earned = amount * period_interest_rate
            net_amount = amount + interest_earned
            self.balance += net_amount
            self.deposits.append({"amount": net_amount, "term": term, "interest_earned": interest_earned})

        def calculate_tax(self, interest_earned, term):
            if term <= 180:
                return interest_earned * 0.225
            elif 181 <= term <= 360:
                return interest_earned * 0.20
            elif 361 <= term <= 720:
                return interest_earned * 0.175
            else:
                return interest_earned * 0.15

        def withdraw(self, withdrawal_amount):
            if not self.deposits:
                print("Error: No investment to withdraw from.")
                return

            net_amount_total = 0
            tax_total = 0

            while self.deposits and withdrawal_amount > 0:
                deposit = self.deposits.pop()  # Pop the last deposit

                withdrawal_amount += tax_total  # Adjust the withdrawal amount with the accumulated tax

                deposit_amount = deposit["amount"]
                term = deposit["term"]
                interest_earned = deposit["interest_earned"]

                tax = self.calculate_tax(interest_earned, term)
                net_amount = deposit_amount - tax

                if net_amount < withdrawal_amount:
                    net_amount_total += net_amount
                    tax_total += tax
                    withdrawal_amount -= net_amount
                else:
                    net_amount_total += withdrawal_amount
                    tax_total += withdrawal_amount * (tax / interest_earned)

                    # If there is a remainder, add the remaining amount back to the deposits with the same term
                    if net_amount - withdrawal_amount > 0:
                        self.deposits.append({"amount": net_amount - withdrawal_amount, "term": term,   "interest_earned": interest_earned})

                    withdrawal_amount = 0

            # Update the balance
            self.balance -= net_amount_total

            # Return the total net amount and total tax
            return net_amount_total, tax_total


## III. Set
   - What is a Set?
     - Sets are characterized by being a data structure, or collection, where there is no notion of order (at least, not intrinsically) and by not allowing repetition.
     Sets are what come closest to what we learn about sets in school mathematics classes and carry precisely these properties. We can ask the size of a set (which characterizes the number of elements in it, since there are no repetitions) and we can ask whether an element belongs or does not belong to the set.
     But we cannot do an operation like “get the third element” from the set. In fact, formulating this sentence for sets no longer makes sense. There is no “third” element of an unordered set.
     As you might have guessed, set structure comes from mathematics, and it is also possible to do operations such as union and intersection on data sets. One of the most common uses of this structure is in SQL databases.

   - What is the performance of Set?
     - The Big O (O(n)) notation for the performance of a set can vary depending on the operation being performed. Let's look at some common operations on sets and their average time complexities:
     Insertion: The average time to insert an element into a set is generally O(1), that is, constant. However, it may vary depending on the underlying implementation.
     Deletion: Similar to insertion, removing an element from a set is also, on average, O(1).
     Search: Searching for an element in a set also takes O(1) time on average, due to the unique nature of the elements in a set. However, in extreme cases it can approach O(n), especially if there are collisions or the set is implemented inefficiently.

   - Problems that can be solved with a Set
     - Sets are data structures useful for solving various problems, especially those that involve manipulating sets of single elements. Here are some common problems that can be efficiently solved using sets:
         - Duplicate Removal:
            Sets are ideal for removing duplicates from a collection of elements. Just add all elements to a set, and   duplicates will be automatically removed.
         - Belonging Check:
            It is efficient to check whether an element belongs to a set. This is useful for testing the presence of    specific elements in a dataset.
         - Union and Intersection Operations:
            Sets are effective for performing union, intersection, and difference operations between sets. This is useful   in situations where you need to compare or combine sets of elements.
         - Anagram Check:
            Using sets, it is possible to check whether two strings are anagrams (that is, whether they have the same   letters, regardless of the order).
         - Unique Element Count:
            If you need to count the number of unique elements in a collection, a set can be used to keep track of the  unique elements.
         - Common Element Detection:
            Checking for the presence of common elements between two collections is an efficient task with sets. Just   create sets for both collections and use the intersection operation.
         - Graph Problems:
            In algorithms that involve graphs, sets can be used to track the vertices visited, facilitating cycle   detection and breadth-first search, for example.
         - Subset Check:
            Sets can be used to check whether one set is a subset of another, which is useful in many applications, such    as checking whether a list of items is a subset of a catalog.
         - Checking for Unique Elements in a List:
            If you have a list and want to check if all the elements are unique, just convert the list to a set and     compare the sizes.

   - Applied example
     - An e-commerce platform wants to analyze the pages users visit. You have records of page views in a list but want to identify which unique pages were visited and how many times. Let's use sets to simplify this task.

        def analyze_interactions(views):
            # Converting the list of views into a set to get unique pages
            unique_pages = set(views)

            # Counting views per page using a dictionary
            page_count = {}
            for page in views:
                page_count[page] = page_count.get(page, 0) + 1

            # Printing results
            print("Unique Pages Visited:")
            for unique_page in unique_pages:
                print(f"{unique_page}")

            print("\nView Count per Page:")
            for page, count in page_count.items():
                print(f"{page}: {count} views")

        # Example of usage:
        user_views = ["home", "products", "cart", "products", "contact", "home", "products"]

        analyze_interactions(user_views)


## IV. Tree
   - What is a Tree?
     - The tree is a non-sequential structure, very useful for storing data in a hierarchical manner and which can be accessed quickly.
     A tree can be defined as a collection of data represented by nodes and arranged in hierarchical levels (instead of sequences like the structures seen previously).
     An example of a tree structure is company organization charts.
     The most common structure is the binary tree, which has a maximum of two child nodes from the initial node (called the root). A node can have parents, siblings and children; Nodes that have at least one child are called internal nodes, and nodes without children are called external or leaf nodes, how you can see in the link.

        - https://raw.githubusercontent.com/danielcordeirofaria/finalprojectCSE212/main/tree.drawio.png

     From the binary tree structure (with one child node to the left and one to the right of the root) it is possible to structure the so-called BST, or binary search tree, which uses the principle of the binary search algorithm to structure the data so that smaller values are to the left of the root and larger values to the right. This union of the algorithm with the data structure leads to greater efficiency in data manipulation, whether to search, change, include or remove elements.

   - What is the performance of Tree?
     - The performance (time complexity) of a tree may vary depending on the specific type of tree and the operation performed. Here are some of the typical time complexities for different operations on common trees:

       - Binary Search Trees (BST):

         - Insertion: O(log n) - In a balanced binary search tree, insertion occurs in logarithmic time.
         - Search: O(log n) - Search is also logarithmic in a balanced BST.
         - Removal: O(log n) - Removal in a balanced BST is logarithmic.
         - AVL Trees and Red-Black Trees:

         - Insert: O(log n) - These self-balancing trees ensure that the height of the tree is maintained at a logarithmic level.
         - Search: O(log n) - Search is logarithmic in an AVL tree or balanced red and black tree.
         - Removal: O(log n) - Removal in an AVL tree or balanced red and black tree is logarithmic.

       - B-Trees:

         - Insertion: O(log n) - B-trees also have a logarithmic complexity for insertion.
         - Search: O(log n) - The search in a B-tree is logarithmic.
         - Removal: O(log n) - Removal in a B-tree is logarithmic.

       - Trie Trees:

         - Insertion: O(m), where m is the key length - Complexity depends on the key length.
         - Search: O(m), where m is the key length - Complexity depends on the key length.
         - Heap Trees (Binary Heap, Binomial Heap, Fibonacci Heap, etc.):
         - Insertion: O(log n) - Insertion occurs in logarithmic time.
         - Minimum (or Maximum) Removal: O(log n) - Removing the minimum (or maximum) in a heap is logarithmic.
         - Trie Trees (Radix Tree) for Strings:
         - Insertion: O(m), where m is the length of the string - Complexity depends on the length of the string.
         - Search: O(m), where m is the length of the string - Complexity depends on the length of the string.

       - These time complexities are average or worst cases depending on the specific tree structure. In specific cases, the implementation and choice of data structure can impact these complexities. It is always important to consider problem-specific characteristics when choosing a tree to ensure desired performance for relevant operations.

   - Problems that can be solved with a Tree
     - The tree structure has several diverse uses, such as decision-making algorithms in machine learning, indexing databases, indexing and displaying files and folders in the file explorer of operating systems, among several other cases.

     The binary heap, as we have already mentioned, is used in priority queues (a special type of queue where elements are removed from the queue not in the FIFO pattern, but organized by priority: more priority at the beginning of the queue and less priority at the end) and also in a specific sorting algorithm, heap sort.

   - Applied example
     
     - In this example, we created a TreeNode class to represent the nodes of the tree. The tree_sum function calculates the sum of all elements in the tree recursively. The example creates a sample tree and calculates the sum of its elements. This is a simple example, and trees can be used to solve a variety of more complex problems, such as search algorithms, sorting, etc.

        class TreeNode:
          def __init__(self, value):
              self.value = value
              self.left = None
              self.right = None
  
          def tree_sum(root):
              """
              Function that calculates the sum of all elements in a binary tree.
          
              Args:
              - root: The root node of the tree.
          
              Returns:
              - The sum of all elements in the tree.
              """
              if root is None:
                  return 0
          
              # The sum is the value of the current node plus the sum of the left and right subtrees
              return root.value + tree_sum(root.left) + tree_sum(root.right)
          
          # Creating an example tree
          #       5
          #      / \
          #     3   8
          #    /|   |\
          #   1  4  6  9
          root = TreeNode(5)
          root.left = TreeNode(3)
          root.right = TreeNode(8)
          root.left.left = TreeNode(1)
          root.left.right = TreeNode(4)
          root.right.left = TreeNode(6)
          root.right.right = TreeNode(9)
          
          # Calculating the sum of the tree
          total_sum = tree_sum(root)
          
          # Displaying the result
          print("The sum of all elements in the tree is:", total_sum)
  
