Support functions for BBLs and BINs (key identifiers in the NYC property ecosystem).

Logically these functions are mostly trivial - simple stuff like tell you "is this a valid BBL/BIN"
(for certain degrees of "valid"); splitting BBLs into (and forming them out of) components, etc.  
But simple though they are, it's also easy to screw them up.  So the point of this package is 
to not screw them up.  And to have them all in one place.

About BBLs and BINs
-------------------

BBLs and BINs are numeric identifiers unique to the the NYC data ecosystem (used in various 
databases put out by the City).  Conceptually they're both very simple, but in practice they 
both have certain quirks and caveats.

**BBL**

The BBL (or "Borough, Block, Lot") number refers to a *tax parcel*, which is usually 
an actual, physical lot (in the property's block-and-lot system); but sometimes a 
condominium unit, and something something more abstract like an air rights parcel.
It's always a 10-digit number, and the first number corresponds to the "borough number"
(1 for Manhattan; 2-5 for the others, in alphabetical order).

And from there, it gets more complicated: lots get "de-mapped" and seem to disappear
from the city's tax maps (and from it's geocoding API) even though people still have 
mortgages on them (or they're still linked to other records).  And when properties
go condo, a new magical "bank" BBL (with a special lot number always in the range 
7501-7569) gets assigned (but this assignation only goes out to some databases;
others still keep tracking the now de-mapped, "physical" lot number).

**BIN**

The BIN (Building Identification Number) is just that, a numeric identifier for a 
single building.  Except when it isn't: there are some 2k+ duplicate (or n-to-1) BINs
that are assigned to multiple buildings (sometimes on completely different lots); and 
some 20k+ buildings don't have proper BINs at all, but are assigned what we call a 
"degenerate" BIN (and what others call a "million" BIN), which have all zeros except 
for the leading digit (which is also the borough number, as with BBLs).

To complicate matters further, the degenerate BINs are frequently used as de-facto 
foreign keys in many city databases (even though strictly speaking they're "broken" 
as proper database keys, due to their non-uniqueness).  But this is actually OK 
(or OK enough) in practice, because in context they're usually used in association
with a BBL; so as a composite key what the degenerate BIN means is "the building on
this lot" or "the *other* building on this lot" (besides the one with a 
non-degenerate BIN).  

In any case they're always 7 digits.  

**Further Info**

* https://en.wikipedia.org/wiki/Borough,_Block_and_Lot
* BINs are a bit more obscure.  Good luck finding info about them!


