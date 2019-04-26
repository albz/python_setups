@REM Adapt folder name
@REM PATH=C:\Users\a.marocchino\AppData\Local\Continuum\anaconda3\Sciprts;%PATH% 
@SET PATH=C:\Users\a.marocchino\AppData\Local\Continuum\anaconda3\envs\py37_knime;%PATH% 
@CALL activate py36_knime || ECHO Activating py36_knime failed
@python %*