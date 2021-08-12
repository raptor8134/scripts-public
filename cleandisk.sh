yes | yay -Sc
yes | yay -Rns $(yay -Qtdq)
rm -rf ~/.wine/drive_c/users/$USER/Temp/*
rm -rf ~/.cache/*
sudo journalctl --vacuum-size=50M
rm -rf ~/.config/discord/Cache/*
rm -rf ~/.config/Slack/Cache/*
rm -rf ~/.config/Slack/Service\ Worker/CacheStorage/*
