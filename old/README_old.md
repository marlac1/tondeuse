<h2>GOAL</h2>
An input file provides the following datas : the surface of an area, the initial position and orientation of mowers and instructions to move them. The program aims to return mower's final position and orientation. 

<h2>INSTRUCTIONS</h2>
<ul>
<li>Requirements : python 3.9</li>
<li>Inside the project's folder, execute the program "test_updated.py" with "input.txt" argument : <i> $python test_updated.py input.txt </i>. "Test_updated.py" is the last version of my answer to the technical test.</li>
<li>You will find the output of the program in the terminal.</li>
</ul>

<h2>ALGO :</h2>
I divided the program into two classes representing the mower "TondeuseUpdated" and input datas "InputDatasUpdated".
Once extracted from the file and cleaned, datas are used as attributes of the mower object.
Several methods are processed among this object to return its final position and orientation.
</br>
</br>

<ol>
<li>InputDatasUpdated class
Calling its methods returns cleaned file datas as a list of tuples containing the position (x, y), orientation and instructions of each mower (for example : <i> [('4', '4', 'S', 'GADDAAGADAA')]</i>)</li>
<li>TondeuseUpdated class
Calling its methods returns the final position (x, y) and orientation of each mower. 
The algo follows these steps :
   <ul>
   <li><strong>The program translates instructions ("DG") strings to orientations ("N", "S", "E", "W") and action ("A") strings </strong> inside a list. For example, <i>'GADDAAGADAA'</i> will be translated as <i>['E', 'A', 'W', 'A', 'A', 'S', 'A', 'W', 'A', 'A']</i>.</li>
   <li><strong>This list is looped over to increment or decrement x and y : each character orientation corresponds to an elevation or decrease of x and y</strong>. 
Also, <strong>x and y values are limited to area's surface</strong>.</li>
   </ul>
   </li>
</ol>