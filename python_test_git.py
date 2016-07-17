import subprocess
import os
	
print subprocess.check_output(['git', 'rev-parse','HEAD'])
#print subprocess.check_output(['git', 'log'])

nr_of_commits_master = int(subprocess.check_output(['git', 'rev-list','--count','master']))

print nr_of_commits_master 

nr_of_commits_nexus = int(subprocess.check_output(['git', 'rev-list','--count','bdf0cafbd8545b8225adc89e4d19f00ce6b39f38'])) #the last argument should be the commit hash that has been deployed to Nexus

print nr_of_commits_nexus

print 'the number of commits from nexus to master ='
print nr_of_commits_master - nr_of_commits_nexus	#prints the difference (the number that we need)

path="/home/d066645/hanalite-vora" #the path will be different for every component - using get_component_dir()?
# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print "Directory changed successfully %s" % retval

nr_of_commits_master = int(subprocess.check_output(['git', 'rev-list','--count','master']))

print nr_of_commits_master 

nr_of_commits_nexus = int(subprocess.check_output(['git', 'rev-list','--count','32706805af6e62610d0361c5daf80315ccb7f9c3'])) #the last argument should be the commit hash that has been deployed to Nexus

print nr_of_commits_nexus

print 'the number of commits from nexus to master ='
print nr_of_commits_master - nr_of_commits_nexus #prints the difference (the number that we need)


