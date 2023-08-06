echo off
echo Setting up your conda enviroment:
echo Change the Anaconda path "...\activate.bat" to your own
echo To print your Anaconda path, run this in Anaconda prompt:
echo $ where conda
echo In a multi-user setting, you can create the py37 environment in a public folder accessible for all users:
echo $ conda create -p C:/Users/Public/conda/envs/mesoSPIM-py37 python=3.7
echo Make sure all users have right to execute python in this py37 environment (admin rights required).
echo off
"%windir%\System32\cmd.exe" /k ""C:\Users\Nikita\anaconda3\Scripts\activate.bat" "C:\Users\Public\conda\envs\mesoSPIM-py37" && "mesospim-control""
pause