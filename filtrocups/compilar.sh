sudo rm fpyfacil.pyc
sudo python -m compileall fpyfacil.py
sudo chmod ugo+x fpyfacil.pyc
sudo cp fpyfacil.pyc /usr/lib/cups/filter/fpyfacil
sudo /etc/init.d/cups restart

