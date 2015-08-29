# pentoo

#Install google earth

copy package.accept_keywords,package.license,package.unmask to /etc/portage folder.

then run emerge --autounmask googleearth which will download and install googleearth

#Install adsb receiver

download the scripts folder from repo and run:

make install
ldconfig

finally run the software using modes_rx -s osmocom
