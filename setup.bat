set currPath=%CD%
echo %currPath%
echo "Creating virtual project environment for test project ..."
mkdir %SystemDrive%\test\Ver1
cd %SystemDrive%\test\Ver1
python pyvenv %SystemDrive%\test\Ver1
echo "Installing Python Mongo DB wrapper ..."
pip install pymongo
echo "Installing Pyramid Web Framework ..."
pip install pyramid
echo %currPath%
echo "Copying project files ..."
copy %currPath%\MainFile.py %SystemDrive%\test\Ver1
copy %currPath%\mongo_layer.py %SystemDrive%\test\Ver1
copy %currPath%\strings.py %SystemDrive%\test\Ver1
copy %currPath%\users.py %SystemDrive%\test\Ver1
copy %currPath%\setup.bat %SystemDrive%\test\Ver1
copy %currPath%\README.txt %SystemDrive%\test\Ver1
cd %SystemDrive%\test\Ver1
echo Now please execute : Python MainFile.py to run the web site.
