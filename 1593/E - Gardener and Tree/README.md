<h3><a href="https://codeforces.com/contest/1593/problem/E" target="_blank" rel="noopener noreferrer">Gardener and Tree</a></h3>

<div class="header"><div class="title">E. Gardener and Tree</div><div class="time-limit"><div class="property-title">time limit per test</div>4 seconds</div><div class="memory-limit"><div class="property-title">memory limit per test</div>256 megabytes</div><div class="input-file input-standard"><div class="property-title">input</div>standard input</div><div class="output-file output-standard"><div class="property-title">output</div>standard output</div></div><div><p>A tree is an undirected connected graph in which there are no cycles. This problem is about non-rooted trees. A leaf of a tree is a vertex that is connected to <span class="tex-font-style-bf">at most one</span> vertex.</p><p>The gardener Vitaly grew a tree from $$$n$$$ vertices. He decided to trim the tree. To do this, he performs a number of operations. In one operation, he removes <span class="tex-font-style-bf">all</span> leaves of the tree.</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/390f0f2fee2dccde0befa41c992fa715c0864037.png" style="zoom: 100.0%;max-width: 100.0%;max-height: 100.0%;"> <span class="tex-font-size-small">Example of a tree.</span> </center><p>For example, consider the tree shown in the figure above. The figure below shows the result of applying exactly one operation to the tree.</p><center> <img class="tex-graphics" src="https://espresso.codeforces.com/3e241ec4bc248a37748afb14103a67d47298e571.png" style="zoom: 100.0%;max-width: 100.0%;max-height: 100.0%;"> <span class="tex-font-size-small">The result of applying the operation "remove all leaves" to the tree.</span> </center><p>Note the special cases of the operation:</p><ul> <li> applying an operation to an empty tree (of $$$0$$$ vertices) does not change it; </li><li> applying an operation to a tree of one vertex removes this vertex (this vertex is treated as a leaf); </li><li> applying an operation to a tree of two vertices removes both vertices (both vertices are treated as leaves). </li></ul><p>Vitaly applied $$$k$$$ operations sequentially to the tree. How many vertices remain?</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line contains one integer $$$t$$$ ($$$1 \le t \le 10^4$$$) — the number of test cases. Then $$$t$$$ test cases follow.</p><p>Each test case is preceded by an empty line.</p><p>Each test case consists of several lines. The first line of the test case contains two integers $$$n$$$ and $$$k$$$ ($$$1 \le n \le 4 \cdot 10^5$$$, $$$1 \le k \le 2 \cdot 10^5$$$) — the number of vertices in the tree and the number of operations, respectively. Then $$$n - 1$$$ lines follow, each of them contains two integers $$$u$$$ and $$$v$$$ ($$$1 \le u, v \le n$$$, $$$u \neq v$$$) which describe a pair of vertices connected by an edge. It is guaranteed that the given graph is a tree and has no loops or multiple edges.</p><p>It is guaranteed that the sum of $$$n$$$ from all test cases does not exceed $$$4 \cdot 10^5$$$.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case output on a separate line a single integer — the number of vertices that remain in the tree after applying $$$k$$$ operations.</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input<div title="Copy" data-clipboard-target="#id00025331237894402836" id="id0047004271888385474" class="input-output-copier">Copy</div></div><pre id="id00025331237894402836">6

14 1
1 2
2 3
2 4
4 5
4 6
2 7
7 8
8 9
8 10
3 11
3 12
1 13
13 14

2 200000
1 2

3 2
1 2
2 3

5 1
5 1
3 2
2 1
5 4

6 2
5 1
2 5
5 6
4 2
3 4

7 1
4 3
5 1
1 3
6 1
1 7
2 1
</pre></div><div class="output"><div class="title">Output<div title="Copy" data-clipboard-target="#id007817265809115268" id="id008118855356941644" class="input-output-copier">Copy</div></div><pre id="id007817265809115268">7
0
0
3
1
2
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>The first test case is considered in the statement.</p><p>The second test case contains a tree of two vertices. $$$200000$$$ operations are applied to it. The first one removes all two vertices, the other operations do not change the tree.</p><p>In the third test case, a tree of three vertices is given. As a result of the first operation, only $$$1$$$ vertex remains in it (with the index $$$2$$$), the second operation makes the tree empty.</p></div>