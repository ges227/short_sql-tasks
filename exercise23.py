import sys
from model2 import *

init()
try:
	inputname= str(sys.argv[1])
except IndexError:
	print >>sys.stderr, "Need an Organism name argument"
	sys.exit(1)
try:
	hsname= Name.selectBy(name=inputname)[0]
except IndexError:
	print "No record of '"+inputname+"' in the current database 'small_taxa.db3'"
	sys.exit(1)
t=hsname.taxonomy
print "Organism",inputname, "has scientific name:", t.scientific_name, "and rank:", t.rank 

def findchildren(taxon):
	for c in taxon.children:
		print taxon.scientific_name+ " has child: "+ c.scientific_name+ ", and rank:", c.rank
		findchildren(c)
r=t
print "\t\t*******lower level lineage*******"
findchildren(r)
print "\t\t*******higher level lineage*******"
while r != r.parent:
	print "Name:"+r.scientific_name+", rank:",r.rank
	r=r.parent 
