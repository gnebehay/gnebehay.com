title: About me

<script>
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
</script>

<img class='sidecolumn' style='border: 2px solid black' width='200' src='portrait.jpg' alt='My portrait' />

I am a lead engineer at [Locatee][1] in Zurich, Switzerland, where I started working as a data scientist on indoor localization using Wifi data.

Previously, I was a PhD student at the Austrian Institute of Technology,
where I worked together with Roman Pflugfelder.
My PhD supervisor was [Horst Bischof][2] from the Institute for Computer Graphics and Vision
at the Graz University of Technology.

My research was revolving around novel computer vision algorithms for object tracking,
with a focus on methods that are applicable to a wide range of object classes and scenarios
while not requiring any manual adaptation or re-training (model-free object tracking).

The main result of my work as a PhD student is the algorithm [CMT](/cmt)
that allows for tracking deformable objects.

During my master's program I created a [C++ implementation of Zdenek Kalal's OpenTLD](/tld),
a tracking algorithm that sparked [quite some interest in popular media][3].

<a href="https://twitter.com/gnebehay" target="_blank"><img src="/img/Twitter_logo_blue.png" alt="Follow me on twitter" width="46"></a>
<a href="https://github.com/gnebehay" target="_blank"><img src="/img/Octocat.png" width="46" alt="View my GitHub page"></a>
<script>insert_mail_address();</script>
<noscript>Sorry, you need Javascript on to email me.</noscript>


[1]: http://www.locatee.ch
[2]: http://www.icg.tugraz.at/Members/bischof
[3]: http://www.engadget.com/2011/03/31/zdenek-kalals-object-tracking-algorithm-learns-on-the-fly-like
