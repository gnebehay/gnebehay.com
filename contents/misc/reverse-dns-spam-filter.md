title: Reverse DNS as a spam filter
date: 2018-03-17
comments: true

One of the most important spam filters in use nowadays involves reverse DNS lookup.
Let us see why this is important by pretending we have a server on the domain example.com
running on the IP address A.B.C.D. and we want to send a mail from there to a @gmail.com address.
This is what happens.

- The SMTP server at example.com opens a connection to the gmail SMTP server.
- The gmail server should be very suspicious of course because anyone can open a connection, so it would like to filter emails sent from random servers on the internet.
- One assumption here is apparently that if you want to send mail you should also have a DNS entry.
- Furthermore, the mail server that the email is coming from should be the mail server for that domain.
- So what happens it that first of all the gmail server does a reverse DNS lookup for the IP address that the connection comes from.
- If the reverse DNS is setup properly, it should resolve to example.com.
- Of course, when I configure reverse DNS for my server I can just type in anything, for example tralala.com
- To complete the checking loop, a forward DNS lookup needs to be performed and that lookup should resolve back to the original IP address.

Prior to 2018-03-17, the following settings were in place:

DNS entry for schosel.net: 77.37.11.150 
DNS entry for nebehay.com: 77.37.11.150 
reverse lookup of this IP address: schosel.net

On 2018-03-17 the DNS entry for schosel.net was changed to 51.15.89.77, while nebehay.com was left as is.
The reverse lookup of 77.37.11.150 was left unchanged and no reverse lookup was configured for the new IP address.
We were now sending mail from both the old address and the new address, but neither of those servers would actually pass the DNS reverse lookup spam check:

mail from 77.37.11.150 -> reverse lookup is schosel.net -> lookup of schosel.net is 51.15.89.77 -> fail
mail from 51.15.89.77 -> reverse lookup is x.y.z.scaleway.com -> No dns entry available -> fail

I was somehow stubbornly believing that the reverse DNS entry should be set in you domain provider, but in fact you have to change it in your hosting provider.

The actual solution was super simple, one just has to set the proper lookups. This also works without problems for sending mail from different addresses, because the addresses themselves are never involved in the checking. Maybe there are other checks that do that (e.g. SPF?), but for sure it is not part of the reverse DNS check.



