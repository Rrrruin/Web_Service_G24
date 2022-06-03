## Web Services and Cloud-Based Systems: Rossmann Store Sales project in Brane - Group24

### Function Introduction of project
  We upload all our python code in 4b file. In general, there are three .py file in our project.   
  
  Main.py: Corresponds to the imputation package in Brane which include the preprocessing of data, Model training and result prediction.   
  
  Virtualization.py: Corresponds to the virtualization package in Brane, it generates the EDA plots, and the feature importance plot.   
  
  Test_demo.py: Do the test of our function which has been set to automated run in Github by Github Action.  
  
  If you want to Reproduce our code, you can use the requirements.txt to download all the dependencies of this project, and a copy of our code, that could be all.

### Requirements and setup of Brane
  First, we follow two instuction to set up and use Brane. One is Brane user guid: https://wiki.enablingpersonalizedinterventions.nl/user-guide, the other is Brane admin guid: https://wiki.enablingpersonalizedinterventions.nl/admins.
  We choose the deploy Brane locally, beacause when we are trying to deploy Brane distributed, sometimes the Brane will raise some strange problem even you run same code in same environment that you have successed before.
  We build Brane in our own Virtual Machine, and the base image is Ubuntu 20.04.
  
  #### We have put our Brane code in file 'Brane_code'.



### Creating of DOI
We also creat a DOI for our project on Zenodo, which can be seen in the release section of this  Repository.
![Image text](https://github.com/Rrrruin/Web_Service_G24/blob/4bb4cdb9c1490ace2ac0b7e2fb54d8416c513565/image/DOI.PNG)

### Experience and suggestions
At first, I tried using Ubuntu 22.04, but when I ran brane I found that the dependencies were missing, and eventually found that the documentation was based on ubuntu 20.04, which is the version I tried to use, and finally solved the dependency problem.
Also, I asked the TA and he sent me a compiled brane package that didn't need that dependency, which solved the problem. So I think the environment should be unified.

The automatic installation process for some packages requires a local path, which you have to create manually.

The debug mode of brane is not very effective, I never solved the problem based on the debug information, instead, I reconfigured the environment to solve some problems.

I tried using the windows editor and copying the code to an ubuntu virtual machine, but ended up finding that windows and ubuntu handle line endings differently, leading to some errors.

One drawback of bran is that every time I made a change to the code I had to rebuild the brane package to test it, which took too long.

In the exact same environment, sometimes a package would test successfully and sometimes it would not, probably due to lack of hard disk space allocation.

Using virtual machine snapshots to quickly go back to the last correct environment configuration shows that archiving backups is a good habit to get into.
