
/* Kui Te seda lehekülge näete, tegi Teie brauser vea JavaScript programmi lugemisel. */
/* Et tagasi saada, vajutage brauseris nupule "Back" */

/* Soovitame kasutada uuemaid brauserite versioone. Viited leiate, näiteks, aadressil: */
/* http://www.ttkool.ut.ee/tarkvara.html */

function getMenu(width,links,items,lenght){
	document.writeln('<hr size="1">');
	document.writeln('<a class="leftmenu" href="/tarkvara.html">Tarkvara</a>');
	document.writeln('<hr size="1">');
	document.writeln('<a class="leftmenu" href="ftp://ftp.ttkool.ut.ee/">FTP server</a>');
	document.writeln('<hr size="1"><br>');

	for(var i = 0; i < lenght; i++) {
		document.writeln('<hr size="1">');
		if (links[i].substring(0,1) == '#') {
			document.writeln('<a class="leftmenu" href="index.html' + links[i] + '">' + items[i] + '</a>');
		} else {
	 		document.writeln('<a class="leftmenu" href="' + links[i] + '">' + items[i] + '</a>');
		}
	}

	document.writeln('<hr size="1">');
	document.writeln('<img hspace="0" width="' + width + '" height="1" src="/pics/empty.gif">');
	document.writeln('</td><td valign="top">');

}

function getHeader(){
	document.writeln('<table border="0" cellspacing="0" cellpadding="0" width="620" bgcolor="navy"><tr><td>');
	document.writeln('<table border="0" cellspacing="1" cellpadding="0" width="620"><tr><td bgcolor="white">');

	document.writeln('<table border="0" cellspacing="0" cellpadding="0" width="618">');

	document.writeln('<tr><td bgcolor="#FFFFCC" colspan="15"><center><a href="index.html"><img border="0" src="pics/title.gif"></a></center></td></tr>');

	document.writeln('<tr>');
	document.writeln('<td class="topmenu"><img src="/pics/empty.gif" width="5" height="22"></td>');
	document.writeln('<td class="topmenu"><a class="topmenu" href="/math/">Matemaatika</a></td>');
	document.writeln('<td class="topmenu">|</td>');
	document.writeln('<td class="topmenu"><a class="topmenu" href="/comp/">Informaatika</a></td>');
	document.writeln('<td class="topmenu">|</td>');
	document.writeln('<td class="topmenu"><a class="topmenu" href="/phys/">Füüsika</a></td>');
	document.writeln('<td class="topmenu">|</td>');
	document.writeln('<td class="topmenu"><a class="topmenu" href="/chem/">Keemia</a></td>');
	document.writeln('<td class="topmenu">|</td>');
	document.writeln('<td class="topmenu"><a class="topmenu" href="/bio/">Bioloogia</a></td>');
	document.writeln('<td class="topmenu">|</td>');
	document.writeln('<td class="topmenu"><a class="topmenu" href="/geo/">Geograafia</a></td>');
	document.writeln('<td class="topmenu">|</td>');
	document.writeln('<td class="topmenu"><a class="topmenu" href="/">Esileht</a></td>');
	document.writeln('<td class="topmenu"><img src="/pics/empty.gif" width="5" height="20"></td>');
	document.writeln('</tr>');
	
	document.writeln('</table>');

	document.writeln('<table border="0" cellspacing="0" cellpadding="20" width="618"><tr><td valign="top">');
}

function getFooter(){
	
	document.writeln('<br><hr size="1">');
	document.writeln('<center><img src="/pics/empty.gif" border="0" height="10"></center>');
	if ((document.location.href.substring(0,27) == '/bio')) { 
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:illarl@ut.ee?subject=" + '" + document.URL + "' + "'>illarl@ut.ee</a>" + '")</script></small></center>');
	} else if ((document.location.href.substring(0,27) == '/geo')) { 
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:yllel@ut.ee?subject=" + '" + document.URL + "' + "'>yllel@ut.ee</a>" + '")</script></small></center>');
	} else if ((document.location.href.substring(0,28) == '/phys')) { 
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:ttkool@ut.ee?subject=" + '" + document.URL + "' + "'>ttkool@ut.ee</a>" + '")</script></small></center>');
	} else {	
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:ttkool@ut.ee?subject=" + '" + document.URL + "' + "'>ttkool@ut.ee</a>" + '")</script></small></center>');
	}

	document.writeln('<center><small>Viimati muudetud: <script language="JavaScript">document.write(document.lastModified)</script></small></center>');
	document.writeln('<center><small>© 1996-2004 Tartu Ülikool</small></center>');

	document.writeln('</td></tr></table>');
	document.writeln('</td></tr></table>');
	document.writeln('</td></tr></table>');
}

function tyhi() {
	window.status=''; 
	return true;
}


function getFooter1(){
	
	document.writeln('<br><hr size="1">');
	document.writeln('<center><img src="/pics/empty.gif" border="0" height="10"></center>');
	if ((document.location.href.substring(0,27) == '/bio')) { 
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:illarl@ut.ee?subject=" + '" + document.URL + "' + "'>illarl@ut.ee</a>" + '")</script></small></center>');
	} else if ((document.location.href.substring(0,27) == '/geo')) { 
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:yllel@ut.ee?subject=" + '" + document.URL + "' + "'>yllel@ut.ee</a>" + '")</script></small></center>');
	} else if ((document.location.href.substring(0,28) == '/phys')) { 
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:ttkool@ut.ee?subject=" + '" + document.URL + "' + "'>ttkool@ut.ee</a>" + '")</script></small></center>');
	} else {	
		document.writeln('<center><small>Kõik küsimused selle lehe kohta saata aadressil  <script language="JavaScript">document.write("<a href=' + "'mailto:ttkool@ut.ee?subject=" + '" + document.URL + "' + "'>ttkool@ut.ee</a>" + '")</script></small></center>');
	}

	document.writeln('<center><small>Viimati muudetud: <script language="JavaScript">document.write(document.lastModified)</script></small></center>');
	document.writeln('<center><small>© 1996-2004 Tartu Ülikool</small></center>');
	document.writeln('<center><img src="pics/empty.gif" border="0" height="10"></center>');
	document.writeln('<center><a href="http://www.eenet.ee/" target="_blank"><img src="http://nw.eenet.ee/logo/eenet_sinimustvalge_vaike.gif" border="0" alt="Serverit teenindab EENet"></a></center>');

	document.writeln('</td></tr></table>');
	document.writeln('</td></tr></table>');
	document.writeln('</td></tr></table>');
}