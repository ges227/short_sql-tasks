import sys
import sqlite3


if len(sys.argv)<2:
	print "please input the organism in your command line call"
	sys.exit(1) 
inputname=[sys.argv[1]]
conn = sqlite3.connect('taxa.db3')
c=conn.cursor()
c.execute("""
	select * from taxonomy,name 
	where name.name=? 
	 and taxonomy.tax_id=name.tax_id
	""",inputname)
for row in c:
	scientific_name=row[1]
	print "Scientific name:", row[1]