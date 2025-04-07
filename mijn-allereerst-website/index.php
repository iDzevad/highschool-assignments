<!DOCTYPE html>
	<head> 
		<meta name="viewport" content="widht=device-width, initial-scale=1,0">
		<meta charset="utf-8">		
		<link rel="shortcut icon" type="image/png" href="IMAGES/favicon.png">
		
	</head>

	<body class="body"> 
		<header class="mainheader">
			<a href="index.php?page=1">
				<img src="IMAGES/logo.png" alt="DwaneWeb">
			</a>

			<nav> 
				<ul>
                        <li><a href="index.php?page=1">Home</a></li>
						<li><a href="index.php?page=2">Overmij</a></li>
						<li><a href="index.php?page=3">Dagboek</a></li>
						<li><a href="index.php?page=4">Opdrachten</a></li>
						<li><a href="index.php?page=5">Ontwerp</a></li>
				</ul>
			</nav>
		</header>

		<div class="maincontent">
			<div class="content">
				<article class="topcontent">
					<header>
						<h2 class="mainpageh2"></h2>
					</header>
                   
                   
             <article>

			<?php
			if (isset( $_GET["page"]))
			{
				$nummer = $_GET["page"];
			}
			else
			{
				$nummer = 1;
			}

			switch ($nummer)
			{
				case 1:
					readfile("home.inc");
					break;

				case 2:
					readfile("overmij.inc");
					break;

				case 3:
					readfile("eendag.inc");
					break;

				case 4:
					readfile("opdrachten.inc");
					break;

				case 5:
					readfile("ontwerp.inc");
					break;

				case 6:
					readfile("logocode.inc");
					break;

				default:
					readfile("home.inc");
			};
			?>
		</article>

					<footer>
						<p class="post-info"></p>
					</footer>

					<content>
						<p></p>
					</content>
				</article>
				<article class="bottomcontent">
					<header>
						<h2 class="mainpageh2"></h2>
					</header>

					<footer>
						<p class="post-info"></p>
					</footer>
					<content>
						<p>
						</p>
					</content>
				</article>
			</div>
		</div>




		<footer class="mainfooter">
			<p>Copyright &copy; Dwaneweb.nl</p>
		</footer>
		
	</body>


</html>