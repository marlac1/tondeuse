<h2>GOAL</h2>
An input file provides the following datas : the surface of an area, the initial position and orientation of mowers and instructions to move them. The program aims to return mower's final position and orientation. 

<h2>INSTRUCTIONS</h2>
<ul>
<li>Requirements : python 3.9</li>
<li>Inside the project's folder, execute the program "test.py" with "input.txt" argument : <i> $python test.py input.txt </i></li>
<li>You will find the output of the program in the terminal.</li>
</ul>

<h2>ALGO :</h2>
I divided the program into two classes representing the mower "Tondeuse" and input datas "InputDatas".
Once extracted from the file and cleaned, datas are used as attributes of the mower object.
Several methods are processed among this object to return its final position and orientation.
</br>
</br>

<ol>
<li>InputDatas class
Calling its methods returns cleaned file datas as a list of tuples containing the position (x, y), orientation and instructions of each mower (for example : <i> [('4', '4', 'S', 'GADDAAGADAA')]</i>)</li>
<li>Tondeuse class
Calling its methods returns the final position (x, y) and orientation of each mower. 
The algo follows these steps :
   <ul>
   <li><strong>The program translates instructions ("DG") strings to orientations ("N", "S", "E", "W") and action ("A") strings </strong> inside a list. For example, <i>'GADDAAGADAA'</i> will be translated as <i>['E', 'A', 'W', 'A', 'A', 'S', 'A', 'W', 'A', 'A']</i>.</li>
   <li><strong>This list is looped over to increment or decrement x and y : each character orientation corresponds to an elevation or decrease of x and y</strong>. 
Also, <strong>x and y values are limited to area's surface</strong>.</li>
   </ul>
   </li>
</ol>

<h2>SUGGESTED IMPROVEMENTS</h2>
<ul>
<li>Algo : This algorithm is heavy and its cyclomatic complexity is too big. This can be reduced by not creating an intermediary string. How can it be implemented ?</li>
<li>Inside the code : I refactored my code to avoid redudancies, by creating one task functions. Despite this work, redudancies exist, due to the choice of the algorithm.</li>
</ul>