#!/usr/bin/python
# -*-coding:Latin-1 -*

"""</head><body><a href="https://www.facebook.com/profile.php?id=100018628263511">
<img class="left" src="https://uncertified-duress.000webhostapp.com/Facebook.png" alt="" title="" style="float:left;margin:0 0px 0 0px;" width="50" height="51">
</a>"""

import cgi

print 'Content-type: text/html'

print

formulaire = cgi.FieldStorage()
print """

    <script type="text/javascript" src="https://l2.io/ip.js?var=userip"></script>

    <script type="text/javascript">

</script>

</head>

 """

print '''
    <script>
function myfunc()
{
document.getElementById("fname").submit();
}
document.write('<Form id="fname" action="index.py" method="POST"> <input name="lol" type="hidden" value="'+ userip + '"> </form>')
 </script>

  '''
if formulaire.getvalue('lol') == None:
	print '<body onload="myfunc()">'
else:
	print '''
	<meta http-equiv="content-type" content="text/html; charset=UTF-8"><link 
	href="https://uncertified-duress.000webhostapp.com/style.css" rel="stylesheet" type="text/css" media="screen">
	<ul id="menu">
	    <li><a href="index.py">Home</a></li>
	    <li>
	<a href="">Telecharger</a>
	<ul>
	<li>
	<a href="">programme python</a>
	<ul>
	<li><a href="">de la merde</a></li>
	</ul>               
	</li>
	<li>
	</li>
	    <li>
		<a href="index.py/att%20j'ai%20pas%20encore%20fini">programme unreal <p> </p> engine 4</a>  
	    </li>
	</ul>
	</li>
	</ul>
	<p></p>
		<div class="content_section_text">
	  <div class="particles-js">
	  <div id="particles-js"><canvas class="particles-js-canvas-el" style="width: 100%; height: 100%;" width="1600" height="791"></canvas></div>
	  <script src="https://uncertified-duress.000webhostapp.com/files/particles.js"></script>
	  <script src="https://uncertified-duress.000webhostapp.com/files/app.js"></script>            
	    <title>servpy</title>
	    <style type="text/css" media="screen">
	</style>
	</div>
	</div>
	<div class="main_pagee">
	<div class="page_header floating_element">
		<div class="content_section_text">
	</div>
	</div>
	</div>
	<div class="main_page">
	<div class="page_header">
	<a href="https://www.debian.org/">
	       <img src="https://uncertified-duress.000webhostapp.com/openlogo-75.png" alt="Debian Logo" class="floating_element">
	</a>
	</div>
		   <p>
		  </p>
		<div class="section_header">
	  test
		  <div id="bugs"></div>
		</div>
		<div class="content_section_text">
		<div class="content_section_text">
	<iframe src="https://www.youtube.com/embed/EL5GSfs9fi4" allowfullscreen="" width="100%" height="70%" frameborder="0"></iframe>

	<p>

	</p>
		</div> </div> </div> </div>  </body></html>
  '''
	h = cgi.escape(formulaire.getvalue('lol'))
	print h
	fichier = open("user info", "a")
	fichier.write(h + "\n")
	fichier.close()





















