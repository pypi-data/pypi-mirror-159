<h1>KiwiCalc</h1>
<h2>Abstract</h2>
The project is intended to help integrating mathematical
expressions in python with greater ease and provide powerful
tools along them.
Python's syntax can be cumbersome when it comes to 
more sophisticated mathematical notations, so wouldn't it be easier to
use them in a more intuitive "math-like" syntax?


<img src="https://github.com/jonaprojects/kiwicalc/blob/main/kiwicalc_functions16x9.gif" >


<h2>Sources</h2>

* Official website: <a href="https://www.kiwicalc.com">kiwicalc.com</a>
  
* <a href="https://www.kiwicalc.com/documentation">Official Documentation </a>

* <a href="https://colab.research.google.com/drive/1x411iW1nczAp67YBfp55Erd-72Nd7k7Z?usp=sharing">Google Colab.</a>
* <a href="https://github.com/jonaprojects/kiwicalc">GitHub</a>.


<h2>Installation</h2>

You can install the library with <code>pip</code>, by executing the command <code>pip install kiwicalc</code> in your command prompt.
  
<h2>Basic Examples</h2>
First, import kiwicalc:

<code>from kiwicalc import *</code>
<h3>Plotting and scattering functions </h3>

<pre lang="python">
my_function = Function("f(x) = x^2")
my_function.plot()
</pre>

<pre lang="python">
my_function = Function("f(x) = sin(x) * cos(y)")
my_function.plot()
</pre>

<pre lang="python">
my_function = Function("f(x,y) = sin(x) * cos(y)")
my_function.scatter3d()
</pre>


  