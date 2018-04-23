
Inputs: 

For each graph G, three text files and the Number of nodes (N) is given as follows:

    1) N                                          %% An integer number, number of nodes in G
    2) AdjacencyMatrix_of_Graph_G.txt             %% text file, N Rows, N columns, contain 0,1
    3) Node_Information_of_Graph_G.txt            %% text file, N Rows, 4 Columns
    4) SourceNode_StoppingCondition.txt           %% text file, a text file contains only two items (source node & condition of the Target)
   

 Remarks: 

   N: is an integer, which shows the Number of nodes in the given Graph G.
  
  "AdjacencyMatrix_of_Graph_G.txt" includes the Adjacency Matrix of graph G (for example Matrix A with size N*N ).
  if A(i,j) == 0, there is no edge between Node i & Node j. 
  if A(i,j) == 1, there is an edge between Node i & Node j. 

   Each node in the graph corresponds to a city, and
   "Node_Information_of_Graph_G.txt"  is a text file which has N row and each row indicates the information 
   of the corresponding node (infect corresponding city). This file has 4 columns including : 
   Node#, CityName, Population, HighestElevation. 

   "SourceNode_StoppingCondition.txt", is a text file which has only two columns and one row (only two items: source node & condition of the Target node)

  
 
Outputs:

    DFS and/or BFS search program will create two text files  for each graph G with N nodes (N here is =100 or 1000) as follows:
    1)  Result_of_BFS_from_Source_to_Target_N_100(or1000).txt
    2)  Result_of_DFS_from_Source_to_Target_N_100(or1000).txt
    The search stop when the algorithm encounter a node that satisfies condition of the Target or all Graph nodes are visited and no node found as the target, and all the results of visited nodes
    are reported in these two files.

   
For Python£¬the code file need to put into the same folder with the input text file, then do the execution.
the runtime environment is windows7 version Python2.7.6
