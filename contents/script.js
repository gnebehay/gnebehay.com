function toggle_visibility(id) {
    var e = document.getElementById(id);
    if(e.style.display == 'block')
      e.style.display = 'none';
    else
      e.style.display = 'block';
}

function insert_mail_address() {
  // Email obfuscator script 2.1 by Tim Williams, University of Arizona
  // Random encryption key feature by Andrew Moulden, Site Engineering Ltd
  // This code is freeware provided these four comment lines remain intact
  // A wizard to generate this code is at http://www.jottings.com/obfuscator/
  coded = "UqGWGbvK@Ufv1H.0Nf"
    key = "tak04Zphnr3lPMy5Eg6vVsxizbqYSHR2KoLUADIem18WwO9cQTdNJFBX7GfujC"
    shift=coded.length
    link=""
    for (i=0; i<coded.length; i++) {
      if (key.indexOf(coded.charAt(i))==-1) {
        ltr = coded.charAt(i)
          link += (ltr)
      }
      else {
        ltr = (key.indexOf(coded.charAt(i))-shift+key.length) % key.length
          link += (key.charAt(ltr))
      }
    }
  document.write("<a href='mailto:"+link+"'><img src='/img/googlemail-64.png' width='46' alt='Email me'/></a>")
}

(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

ga('create', 'UA-61297334-1', 'auto');
ga('send', 'pageview');

