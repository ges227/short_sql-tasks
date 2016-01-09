from model import *
import sys
try:
	inputname= str(sys.argv[1])
except IndexError:
	print >>sys.stderr, "Need an Organism name argument"
	sys.exit(1)
try:
	hsname= Name.selectBy(name=inputname)[0]
	#for n in Name.selectBy(name=inputname):
	#	print "scientificName=" n.taxa.scientificName 
except IndexError:
	print "No record of '"+inputname+"' in the name table"
	sys.exit(1)
print "Scientific Name:",hsname.taxa.scientificName
