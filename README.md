# ITS Graph Theory class Group 5 Assignment 5

Group 5 Members:

- Maulana Anugra Putra / 5025251159 (kukii83)

- I Gusti Agung Candra Nugraha / 5025251169 (candranugraha576)

- Hussein Mohammad Mahsun / 5025251170 (TheDelightOFice)


# Graph Visualizer: Spanning Forest, Fundamental Cycles & Cut-Sets

A Python-based command-line and graphical tool to analyze undirected graphs. The application accepts either an adjacency matrix or an incidence matrix, computes the spanning forest (tree edges vs. chords), and computes/visualizes the fundamental cycle matrix and fundamental cut-set matrix.

---

## Features

1. **Flexible Matrix Input:** Supports both **Adjacency Matrix** ($n \times n$) and **Incidence Matrix** ($n \times m$).
2. **Spanning Forest Computation:** Discovers tree branches and chords using Disjoint Set Union (Kruskal's spanning forest).
3. **Fundamental Cycle Matrix:** Identifies the unique elementary cycle created by adding each chord to the spanning tree.
4. **Fundamental Cut-Set Matrix:** Identifies cut-sets formed by removing individual tree branches.
5. **Interactive Visualization:**
   - Base graph plot highlighting spanning tree branches in red.
   - Individual subplots for each fundamental cycle.
   - Individual subplots for each fundamental cut-set.

---

## Prerequisites

1. Make sure you have **Python 3.8+** installed along with the required libraries:

```bash
pip install networkx matplotlib
```
2. Copy the program visualizer.py
3. Run the program
4. Pick either 1(for adjacency) or 2(for incidence)
5. Input your graph

---

## Sample Input/Output

Sample Input 1 (choose 1)
```bash
0 1 0 1 1
1 0 1 1 1
0 1 0 0 1
1 1 0 0 1
1 1 1 1 0
```

Sample Output 1
```bash
Edges: e1=(1,2), e2=(1,4), e3=(1,5), e4=(2,3), e5=(2,4), e6=(2,5), e7=(3,5), e8=(4,5)
Tree edges: ['e1', 'e2', 'e3', 'e4']  Chords: ['e5', 'e6', 'e7', 'e8'] 

Fundamental cycle matrix
         e5   e6   e7   e8   e1   e2   e3   e4
   Z1     1    0    0    0    1    1    0    0
   Z2     0    1    0    0    1    0    1    0
   Z3     0    0    1    0    1    0    1    1
   Z4     0    0    0    1    0    1    1    0

Fundamental cut-set matrix
         e1   e2   e3   e4   e5   e6   e7   e8
   c1     1    0    0    0    1    1    1    0
   c2     0    1    0    0    1    0    0    1
   c3     0    0    1    0    0    1    1    1
   c4     0    0    0    1    0    0    1    0
```
<img width="502" height="482" alt="image" src="https://github.com/user-attachments/assets/c2b2a311-185f-4782-8792-497729212a58" />
<img width="1352" height="882" alt="image" src="https://github.com/user-attachments/assets/7fca18f5-301b-4970-9f43-e6fdcfb11ba6" />
<img width="1352" height="882" alt="image" src="https://github.com/user-attachments/assets/a63b4ffd-e090-4ba0-aeaf-f9fbf97a60b9" />


Sample Input 2 (choose 2)
```bash
1 1 1 0 0 0 0 0
1 0 0 1 0 1 1 0
0 0 0 0 0 0 1 1
0 1 0 1 1 0 0 0
0 0 1 0 1 1 0 1
```

Sample Output 2
```bash
Edges: e1=(1,2), e2=(1,4), e3=(1,5), e4=(2,4), e5=(4,5), e6=(2,5), e7=(2,3), e8=(3,5)
Tree edges: ['e1', 'e2', 'e3', 'e7']  Chords: ['e4', 'e5', 'e6', 'e8'] 

Fundamental cycle matrix
         e4   e5   e6   e8   e1   e2   e3   e7
   Z1     1    0    0    0    1    1    0    0
   Z2     0    1    0    0    0    1    1    0
   Z3     0    0    1    0    1    0    1    0
   Z4     0    0    0    1    1    0    1    1

Fundamental cut-set matrix
         e1   e2   e3   e7   e4   e5   e6   e8
   c1     1    0    0    0    1    0    1    1
   c2     0    1    0    0    1    1    0    0
   c3     0    0    1    0    0    1    1    1
   c4     0    0    0    1    0    0    0    1
   ```
<img width="502" height="482" alt="image" src="https://github.com/user-attachments/assets/1213ac3f-f007-4243-8d4f-f3ffd3f5367a" />
<img width="1352" height="882" alt="image" src="https://github.com/user-attachments/assets/a09e804c-7d1a-4a9e-8166-08abad58f9ba" />
<img width="1352" height="882" alt="image" src="https://github.com/user-attachments/assets/2e1c9d04-6396-45e3-9b69-fec66826e765" />


Sample Input 3 (choose 1)
```bash
0 1 1 1
1 0 1 1
1 1 0 1
1 1 1 0
```

Sample Output 3
```bash
Fundamental cycle matrix
e4   e5   e6   e1   e2   e3
    Z1     1    0    0    1    1    0
    Z2     0    1    0    1    0    1
    Z3     0    0    1    0    1    1

Fundamental cut-set matrix
e1   e2   e3   e4   e5   e6
    c1     1    0    0    1    1    0
    c2     0    1    0    1    0    1
    c3     0    0    1    0    1    1
   ```

<img width="2065" height="1125" alt="image" src="https://github.com/user-attachments/assets/5f751401-3987-4585-963a-cecc753c30df" />

---

AI usage:
https://claude.ai/share/7cff1b51-5b65-4c19-9c5e-17d6e6422140
