#!/bin/bash
pip install sine-calc --break-system-packages
touch /bin/launchsine 
echo "#!/bin/bash" >> /bin/launchsine
echo "$HOME/.local/bin/sine-calc" >> /bin/launchsine
cp desktop.desktop $HOME/.local/share/applications/sine.desktop