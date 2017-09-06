title: Zurich Soccer/Football Meetup

<script>
  // Email obfuscator script 2.1 by Tim Williams, University of Arizona
  // Random encryption key feature by Andrew Moulden, Site Engineering Ltd
  // This code is freeware provided these four comment lines remain intact
  // A wizard to generate this code is at http://www.jottings.com/obfuscator/
  coded = "PBBC8://mPDB.gPDB8DCC.mAl/zDrHYRRlUdKZZTLogUBUiU"
  key = "9RcVk12zrChbLGgy3QSUKD0pf5FEw6JIjNMalXxqBdAve8HY7OmiWntToZPsu4"
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
document.write("<a href='"+link+"'>Join our Whatsapp Group</a>")
</script>
